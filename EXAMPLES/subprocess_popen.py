#!/usr/bin/env python

import sys
import subprocess as sp
from glob import glob

files = glob('DATA/*')  # <1>

print(sys.platform)

if sys.platform == 'win32':  # <2>
    CMD = ['cmd', '/c', 'dir', r'c:\Windows\system32\calc.exe']
    # change to clac.exe to see STDERR
else:
    CMD = ['ls', '-l', '/etc/passwd', '/etc/wildebeest']

stdout_filename, stderr_filename = 'proc_stdout.txt', 'proc_stderr.txt'

with open(stdout_filename, 'w') as stdout:
    with open(stderr_filename, 'w') as stderr:
        try:
            proc = sp.Popen(CMD, stdout=stdout, stderr=stderr)  # <3>
        except sp.CalledProcessError as err:  # <4>
            print("TRY 2: Process failed with return code", e.returncode)
            print("Error message is [[{}]]".format(err))
        else:
            print("No exceptions were raised.")

        #
        status_code = proc.wait()  # <5>

# <6>
with open(stdout_filename) as stdout:
    with open(stderr_filename) as stderr:
        stderr_text = stderr.read()  # <7>
        stdout_text = stdout.read()

print("STATUS:", status_code)
print("CAPTURED STDOUT:\n", stdout_text)
print("CAPTURED STDERR:\n", stderr_text)
