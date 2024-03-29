import random
import smtplib
import face_recognition as fr # To recognize faces
import numpy as np # To handle all lists/arrays
import cv2 # To capture webcam footage
import os # To handle all matters relating to folders, paths, image/file names, etc.
# Path to folder containing all known faces. The 'known' folder needs all known faces,
# where the image\file name is the name of the person to be recognized.
faces_path = "C:\Users\artam\PycharmProjects\face_reco\face"
n = ""
em = ''
# Function to get face names, as well as face encodings
def get_face_encodings():
    face_names = os.listdir(faces_path)
    face_encodings = []
    # For loop to retrieve all face encodings and store them in a list.
    # Below loop also gets the names of people and removes ".jpg", and stores
    # the names in a list
    for i, name in enumerate(face_names):
        face = fr.load_image_file(f"{faces_path}\\{name}")
        face_encodings.append(fr.face_encodings(face)[0])
        face_names[i] = name.split(".")[0] # To remove ".jpg" or any other image extension
    return face_encodings, face_names
# Retrieving face encodings and storing them in the face_encodings variable, along with the names
face_encodings, face_names = get_face_encodings()
# Reference to webcam
video = cv2.VideoCapture(0)
#video.set(cv2.CAP_PROP_FPS, 420)
# Setting variable which will be used to scale size of image
scl = 2
# Continuously capturing webcam footage
while True:
    success, image = video.read()
    # Making current frame smaller so program runs faster
    resized_image = cv2.resize(image, (int(image.shape[1] / scl), int(image.shape[0] / scl)))
    # Converting current frame to RGB, since that's what the face recognition module uses
    rgb_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)
    # Retrieving face location coordinates and unknown encodings
    face_locations = fr.face_locations(rgb_image)
    unknown_encodings = fr.face_encodings(rgb_image, face_locations)
    # Iterating through each encoding, as well as the face's location
    for face_encoding, face_location in zip(unknown_encodings, face_locations):
    # Comparing known faces with unknown faces
        result = fr.compare_faces(face_encodings, face_encoding, 0.4)
        # Getting correct name if a match was found
    if True in result:
        name = face_names[result.index(True)]
        # Setting coordinates for face location
        top, right, bottom, left = face_location
        # Drawing rectangle around face
        cv2.rectangle(image, (left * scl, top * scl), (right * scl, bottom * scl), (0, 0, 
        255), 2)
        # Setting font, as well as displaying text of name
        font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(image, name, (left * scl, bottom * scl + 20), font, 0.8, (255, 255, 
255), 1)
    n = name
    print(n)

    cv2.imshow("frame", image)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("rahulmydur341@gmail.com", 'setvmwylpfgkjown')
    otp = ''.join([str(random.randint(0, 9)) for i in range(6)])
    msg = 'Hello, Your OTP is ' + str(otp)

    if n == 'Rahul':
        em = 'rahulmydur@gmail.com'
        server.sendmail('rahulmydur341@gmail.com', em, msg)
        server.quit()
        break
        print("Hello rahul")
    elif n == "pawan":
        em = '7pawancena@gmail.com'
        server.sendmail('rahulmydur341@gmail.com', em, msg)
        server.quit()
        break
        print("Hello pawan")
    elif n == "manoj":
        em = 'manojmanugmail.com'
        server.sendmail(''rahulmydur341@gmail.com', em, msg)
        server.quit()
        break
        print("Hello manoj")
    if cv2.waitKey(25) & 0xFF == ord(' '):
    break
otp_m = int(otp)
correct_otp = int(input("Enter the OTP : "))
if correct_otp == otp_m:
 print("Access granted")
else:
 print("Incorrect OTP ")

