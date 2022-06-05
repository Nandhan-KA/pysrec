# MIT License

# Copyright (c) 2022 NandhanK (developer.nandhank@gmail.com)

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import pkg_installer
import pyttsx3
import speech_recognition as sr
import urllib
#
        
def internet(ping="https://google.com"):
    try:
        urllib.request.urlopen(ping)
        return True
    except:
        return False
    
def speak(text):
    if (internet==True):
        engine=pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    else:
        print("Internet connection required!!!")
    
def get_audio():
    
    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("Say Something:)")
        audio=r.listen(source)

    data=''
    try:
        data = r.recognize_google(audio)
        print("You said:"+data)
        with open('datas.txt','wb') as f:
            f.write(data)
    except sr.UnknownValueError:
        print("Unknown error")
    except sr.RequestError as e:
        print("Service error"+e)

    return data
get_audio()
        