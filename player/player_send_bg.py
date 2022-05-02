import os
from time import sleep
import signal
import subprocess


def send_bg():

    processes = subprocess.Popen(["ps ax | grep 'main.py'"],
                                  shell=True, stdout=subprocess.PIPE,
                                  stderr=subprocess.STDOUT)
    stdout, stderr = processes.communicate()
    print(stdout)
    pid = stdout.split()[0]
    pid_str = pid.decode('utf-8')
    print(pid_str)
    os.kill(int(pid_str), signal.SIGSTOP)
    sleep(2)
    subprocess.call(["bg 'python3 main.py'"], shell=True)


if __name__ == '__main__':
    send_bg()
