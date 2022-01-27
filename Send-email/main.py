

from calendar import day_abbr, weekday
import datetime as dt 
import random
import smtplib
MY_EMAIL = "test@gmail.com"
MY_PASSWORD= 'testpassword'

now = dt.datetime.now()
year = now.year
month = now.month
day_of_month = now.day
day_of_week = now.weekday()
print(year)
print(month)
print(day_of_month)
print(day_of_week)
if day_of_week == 2:
    with open ("Birthday Wisher/quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL, msg=f"Subject:Webnesday Motivation\n\n{quote}"
        )
