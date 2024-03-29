##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

from datetime import datetime
import pandas
import random
import smtplib
today_tuple = (datetime.now().month, datetime.now().day)
data = pandas.read_csv("birthday-wisher/birthdays.csv")

MY_EMAIL = "test@gmail.com"
MY_PASSWORD = 'test'
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# contents={}
if today_tuple in birthdays_dict:  
    birthday_person = birthdays_dict[today_tuple]
    file_path =f"birthday-wisher/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"], msg=f"Subject: Happy Birthday ! \n\n {contents}"
        )



