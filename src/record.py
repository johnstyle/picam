#!/usr/bin/env python

import subprocess
import datetime
import os

ROOT_PATH = "/var/www/html"
SEGMENT_TIME = 10

recording_path = os.path.join(ROOT_PATH, datetime.datetime.now().strftime("%Y%m%d"))
os.mkdir(recording_path)

segments_path = os.path.join(recording_path, "{}_%03d.avi".format(datetime.datetime.now().strftime("%H%M%S")))

command = "ffmpeg -i /dev/video0 -r 30 -framerate 30 -video_size 1280x720 -c:v ffv1 -an -sn -dn -vf drawtext=\"fontfile=Arial.ttf:fontcolor=white: timecode='00\:00\:00;00': r='30000/1001': text='': fontsize=14: x=1000: y=710:\" -segment_time {} -f segment {}".format(SEGMENT_TIME, segments_path)

subprocess.call(command, shell=True)
