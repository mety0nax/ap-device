import os
import sys
import time
import random
import pathlib
import datetime

def main( ):
  if len(sys.argv) <= 1:
    print('[*] ERROR: Output directory is not specified')
    return

  targetDir = pathlib.Path(sys.argv[1])
  if not targetDir.exists( ):
    print('[*] ERROR: Output directory does not exist')
    return

  dirName = ''
  dirs = os.listdir(targetDir)
  print(dirs)
  for d in dirs:
    if 'data_' in d:
      dirName = targetDir.joinpath(d)
      break

  timer = random.randrange(120)
  ctime = datetime.datetime.now( ).strftime('%d-%m-%Y___%H-%M-%S')
  print(dirName)
  new_file = dirName.joinpath(f'{ctime}.txt')
  f_desc = open(new_file, 'w')
  
  for i in range(timer):
    f_desc.write(f'{i}: Just a random text ...\n')
    time.sleep(1)

  f_desc.close( )

if __name__ == '__main__':
  main( )
  print('[*] Success')
else:
  print('This module is supposed to be run as __main__')