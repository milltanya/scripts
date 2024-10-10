from datetime import datetime, timedelta
import os
from subprocess import call
import sys

start_dttm = datetime.fromisoformat(sys.argv[1])
print(start_dttm)

for i, filename in enumerate(sorted(os.listdir())):
    offset = timedelta(seconds=i)
    creation_dttm = (start_dttm+offset).strftime("%m/%d/%Y %H:%M:%S")
    command = f'SetFile -d "{creation_dttm}" -m "{creation_dttm}" "{filename}"'
    print(i, filename, creation_dttm, command)

    call(command, shell=True)
