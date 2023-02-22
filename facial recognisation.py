Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import cgi
... from base64 import b64decode
... import face_recognition
... formData=cgi.filedstorage()
... face_match=0
... image=formData.getvalue("current_image")
... email=formData.getvalue("email")
... data_uri =image
... header,encoded=data_uri.split(",",1)
... data=b64decode(encoded)
... with open("image.png","wb") as f:
...     f.write(data)
... got_image=face_recognition.load_image_file("image.png")
... existing_image=face_recognition.load_image_file("student/"+email+".jpg")
... got_image_facialfeatures=face_recognition.face_encoding(got_image)[0]
... existing_image_facialfeatures=face_recognition.face_encoding(existing_image)[0]
... 
... 
... results=
... face_recognition.compare_faces([existing_image_facialfeatures],got_image_facialfeatures)
... 
... if(results[0]):
...     face_match=1
... else:
...     face_match=0
...     
... print("context-type: text/html")
... print()
... 
... if(face_match==1):
...     print("<script>alert('welcome",email,"')</script>")
... else:
...     print("<script>alert('face not recognised')</script>")
