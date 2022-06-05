import subprocess
from urllib import request
#checking internet connection

def internet(ping="https://google.com"):
    try:
        request.urlopen(ping)
        return True
    except:
        print("No Internet Connection")
        return False
    
def pipwin():
    p=subprocess.run('pipwin install pyaudio', True)
    if ( p.returncode==1 and internet() == False):
        print("No internet Access")
    elif (p.returncode ==0):
        print("pyaudio is installed")
    elif(p.returncode==1 and internet() ==True):
        print("check the module name")
    else:
        print("Module not found Error")
        
        
    
        
    
    
