# Secure Virtual Key Entry System

## Overview

This repository contains a Python program that implements a Secure Virtual Key Entry System using Two-Factor Authentication (2FA). The system utilizes Facial Recognition and One-Time Passcode (OTP) Verification to enhance the security of virtual key entry.

## Features

- **Two-Factor Authentication (2FA):** The system incorporates 2FA for enhanced security, requiring users to provide two different authentication factors.
  - **Facial Recognition:** Utilizes facial recognition technology to identify or confirm an individual's identity using their face.
  - **OTP Verification:** Implements OTP verification by sending a one-time passcode to the user's registered email during login.

## Dependencies

- Python
- face_recognition library
- NumPy
- OpenCV
- smtplib (for email functionality)

## Usage

1. Clone the repository to your local machine.

   ```bash
   git clone https://github.com/RAHULMYDUR/Secure-Virtual-Key-Entry-Python-project
   ```

2. Run the program.

   ```bash
   python Secure_Virtual_Key_Source_code.py
   ```

3. Follow the on-screen instructions to use the Secure Virtual Key Entry System.

## Program Flow

1. The program continuously captures webcam footage and performs facial recognition on the faces detected.

2. If a known face is recognized, an OTP is generated and sent to the registered email address associated with the recognized face.

3. The user is prompted to enter the received OTP.

4. If the entered OTP matches the generated OTP, access is granted. Otherwise, access is denied.

## Configuration

- Update the `faces_path` variable in the code to the path containing images of known faces.

## Results

- The program displays the webcam footage with rectangles around recognized faces and their corresponding names.
  
- Email notifications with OTPs are sent to the registered email addresses.

## Note

- Ensure that your system has a webcam for facial recognition.

- The email functionality is currently configured for a Gmail SMTP server. Update the email server details and credentials in the code for your email provider.

## Contributors

- Rahul Mydur (https://github.com/RAHULMYDUR)

