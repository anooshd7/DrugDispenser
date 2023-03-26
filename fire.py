import pyrebase
from facial_recognition.facial_req import *

something = recog()

config={
    
  'apiKey': "AIzaSyAc3AkKkAphbmcIVyt9qh1G7TOCKcb2-RI",
  'authDomain': "drugdispenser-1bdd2.firebaseapp.com",
  'databaseURL': "https://drugdispenser-1bdd2-default-rtdb.firebaseio.com",
  'projectId': "drugdispenser-1bdd2",
  'storageBucket': "drugdispenser-1bdd2.appspot.com",
  'messagingSenderId': "717276153680",
  'appId': "1:717276153680:web:9920e01baa5a4167e5ce55"
}

firebase = pyrebase.initialize_app(config)
db=firebase.database()
data = (db.child("Form").get())
data1 = data.val()
current=[]
for i in data1:
    #print(i)
    parent=db.child("Form").child(i).child("name").get()
    current.append(i)
    if(parent.val()==something[0]):
        current.append(i)
        break
required=current[-1]


name=db.child("Form").child(required).child("name").get()
head = name.val()

print(head)

du_1 = db.child("Form").child(required).child("drug1").get()
dru_1 = du_1.val()
du_2 = db.child("Form").child(required).child("drug2").get()
dru_2 = du_2.val()

