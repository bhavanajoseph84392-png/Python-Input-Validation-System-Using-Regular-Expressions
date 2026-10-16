import re

class Validation:
    def __init__(self, mobile, password, email):
        self.mobile = mobile
        self.password = password
        self.email = email

    def mob(self):
        if re.fullmatch(r"[6-9][0-9]{9}", self.mobile):
            print("Valid Indian number")
        else:
            print("Invalid Indian number")

    def password_(self):
        patt = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=!]).{8,}$"
        if re.fullmatch(patt, self.password):
            print("Valid Password")
        else:
            print("Invalid Password")

    def mail(self):
        if re.fullmatch(r"[^@\s]+@gmail\.com", self.email):
            print("Valid Gmail format")
        else:
            print("Invalid Gmail format")


mobile = input("Enter mobile number: ")
password = input("Enter password: ")
email = input("Enter email: ")

val = Validation(mobile, password, email)
val.mob()
val.password_()
val.mail()
