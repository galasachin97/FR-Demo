from cgi import test
from urllib import response
from cv2 import bilateralFilter
import requests
import json
import numpy as np
import cv2

# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

#insert
@app.post("/insert")
async def insert():
    headers = {'api_key' : '144278c3bcb2127eccca0ac1aaf799a84a6aa048'}
    data={'name':'demo123','unique_key':'24','license_key':'pSCXCJdJUgqOsav'}
    res = requests.post(url= "http://127.0.0.1:6000/register/", headers = headers, data=data)
    print(res.text)
    return {res.text}
    


#update
@app.put("/update")
async def update():
    headers = {'api_key' : '144278c3bcb2127eccca0ac1aaf799a84a6aa048'}
    data={'prev_name':'demo','new_name':'demonew','unique_key':'2'}
    res = requests.put(url= "http://127.0.0.1:6000/register/", headers = headers, data=data)
    print(res.text)
    return {res.text}


#delete
@app.post("/delete")
async def delete():
    headers = {'api_key' : '144278c3bcb2127eccca0ac1aaf799a84a6aa048'}
    data={'name':'INT1'}
    res = requests.delete(url= "http://127.0.0.1:6000/register/", headers = headers, data=data)
    print(res.text)
    return{res.text}


#verification

'''
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

@app.post("/person_add")
async def person_add():
    file_path = "/home/diycam/Downloads/readme/Sachin.jpeg"
    files = {'file' : open(file_path,"rb")}
    headers = {'api_key' : '144278c3bcb2127eccca0ac1aaf799a84a6aa048'}
    data={'profile_name':'Sachin','profile_id':'2','client_unique_key':'1'}
    res = requests.post(url= "http://127.0.0.1:6000/verify/", headers = headers,files = files,data=data)
    r=json.loads(res.text)
    print(r)
    return{r}

@app.post("/person_add1")
async def person_add1():
    # file_path = "/home/diycam/Downloads/readme2/demo/Khusi chawla.jpeg"
    file_path = "/home/diycam/Downloads/readme2/demo/Khusi chawla.jpeg"
    files = {'file' : open(file_path,"rb")}
    headers = {'api_key' : '144278c3bcb2127eccca0ac1aaf799a84a6aa048'}
    data={'profile_name':'Kushi chawla','prof1ile_id':'1','client_unique_key':'1'}
    res = requests.post(url= "http://127.0.10.1:6000/verify/", headers = headers,files = files,data=data)
    r1 = json.loads(res.text)    
    file_path = "/home/diycam/Downloads/readme2/demo/Megha kathumariya.jpeg"
    files = {'file' : open(file_path,"rb")}
    headers = {'api_key' : '144278c3bcb2127eccca0ac1aaf799a84a6aa048'}
    data={'profile_name':'Megha kathumariya','profile_id':'2','client_unique_key':'1'}
    res = requests.post(url= "http://127.0.10.1:6000/verify/", headers = headers,files = files,data=data)    
    r2 = json.loads(res.text)
    file_path = "/home/diycam/Downloads/readme2/demo/Rahul Sain.jpeg"
    files = {'file' : open(file_path,"rb")}
    headers = {'api_key' : '144278c3bcb2127eccca0ac1aaf799a84a6aa048'}
    data={'profile_name':'Rahul Sain','profil1e_id':'3','client_unique_key':'1'}
    res = requests.post(url= "http://127.0.10.1:6000/verify/", headers = headers,files = files,data=data)
    r3 = json.loads(res.text)
    file_path = "/home/diycam/Downloads/readme2/demo/Rohini Chawla.jpeg"
    files = {'file' : open(file_path,"rb")}
    headers = {'api_key' : '144278c3bcb2127eccca0ac1aaf799a84a6aa048'}
    data={'profile_name':'Rohini Chawla','pro1file_id':'4','client_unique_key':'1'}
    res = requests.post(url= "http://127.0.10.1:6000/verify/", headers = headers,files = files,data=data)
    r4 = json.loads(res.text)
    file_path = "/home/diycam/Downloads/readme2/demo/Shaurabh Sain.jpeg"
    files = {'file' : open(file_path,"rb")}
    headers = {'api_key' : '144278c3bcb2127eccca0ac1aaf799a84a6aa048'}
    data={'profile_name':'Shaurabh Sain','profile_id':'5','client_unique_key':'1'}
    res = requests.post(url= "http://127.0.0.1:6000/verify/", headers = headers,files = files,data=data)
    r5 = json.loads(res.text)
    print(r1,r2,r3,r4,r5)
    r=[r1,r2,r3,r4,r5]
    return{str(r)}

@app.post("/person_delete")
async def person_delete():
    headers = {'api_key' : '144278c3bcb2127eccca0ac1aaf799a84a6aa048'}
    data={'client_unique_key':'1', 'profile_id':'1'}
    res = requests.delete(url= "http://127.0.0.1:6000/verify/", headers = headers, data=data)
    print(res.text)
    return{res.text}

#matching
#image
@app.post("/matching_image1")
async def matching_image1():
    file_path = "/home/diycam/Downloads/readme/index.jpeg"
    #file_path = "/home/diycam/Downloads/readme/sachin123.png"
    files = {'file' : open(file_path,"rb")}
    headers = {'api_key' : '144278c3bcb2127eccca0ac1aaf799a84a6aa048'}
    data={'client_unique_key':'1', 'threshold':'0.5'}
    res = requests.post(url= "http://127.0.0.1:6000/match/", headers = headers,files = files,data=data)
    print(res.text)
    return{res.text}

@app.post("/matching_image2")
async def matching_image2():
    # file_path = "/home/diycam/Downloads/readme/index.jpeg"
    file_path = "/home/diycam/Downloads/readme/sachin123.png"
    files = {'file' : open(file_path,"rb")}
    headers = {'api_key' : '144278c3bcb2127eccca0ac1aaf799a84a6aa048'}
    data={'client_unique_key':'1', 'threshold':'0.5'}
    res = requests.post(url= "http://127.0.0.1:6000/match/", headers = headers,files = files,data=data)
    print(res.text)
    return{res.text}

#video
@app.post("/matching_video")
async def matching_video():
    headers = {'api_key' : '144278c3bcb2127eccca0ac1aaf799a84a6aa048'}
    data={'client_unique_key':'1', 'threshold':'0.5'}
    # cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture("rtsp://admin:12ka442ka1%40%23@192.168.1.156:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif")
    count = 0
    test=[]
    while cap.isOpened() :
        if count<=5000:
            r,f = cap.read()
            cv2.imwrite("1.jpg",f)
            files = {'file' : open("1.jpg","rb")}
            res = requests.post(url= "http://127.0.0.1:6000/match/", headers = headers,files = files,data=data)
            print(res.text)
            count = count + 1
            # cv2.imshow("", f)
            cv2.waitKey(1)
            test.append(str(res.text))
        else:
            break
        print(test)
    return{str(test)}