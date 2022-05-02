"""Module to stop ffplay, ffmpeg's player, by stopping its process."""
import psutil
import subprocess


def stop():
    """I'll use subprocess to, first find out the pid, and then to stoppping it with psutil"""
    processes = subprocess.Popen(["ps ax | grep 'ffplay'"],
                                 shell=True, stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT)
    # 'ps ax | grep 'python3 playsound_player.py' looks for the pid of the command.
    # https://askubuntu.com/questions/180336/how-to-find-the-process-id-pid-of-a-running-terminal-program
    # 'stdout=subprocess.PIPE' pipes the standar output and keeps it.
    # 'stderr=subprocess.STDOUT', sends the errors to the screen
    # https://cmdlinetips.com/2014/03/how-to-run-a-shell-command-from-python-and-get-the-output/

    stdout, stderr = processes.communicate()   # This allows us to see the outputs of the command
    print(stdout)
    pid = stdout.split()[0]                    # It collects just the pid.
    pid_str = pid.decode('utf-8')              # Decodes the Popen byte object into a string.
    print(pid_str)

    p = psutil.Process(int(pid_str))           # psutil is a library the deals with process management
    p.suspend()                                # https://github.com/giampaolo/psutil


stop()


"""
NOTES
All notes on resume.py apply.
"""
