import subprocess
import sys

def getNumberEnv(command):
    listEnv = subprocess.check_output(command).decode("utf-8").splitlines()
    return len(listEnv)

os=sys.platform
#print(sys.platform)

if os=='linux':
    print('Congratulation you have linux platform and you environment have ', getNumberEnv('printenv'), ' lines')

if os=='windows':
    print('Ahtung!!! BIG BROTHER you have windows platform and you environment have ', getNumberEnv('printenv'), ' lines')
