# project-pill-io
project-pill-io created by GitHub Classroom

# Project Abstract
This project proposes a machine learning empowered pill dispenser that will allow both caregivers and patients to have peace of mind as they partake in what for most of them is a daily requirement for their health and safety. This pill dispensing software will allow for medications to always be dispensed with only the needed medications and dosages based on the facial recognition of the patient attempting to get their medication. This will allow patients to get their medication without the struggle of opening or sorting through pill bottles and help prevent the possibility of an overdose on medications by no longer having patients access of all their medicine supply at the same time. Moreover, caregivers will be able to access data regarding the frequency and timing of when/if their patients take their medications which will help inform their care. 

# Contributers
Abin Cheriyan, Anna Minasyan, Ethan Lewis, Misha Golikov, Tandi Huran

# PythonAnywhereHosting
pillio.pythonanywhere.com

# Release v1.0.0

## Release Notes
This is our first release, so there is no previous release to compare to. This release contains preliminary sign-up, log-in, medication registration, and authenication screens and functionallity. 

https://pillio.pythonanywhere.com/

## How to Use and Test
Instruction on how to use the release and how  to test. (should contains language similar Test Procedures Document) 

## UAT

Test 1:
  Creating an Account:
    
    Actions/Steps:
      Click Sign Up
      Enter Username (it has to be an email)
      Enter your first name 
      Enter your last name
      Enter your preferred Password 
      Enter your Date of Birth
      Enter a picture of your face (it will later be used as your Profile Picture and for facial recognition)
    
    Expected Results:
     The user is able to Sign up without any problem and the system will save the user's details onto the db. 
     User will see an "Account created" confirmation popup

Test 2:
  Logging into an Account:
    
    Actions/Steps:
      
    
    Expected Results:
     
Test 3:
  Accessing help/faq page:
    
    Actions/Steps:
    Click on Login on the navbar
    Enter your credentials
    Click on Login button
    Once logged in, Help page should be available to authenticated user on the navbar
    Click on the "Help" button on navbar
      
    
    Expected Results:
    User should be able to access the help page and access the drop down menu with answers. The help icon in the navbar will only appear if the user is logged in.
    User should not see the help bar if they arent logged in
    
## Source Code

v1.0.0
link : https://github.com/Capstone-Projects-2022-Spring/project-pill-io/releases/tag/v1.0.0
