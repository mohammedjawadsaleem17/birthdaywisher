##################### Normal Starting Project ######################

import datetime as dt
import pandas,random,smtplib
today = (dt.datetime.now().month,dt.datetime.now().day)

MY_EMAIL="referrals.jawad@gmail.com"
MY_PASSWORD = "oyyvnideufjipksf"    #Dont Worry this password is no longer valid hehe;)

data = pandas.read_csv("birthdays.csv")


birthdays_dict = {(data_row["month"],data_row["day"]): data_row for (index,data_row) in data.iterrows()}


if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_{random.randint(1,3)}.txt"
    print(file_path)
    with open(file_path) as letter:
        contents = letter.read()
        contents = contents.replace("[NAME]",birthday_person["name"])
        print(type(contents))
        print(contents)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=birthday_person["email"],msg=f"Subject:Happy Birthday!\n\n{contents}")
        print("success")
