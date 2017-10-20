import subprocess
import sys

def getEnv(command):
    listEnv = subprocess.check_output(command).decode("utf-8").rsplit()
    return listEnv

os=sys.platform

if os=='linux':
    print('Congratulation you have a linux platform and your environment have', len(getEnv('printenv')), 'lines')
    print(getEnv('printenv'))
elif os=='win32' or os=='win64':
    print('Ahtung!!! BIG BROTHER you have a windows platform and your environment have', len(getEnv('c:\Windows\system32\cmd.exe /C set')), 'lines')
    print(getEnv('c:\Windows\system32\cmd.exe /C set'))
else:
    print('Your system unknown.')
