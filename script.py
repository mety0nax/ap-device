import sys
import time
import random
import datetime

def main( ):
  if len(sys.argv) <= 1:
    print('[*] ERROR: Output directory is not specified')
    return

  targetDir = pathlib.Path(sys.argv[1])
  if not targetDir.exists( ):
    print('[*] ERROR: Output directory does not exist')
    return

  dirs = os.listdir(targetDir)
  for d in dirs:
    if 'data_' in d:
      dirName = targetDir.joinpath(d)
      break

  timer = random.randrange(60)
  time = datetime.datetime.now( ).strftime('%d-%m-%Y___%H-%M-%S')
  f_desc = open(f'{dirName.joinpath(f"{time}.txt")}', 'w')
  
  for i in range(timer):
    f_desc.write(f'{i}: Just a random text ...\n')
    time.sleep(1)

  f_desc.close( )

if __name__ == '__main__':
  main( )
  print('[*] Done with no errors')
else:
  print('This module is supposed to be run as __main__')