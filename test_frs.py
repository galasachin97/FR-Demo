import requests
import json
import numpy as np

'''
#insert
headers = {'api_key' : '144278c3bcb2127eccca0ac1aaf799a84a6aa048'}
data={'name':'demo','unique_key':'2','license_key':'pSCXCJdJUgqOsav'}
res = requests.post(url= "http://127.0.0.1:6000/register/", headers = headers, data=data)
print(res.text)
'''

'''
#update
headers = {'api_key' : '144278c3bcb2127eccca0ac1aaf799a84a6aa048'}
data={'prev_name':'INTOZI','new_name':'INT','unique_key':'1'}
res = requests.put(url= "http://127.0.0.1:6000/register/", headers = headers, data=data)
print(res.text)
'''

'''
#delete
headers = {'api_key' : '144278c3bcb2127eccca0ac1aaf799a84a6aa048'}
data={'name':'INT1'}
res = requests.delete(url= "http://127.0.0.1:6000/register/", headers = headers, data=data)
print(res.text)
'''


#verification


#sachin
import os
file_path = "/home/diycam/Downloads/readme/demo"
for img_path in file_path:
    rollno = 1
    # Get the filename only from the initial file path.
    basename = os.path.basename(img_path)
    (filename, ext) = os.path.splitext(basename)
    files = {'file' : open(img_path,"rb")}
    headers = {'api_key' : '144278c3bcb2127eccca0ac1aaf799a84a6aa048'}
    data={'profile_name':filename,'profile_id':rollno,'client_unique_key':'1'}
    res = requests.post(url= "http://127.0.0.1:6000/verify/", headers = headers,files = files,data=data)
    r=json.loads(res.text)
    rollno = rollno + 1
    print(r)


'''
file_path = "/home/diycam/Downloads/readme/Sachin.jpeg"
files = {'file' : open(file_path,"rb")}
headers = {'api_key' : '144278c3bcb2127eccca0ac1aaf799a84a6aa048'}
data={'profile_name':'Sachin','profile_id':'2','client_unique_key':'1'}
res = requests.post(url= "http://127.0.0.1:6000/verify/", headers = headers,files = files,data=data)
r=json.loads(res.text)
print(r)
'''
'''
headers = {'api_key' : '144278c3bcb2127eccca0ac1aaf799a84a6aa048'}
data={'client_unique_key':'1', 'profile_id':'1'}
res = requests.delete(url= "http://127.0.0.1:6000/verify/", headers = headers, data=data)
print(res.text)
'''

#matching
#image
'''
file_path = "/home/diycam/Downloads/readme/index.jpeg"
#file_path = "/home/diycam/Downloads/readme/sachin123.png"
files = {'file' : open(file_path,"rb")}
headers = {'api_key' : '144278c3bcb2127eccca0ac1aaf799a84a6aa048'}
data={'client_unique_key':'1', 'threshold':'0.5'}
res = requests.post(url= "http://127.0.0.1:6000/match/", headers = headers,files = files,data=data)
print(res.text)
'''

#video
'''
import cv2

headers = {'api_key' : '144278c3bcb2127eccca0ac1aaf799a84a6aa048'}
data={'client_unique_key':'1', 'threshold':'0.5'}
# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("rtsp://admin:12ka442ka1%40%23@192.168.1.156:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif")
while cap.isOpened() :
    r,f = cap.read()
    cv2.imwrite("1.jpg",f)
    files = {'file' : open("1.jpg","rb")}
    res = requests.post(url= "http://127.0.0.1:6000/match/", headers = headers,files = files,data=data)
    print(res.text)
    cv2.imshow("", f)
    cv2.waitKey(1)
'''