# Raspberry Pi Dashcam

1. Run Makefile
2. Add into `/etc/rc.local` before `exit 0`

    python /home/pi/purge_old_recordings.py
    python /home/pi/record.py &

