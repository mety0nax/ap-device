import os
import sys
import pathlib
import datetime
import subprocess

def getCurrentDatetime( ):
  tm_now = datetime.datetime.now( )
  dt_str = f'{tm_now.day:02}/{tm_now.month:02}/{tm_now.year}'
  tm_str = f'{tm_now.hour:02}:{tm_now.minute:02}:{tm_now.second:02}'
  return f'{dt_str} {tm_str}'

def listOpenedFiles(dirName) :
  output = subprocess.run(
    f'lsof -X | grep {dirName.absolute( )}',
    shell = True,
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE
  ).stdout.decode( ).replace('\n', ' ')
  return [x for x in output.split(' ') if x and str(dirName) in x]

if len(sys.argv) <= 1:
  print(f'[{getCurrentDatetime( )}] ERROR: Target directory is not specified')
  exit(1)

targetDir = pathlib.Path(sys.argv[1])
if not targetDir.exists( ):
  print(f'[{getCurrentDatetime( )}] ERROR: Target directory does not exist')
  exit(1)

excludeList = listOpenedFiles(targetDir)
with open('/tmp/excludeList.txt', 'w') as excludeListFile:
  for file in excludeList:
    excludeListFile.write(os.path.basename(file))
    excludeListFile.write('\n')