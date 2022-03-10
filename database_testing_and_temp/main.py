import sqlite3



connection = sqlite3.connect('../SQLite_Python.db')

cursor = connection.cursor()
print("database created")
# cursor.execute("INSERT OR IGNORE (OR REPLACE) INTO User VALUES(1, 'misha', 02/05/1998)") - how to manually add
rows = cursor.execute("SELECT UserID, UserName, UserDOB FROM User").fetchall()
print(rows)

cursor.execute("INSERT INTO Medication VALUES (1, 'SSRI')")


#sqlite_select_query = """SELECT UserID from User where UserID = 1"""

#sqlite_select_query2 = """SELECT MedicationID from Medication where MedicaitonID = 1"""


# below line can be dow
cursor.execute("INSERT INTO UserMedication VALUES (2, (SELECT UserID from User WHERE UserID = 1), (SELECT MedicationID from Medication WHERE MedicationID = 1))")

rows = cursor.execute("SELECT PrescriptionID, UserID, MedicationID FROM UserMedication").fetchall()
print(rows[0])







exit(1)

# cursor.execute("CREATE TABLE Medication (MedicationID STRING NOT NULL UNIQUE PRIMARY KEY, MedicationType STRING NOT NULL)")
#
# cursor.execute("CREATE TABLE Picture (PictureID INT PRIMARY KEY NOT NULL UNIQUE, PicturePath STRING NOT NULL)")
#
# cursor.execute("CREATE TABLE User (UserID INT PRIMARY KEY NOT NULL UNIQUE ON CONFLICT ABORT, UserName STRING UNIQUE "
#                "ON CONFLICT ROLLBACK NOT NULL, UserDOB DATE NOT NULL)")
#
# cursor.execute("CREATE TABLE UserList (UserID INT REFERENCES User (UserID) ON DELETE CASCADE ON UPDATE CASCADE NOT "
#                "NULL)")
#
#
# cursor.execute("CREATE TABLE UserMedication (PrescriptionID INT PRIMARY KEY NOT NULL UNIQUE, UserID INT REFERENCES "
#                "User (UserID) ON DELETE CASCADE ON UPDATE CASCADE NOT NULL, MedicationID INT REFERENCES Medication ("
#                "MedicationID) ON DELETE CASCADE ON UPDATE CASCADE NOT NULL)")
#
# cursor.execute("CREATE TABLE UserPictureList (UserID INTEGER REFERENCES User (UserID) ON DELETE CASCADE ON UPDATE "
#                "CASCADE NOT NULL, PictureID INT REFERENCES Picture (PictureID) ON DELETE CASCADE ON UPDATE CASCADE "
#                "NOT NULL)")

cursor.fetchall()





#cursor.execute("INSERT INTO User VALUES (1, misha, 02/05/1998)")