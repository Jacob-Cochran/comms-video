from picamera2 import Picamera2
import time

# Initialize the camera
picam2 = Picamera2()

# Start the camera
picam2.start()

# Setup the video encoder (specifically for H.264)
# Picamera2 allows you to specify the output format and configure the encoder
picam2.video_configuration = {
    # "encode": "H264",  # Set to hardware-encoded H.264
    # "bitrate": 2000000,  # Bitrate for the video stream (optional, tweak as necessary)
    # "framerate": 30,  # Set frame rate
    # "width": 1920,  # Width of the video
    # "height": 1080  # Height of the video
}

# Start recording
picam2.start_recording("output.h264")  # The file will be written with H.264 encoded video

# Record for a short period, then stop
time.sleep(10)
picam2.stop_recording()
