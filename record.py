from datetime import datetime
from datetime import date
import re


class Record():
    def __init__(self, forename, surname, dob, gender, csStudent):
        #Store the created time for this instance in the format "Y-M-D H:M:S"
        self._createdTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#Validation for all values entered
        if isinstance(forename, str):
            self._forename = forename
        else:
            raise TypeError("Forename must be str")

        if isinstance(surname, str):
            self._surname = surname
        else:
            raise TypeError("Surname must be str")

        if re.match(r"\d\d\d\d-\d\d-\d\d", dob):
            self._fullDOB = dob
            self._dobYear = int(dob.split("-")[0])
            self._dobMonth = int(dob.split("-")[1])
            self._dobDay = int(dob.split("-")[2])
        else:
            raise ValueError("Date of Birth must fit format \"yyyy-mm-dd\"")

        if gender in ["F", "M", "O"]:
            self._gender = gender
        else:
            raise ValueError("Gender must be F/M/O")

        if isinstance(csStudent, bool):
            self._csStudent = csStudent
        else:
            raise TypeError("CS Student status must be bool")


#Getter methods


    def getForename(self):
        return self._forename

    def getSurname(self):
        return self._surname

    def getGender(self):
        return self._gender

    def getCsStudent(self):
        return self._csStudent

    def getCreatedTime(self):
        return self._createdTime

    def getDOB(self):
        return self._fullDOB

    def getAge(self):
        now = date.today()
        year = now.year - self._dobYear
        if (now.month, now.day) < (self._dobMonth, self._dobDay):
            year -= 1
        return year

#Setter methods (each has validation)
    def setForename(self, forename):
        if isinstance(forename, str):
            self._forename = forename
        else:
            raise TypeError("Forename must be str")

    def setSurname(self, surname):
        if isinstance(surname, str):
            self._surname = surname
        else:
            raise TypeError("Surname must be str")

    def setGender(self, gender):
        if gender in ["F", "M", "O"]:
            self._gender = gender
        else:
            raise ValueError("Gender must be F/M/O")

    def setCsStudent(self, csStudent):
        if isinstance(csStudent, bool):
            self._csStudent = csStudent
        else:
            raise TypeError("CS Student status must be bool")

    def setDOB(self, dob):
        if re.match(r"\d\d\d\d-\d\d-\d\d", dob):
            self._fullDOB = dob
            self._dobYear = int(dob.split("-")[0])
            self._dobMonth = int(dob.split("-")[1])
            self._dobDay = int(dob.split("-")[2])
        else:
            raise ValueError("Date of Birth must fit format \"yyyy-mm-dd\"")

    def dayBorn(self):
        #Create string date in format "yyymmdd"
        dateObject = str(self._dobYear) + \
            str(self._dobMonth) + str(self._dobDay)
        #Convert to date object
        dobDateObject = datetime.strptime(dateObject, "%Y%m%d").date()
        daysOfWeek = ["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"]
        #Using datetime lib's weekday function (returns integer 0-6)
        dayBorn = daysOfWeek[dobDateObject.weekday()]
        return dayBorn


#Testing values
rec1 = Record("John", "Doe", "2004-09-15", "M", True)
print(rec1.getForename())
print(rec1.getSurname())
print(rec1.getGender())
print(rec1.getCsStudent())
print(rec1.getCreatedTime())
print(rec1.getAge())
print(rec1.dayBorn())
