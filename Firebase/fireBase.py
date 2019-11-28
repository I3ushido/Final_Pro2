from firebase import firebase
# # WEB
# <!-- The core Firebase JS SDK is always required and must be listed first -->
# <script src="/__/firebase/6.3.3/firebase-app.js"></script>
#
# <!-- TODO: Add SDKs for Firebase products that you want to use
#      https://firebase.google.com/docs/web/setup#reserved-urls -->
#
# <!-- Initialize Firebase -->
# <script src="/__/firebase/init.js"></script>
# #

# ##################### WEB API
# <!-- The core Firebase JS SDK is always required and must be listed first -->
# <script src="https://www.gstatic.com/firebasejs/6.3.3/firebase-app.js"></script>
#
# <!-- TODO: Add SDKs for Firebase products that you want to use
#      https://firebase.google.com/docs/web/setup#config-web-app -->
#
# <script>
#   // Your web app's Firebase configuration
#   var firebaseConfig = {
#     apiKey: "AIzaSyCKLFr35Akc-ZQJwriYEU89YScgJ-gaEBs",
#     authDomain: "pops-2955e.firebaseapp.com",
#     databaseURL: "https://pops-2955e.firebaseio.com",
#     projectId: "pops-2955e",
#     storageBucket: "pops-2955e.appspot.com",
#     messagingSenderId: "131428012607",
#     appId: "1:131428012607:web:56e0174f23b531d1"
#   };
#   // Initialize Firebase
#   firebase.initializeApp(firebaseConfig);
# </script>
# #####################
#todo 27 july
url = 'https://pops-2955e.firebaseio.com/'
firebase = firebase.FirebaseApplication(url)

student1= {'student_id': 1,'name': 'Arts ', 'stasus': 'Success_'}
student2 = {'student_id': 2,'name': 'Bank ', 'stasus': 'Sucess_'}
student3 = {'student_id': 3,'name': 'Liu ', 'stasus': 'Success_'}
student4 = {'student_id': 4,'name': 'Green ', 'stasus': 'Success_'}

result = firebase.put('/user','Student_ID_1',student1)
result2 = firebase.put('/user','Student_ID_2',student2)
result3 = firebase.put('/user','Student_ID_3',student3)
result4 = firebase.put('/user','Student_ID_4',student4)

print("Success ", result), print("Success ", result2), print("Success ", result3) ,print("Success ", result4)


