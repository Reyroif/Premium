import platform, os

def __main__():
  try:
    if os.path.exists("Data/apikey.txt") == False:
      __import__('Instagram').__apikey__()
    else:
      __import__('Instagram').__menu__()
  except Exception as e:
    exit(f"\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;91m {e}")
if __name__=='__main__':
  if '64bit' in str(platform.architecture()):
    __main__()
  else:
    exit("\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;91m Gunakan Perangkat 64bit")
