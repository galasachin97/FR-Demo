DOCKER SDK RUN
--------------

License:
pSCXCJdJUgqOsav
EVvYfuMosEFWvng


1. Install Docker
2. Pull the image :
	-> 
    docker pull vishalintozi/intozifacesdk:2.0
3. Run docker :
	-> docker run --rm  -d --network=host -v intozifacesdk:/app -e LICENSE_KEY=EVvYfuMosEFWvng vishalintozi/intozifacesdk:2.0

NOTE :
	TO uninstall license key 
		-> 
sudo docker run --rm -d --network=host -v intozifacesdk:/app -e LICENSE_KEY=EVvYfuMosEFWvng -e UNINSTALL=1 vishalintozi/intozifacesdk:2.0
		-> 
sudo docker volume rm intozifacesdk





APIs and Description
--------------------
Base Url    : http://127.0.0.1:6000
Api Key      : 144278c3bcb2127eccca0ac1aaf799a84a6aa048

1. /register/   : Used to register, update or delete client.

2. /verify/     : Used to register and delete people.

3. /match/      : Used to get matching score and people data of registered/unregistered people.


USAGE
-----

1. /register/ :
   ----------
                a. To register a client :
                    headers = {'api_key' : '144278c3bcb2127eccca0ac1aaf799a84a6aa048'}
                    data={'name':'INT','unique_key':'1','license_key':'qwerty'}
                    res = requests.post(url= "http://127.0.0.1:6000/register/", headers = headers, data=data)
                    

                b. To update a client :
                    headers = {'api_key' : '144278c3bcb2127eccca0ac1aaf799a84a6aa048'}
                    data={'prev_name':'INT','new_name':'INT1','unique_key':'1'}
                    res = requests.put(url= "http://127.0.0.1:6000/register/", headers = headers, data=data)

                c. To delete a client :
                    headers = {'api_key' : '144278c3bcb2127eccca0ac1aaf799a84a6aa048'}
                    data={'name':'INT1'}
                    res = requests.delete(url= "http://127.0.0.1:6000/register/", headers = headers, data=data)



2. /verify/ :
                a. To register a person :
                    file_path = "cc2d68e18be04acf90a74623c1087fd6.jpg"
                    files = {'file' : open(file_path,"rb")}
                    headers = {'api_key' : '144278c3bcb2127eccca0ac1aaf799a84a6aa048'}
                    data={'profile_name':'ROB','profile_id':'RBT','client_unique_key':'1'}
                    res = requests.post(url= "http://127.0.0.1:6000/verify/", headers = headers,files = files,data=data) 

                b. To delete a person :
                    headers = {'api_key' : '144278c3bcb2127eccca0ac1aaf799a84a6aa048'}
                    data={'client_unique_key':'1', 'profile_id':'RBT'}
                    res = requests.delete(url= "http://127.0.0.1:6000/verify/", headers = headers, data=data)


3. /match/ :
                a. To get the matching faces and matched person data :
                    a.1 For single image :
                            file_path = "/home/intozi/Downloads/Rob-cc2d68e18be04acf90a74623c1087fd6.jpg"
                            files = {'file' : open(file_path,"rb")}
                            headers = {'api_key' : '144278c3bcb2127eccca0ac1aaf799a84a6aa048'}
                            data={'client_unique_key':'2', 'threshold':'0.7'}
                            res = requests.post(url= "http://127.0.0.1:6000/match/", headers = headers,files = files,data=data)

                    a.2 For a video :
                            
                    
