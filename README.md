# project-pill-io
project-pill-io created by GitHub Classroom
# Contributers
-  Abin Cheriyan 
-  Anna Minasyan 
-  Ethan Lewis
-  Misha Golikov 
-  Tandi Huran

# Project Abstract
This project proposes a machine learning empowered pill dispenser that will allow both caregivers and patients to have peace of mind as they partake in what for most of them is a daily requirement for their health and safety. This pill dispensing software will allow for medications to always be dispensed with only the needed medications and dosages based on the facial recognition of the patient attempting to get their medication. This will allow patients to get their medication without the struggle of opening or sorting through pill bottles and help prevent the possibility of an overdose on medications by no longer having patients access of all their medicine supply at the same time. Moreover, caregivers will be able to access data regarding the frequency and timing of when/if their patients take their medications which will help inform their care. 


# PythonAnywhereHosting
https://pillio.pythonanywhere.com/

# Release v1.0.0 (FIRST MILESTONE DEMO)

## Release Notes
This is our first release, so there is no previous release to compare to. This release contains preliminary:
- Sign-Up/Registration functionality with crosschecking against existing accounts to prevent duplicate users, with password hashing and the ability to upload a user picture, where in the future, it is to be used as a profile picture and for crosschecking facial recognition.
- Login functionality with countermeasures to prevent against incorrectly formatted emails (such as no @ symbol), as well as the hashing of user passwords using the SHA256 encryption algorithm.
- Medication Management System where a user is able to select an arbitrary pill and select the time they wish to take it at (not yet connected to the database).
- Authentication Success/Failure/Loading Screens, where a user is able to stream their webcam on the website and take a photo of themselves, where it will be used for facial recognition in the future.
- NOT INCLUDED IN REPO: Facial Recognition algorithm and functionality on the Jetson Nano that allows a user to authenticate themselves by scanning their face in the camera, after which they are told how many times they've visited that camera in the past.


## How to Use and Test
Instructions on how to use and test the release (contains instructions similar to the Test Procedures document).

## UAT (User Acceptance Testing)

!! MILESTONE DEMO 1 !!

Test 1:
  Creating an Account:
    
    Actions/Steps:
      - Click Sign Up on the navbar
      - Enter Username (it has to be an email)
      - Enter your first name 
      - Enter your last name
      - Enter your preferred Password 
      - Enter your Date of Birth
      - Enter a picture of your face (it will later be used as your Profile Picture and for facial recognition)
      - Press the Sign Up Button at the bottom of the form
    
    Expected Results:
      - The user is able to Sign up without any problem and the system will save the user's details onto the db. 
      - User will see an "Account created" confirmation popup

Test 2:
  Logging into an Account:
    
    Actions/Steps:
      - Click Login on the navbar
      - Enter your email in the field marked "Your Email"
      - Enter your password in the field marked "Your Password", the password is case sensitive as usual
      - Check the checkbox marked "Remember me" if you wish for the website/browser to save your cookies and leave you logged into account when you visit the website again
      - Press the Login Button at the bottom of the form
    
    Expected Results:
      - The user is able to login into their already existing account with no problems, where
      - The user will see the "Medication Form" page in front of them, which is marked by the "/profile" page identifier in the URL
      - If the user checked the "Remember me" checkbox, they are able to close the website, reopen it, and still be logged in.
      - If the user did not check the "Remember me" checkbox, they will be required to login again when they close and reopen the website.
     
Test 3:
  Accessing help/faq page:
    
    Actions/Steps:
      - Click on Login on the navbar
      - Enter your credentials
      - Click on Login button
      - Once logged in, Help page should be available to authenticated user on the navbar
      - Click on the "Help" button on navbar
    
    Expected Results:
      - User should be able to access the help page and access the drop down menu with answers. The help icon in 
        the navbar will only appear if the user is logged in.
      - User should not see the help bar if they arent logged in
  
 Test 4:
   Logout:
    
    Actions/Steps:
      - Once the user login, go to the navbar on top of the page
      - Click the logout button on top right
      
    Expected Results:
      - The user should be able to see the logout button when signed in. After the button is clicked, the website should take the user to the homepage / login screen
      
 Test 5:
   Using Webcam:
    
    Actions/Steps:
      - Click Sign Up
      - Scroll to Webcam Access Page
      - Click Start Webcam Button
      - Click Take Snapshot
      
    Expected Results:
      - The user should be able to capture their face after turning on their webcam and clicking the take snapshot button. (Use Google Chrome for best results)
    
!! MILESTONE DEMO 2 !!

Test 1:
   (test):
    
    Actions/Steps:
      - 
      - 
      
    Expected Results:
      - 

Test 2:
   (test):
    
    Actions/Steps:
      - Login using your credentials
      - Click on "Account" on the navbar up top
      - Scroll down to the bottom to where it says "Change DoB"
      - Enter your new DoB in the same format as it previously was
      - Press Submit and you will see your updated DoB
      
    Expected Results:
      - Upon successfully changing DoB, the user should see his updated DoB on the settings page
      
Test 3:
   (Changing / Uploading Your email):
    
    Actions/Steps:
      - Login using your credentials
      - Click on "Account" on the navbar up top
      - Scroll down to the bottom to where it says "Change your email"
      - Enter your new email
      - Press Submit and you will see your updated email
      
    Expected Results:
      - Upon successfully changing the email, the user should see his or her updated email in the settings page and the user will not be able to login back into that account with that credentials.
      
      
Test 4:
   (Changing / Uploading a new profile Pic):
    
    Actions/Steps:
      - Login using your credentials
      - Click on "Account" on the navbar up top
      - Scroll down to the bottom to where it says "Upload New PROFILE Photo"
      - File format has to be one of these {'.jpg', '.png', '.gif'}. Anything else will throw an error or crash the website
      - Upload your new Picture
      - Scrol up to the top of the page and youll see your updated/new picture
      
    Expected Results:
      - Upon successfully uploading the pic, the user should see his or her updated profile pic (240pxx240px) in the settings page

Test 5:
   (test):
    
    Actions/Steps:
      - Login using your credentials
      - Click on "Account" on the navbar up top
      - Scroll down to the bottom where it says change your First Name
      - Scroll down to the bottom where it says change your Last Name
      - Enter your new First Name and Last Name
      - Press Submit and you will see your updated First and Last Name
      
    Expected Results:
      - Upon successfully submitting, the user should see his updated First and Last name assoicated with his account
      
      
      
## Source Code

!! MILESTONE DEMO 1 !!

v1.0.0
link : https://github.com/Capstone-Projects-2022-Spring/project-pill-io/releases/tag/v1.0.0

!! MILESTONE DEMO 2 !!

v2.0.0
https://github.com/Capstone-Projects-2022-Spring/project-pill-io/releases/tag/v2.0.0

