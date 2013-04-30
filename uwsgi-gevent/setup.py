
import subprocess
import sys
import setup_util
import os

def start(args):
  subprocess.Popen("uwsgi -L -s /tmp/uwsgi.sock -w hello:app --http :8080 --master --gevent " + str((args.max_threads * 2)) + " ", shell=True, cwd="uwsgi-gevent")
  return 0
def stop():
  p = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE)
  out, err = p.communicate()
  for line in out.splitlines():
    if 'wsgi.sock' in line:
      try:
        pid = int(line.split(None, 2)[1])
        os.kill(pid, 9)
      except OSError:
        pass

  return 0