# This script defines a function to extract audio and write it to a file from a given video file

"""Depedencies - pip install moviepy
                 pip install ffmpeg              
"""

import os
import sys
from moviepy.editor import VideoFileClip

def convert_video_to_audio_moviepy(video_file, output_ext="mp3"):
    filename, ext = os.path.splitext(video_file)
    clip = VideoFileClip(video_file)
    clip.audio.write_audiofile(f"{filename}.{output_ext}")

# Test
# if __name__ == "__main__":
#     VIDEO_FILE = './cropped_sample_level1_2.mp4'
#     convert_video_to_audio_moviepy(VIDEO_FILE)