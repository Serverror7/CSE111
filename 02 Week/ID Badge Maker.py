x = " .,/-+"
print("Please enter the following information:\n")
nameFirst = input("First name: ")
nameLast = input("Last name: ")
email = input("Email address: ")
job = input("Job title: ")
ID = input("Identification Number:")
phone = input("Phone Number:")

print(f"\n\n---------------------------------------------\n{nameLast.upper().strip(x)}, {nameFirst.strip(x)}\n{job.title().strip(x)} \nID: {ID.strip(x)}\n\n{email.lower().strip(x)}\n{phone.strip(x)}\n---------------------------------------------")