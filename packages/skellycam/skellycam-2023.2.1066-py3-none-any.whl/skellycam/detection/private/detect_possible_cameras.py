import logging
import time
from threading import Thread

import cv2
import numpy as np

from skellycam.detection.private.found_camera_cache import FoundCameraCache
from skellycam.opencv.config.determine_backend import determine_backend

CAM_CHECK_NUM = 20  # please give me a reason to increase this number ;D

logger = logging.getLogger(__name__)

MIN_RESOLUTION_CHECK = 0   # the lowest width value that will be used to determine the minimum resolution of the camera
MAX_RESOLUTION_CHECK = 10000   # the highest width value that will be used to determine the maximum resolution of the camera
RESOLUTION_CHECK_STEPS = 10 # the number of 'slices" between the minimum and maximum resolutions that will be checked to determine the possible resolutions

class DetectPossibleCameras:
    
    
    def find_available_cameras(self) -> FoundCameraCache:

        self.cams_to_use_list = []
        self.caps_list = []
        self.resolutions_dict = {}
        self.assess_camera_threads = {}
       
        # create a dictionary of threads that will check each port for a real camera 
        for cam_id in range(CAM_CHECK_NUM):
            self.assess_camera_threads[cam_id] = Thread(target=self.assess_camera, args=[cam_id,], daemon=True)
            self.assess_camera_threads[cam_id].start()
        
        # wait for all the threads to finish
        for key, thread in self.assess_camera_threads.items():
            thread.join()

        # due to threads, cam_ids not returned in order, so reorder       
        self.cams_to_use_list.sort(key=int) 
        
        for cap in self.caps_list:
            logger.debug(f"Releasing cap {cap}")
            cap.release()
            logger.debug(f"Deleting cap {cap}")
            del cap

        logger.debug(f"Deleting caps_list {self.caps_list}")
        del self.caps_list
        

        logger.info(f"Found cameras: {self.cams_to_use_list}")
        return FoundCameraCache(
            number_of_cameras_found=len(self.cams_to_use_list),
            cameras_found_list=self.cams_to_use_list,
            possible_resolutions=self.resolutions_dict
        )

    def assess_camera(self,cam_id):
        """A worker that can be spun up on it's own thread to sort out whether or not a given port connects to a legitimate camera"""
        cap = cv2.VideoCapture(cam_id)
        success, image1 = cap.read()
        time0 = time.perf_counter()

        if not success:
            return

        if image1 is None:
            return
        
        possible_resolutions = self.get_possible_resolutions(cap, cam_id)

        if len(possible_resolutions) == 1:
            logger.debug(
                f"Camera {cam_id} has only one possible resolution...likely virtual"
            )
        else: 
            logger.debug(
                f"Camera found at port number {cam_id}: success={success}, "
                f"image.shape={image1.shape},  cap={cap}"
            )
            
            self.cams_to_use_list.append(str(cam_id))
            self.caps_list.append(cap)
            self.resolutions_dict[cam_id] = possible_resolutions
        
    def get_nearest_resolution(self, video_capture, target_width):
        """
        returns the resolution nearest the target width for a given cv2.VideoCapture object
        """
        
        # 1. store the current resolution of the VideoCapture object to reset it later
        current_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        current_height =int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        # 2. attempt to set its width to the provided target_width
        video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, int(target_width))
        
        # 3. determine which resolution the VideoCapture object is actually able to attain
        nearest_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        nearest_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        # 4. reset the VideoCapture object to the original resolution
        video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, current_width)
        video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, current_height)

        logger.info(f"Resolution with a width nearest {target_width} is {(nearest_width,nearest_height)}")

        # 5. return the resolution as a tuple of (width, height)
        return (nearest_width, nearest_height) 

    def get_possible_resolutions(self, video_capture, cam_id):
        
        min_res = self.get_nearest_resolution(video_capture, MIN_RESOLUTION_CHECK)
        max_res = self.get_nearest_resolution(video_capture, MAX_RESOLUTION_CHECK)
        logger.info(f"Minimum resolution of camera at port {cam_id} is {min_res}")
        logger.info(f"Maximum resolution of camera at port {cam_id} is {max_res}")

        min_width = min_res[0]
        max_width = max_res[0]

        STEPS_TO_CHECK = 10  # fast to check so cover your bases

        # the size of jump to make before checking on the resolution
        step_size = int((max_width - min_width) / STEPS_TO_CHECK)

        resolutions = {min_res, max_res}

        if max_width > min_width:  # i.e. only one size avaialable
            for test_width in range(
                int(min_width + step_size), int(max_width - step_size), int(step_size)
            ):
                new_res = self.get_nearest_resolution(video_capture, test_width)
                # print(new_res)
                resolutions.add(new_res)
            resolutions = list(resolutions)
            resolutions.sort()
            possible_resolutions = resolutions
        else:
            possible_resolutions = [min_res]

        logger.info(f"At port {cam_id} the possible resolutions are {possible_resolutions}")
        
        return possible_resolutions

if __name__ == "__main__":
    detector = DetectPossibleCameras()
    start_time = time.perf_counter()
    camera_cache = detector.find_available_cameras()
    elapsed_time = time.perf_counter()-start_time
    
    print(f"Elapsed time for camera detection is {round(elapsed_time,2)} seconds")