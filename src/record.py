#!/usr/bin/env python

import subprocess
import datetime
import os

ROOT_PATH = "/var/www/html"
SEGMENT_TIME = 60
ENCODING = "copy"

recording_path = os.path.join(ROOT_PATH, datetime.datetime.now().strftime("%Y%m%d"))
os.mkdir(recording_path)

segments_path = os.path.join(recording_path, "{}_%03d.avi".format(datetime.datetime.now().strftime("%H%M%S")))

command = "ffmpeg -i /dev/video0 -c:v {} -an -sn -dn -segment_time {} -f segment {}".format(ENCODING, SEGMENT_TIME, segments_path)

subprocess.call(command, shell=True)
