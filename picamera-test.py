from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder
from picamera2.outputs import FileOutput
import time

#### This will snap a simple recording which can be opened in VLC or similar ####

picam2 = Picamera2()
encoder = H264Encoder(bitrate=5_000_000)  # hardware accelerated
output = FileOutput("output.h264")

picam2.start_recording(encoder, output) 
# Can also use convenience method start_and_capture_recording() which infers based on filenames
time.sleep(10)
picam2.stop_recording()