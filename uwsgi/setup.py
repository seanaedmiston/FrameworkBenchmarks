
import subprocess
import sys
import setup_util
import os
from os.path import expanduser

home = expanduser("~")

def start(args):
  subprocess.Popen("uwsgi  -s /tmp/uwsgi.sock --wsgi-file hello.py --callable app --chmod-socket=666 ", shell=True, cwd="uwsgi")
  subprocess.check_call("sudo /usr/local/nginx/sbin/nginx -c " + home + "/FrameworkBenchmarks/uwsgi/config/nginx.conf", shell=True)

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
