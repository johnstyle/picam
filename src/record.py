#!/usr/bin/env python

import subprocess
import datetime
import os

ROOT_PATH = "/var/www/html"
SEGMENT_TIME = 30

recording_path = os.path.join(ROOT_PATH, datetime.datetime.now().strftime("%Y%m%d"))
os.mkdir(recording_path)

segments_path = os.path.join(recording_path, "{}_%03d.avi".format(datetime.datetime.now().strftime("%H%M%S")))

command = "ffmpeg -i /dev/video0 -r 30 -c:v copy -an -sn -dn -vf drawtext=\"fontfile=Arial.ttf:fontcolor=white: timecode='00\:00\:00;00': r='30000/1001': text='': fontsize=148: x=190: y=260:\" -segment_time {} -f segment {}".format(SEGMENT_TIME, segments_path)

subprocess.call(command, shell=True)
