from firebase import firebase

#todo 28  Select User
url = 'https://pops-2955e.firebaseio.com/user/'
firebase = firebase.FirebaseApplication(url)

#todo delete.
# firebase.delete('/user','8')

die = firebase.delete('Student_ID_1',None)
print('Complete : ',die)