#!/usr/bin/env python
from subprocess import run, PIPE, CalledProcessError
import shlex
from glob import glob

cmd = 'netstat -an'



# run(cmd, shell=True)

cmd_words = shlex.split(cmd)

run(cmd_words)


unix_cmd = 'ls -l'
unix_args = 'DATA/*.txt'

cmd_words = shlex.split(unix_cmd)
cmd_args = glob(unix_args)
run(cmd_words + cmd_args)

print('-' * 60)


cmd_words = shlex.split(cmd)

try:
    proc = run(cmd_words, stdout=PIPE)
    for raw_line in proc.stdout.splitlines():
        line = raw_line.decode()
        if "ESTAB" in line:
            print(line)
except CalledProcessError as err:
    print(err)
    print(err.returncode)


