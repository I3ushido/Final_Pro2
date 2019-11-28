from firebase import firebase

#todo 28  Select User
url = 'https://pops-2955e.firebaseio.com/user/'
firebase = firebase.FirebaseApplication(url)

data = firebase.get('Student_ID_3',None)
# data = firebase.get('user','Student_ID_1','name')

print('dataType',type(data))
print('All_Data : ',data)
print('Data_Name : ',data['name'])
