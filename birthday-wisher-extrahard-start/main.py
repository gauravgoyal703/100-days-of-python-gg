##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas
import random

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()

birthdays = pandas.read_csv("birthdays.csv").to_dict(orient='records')
print(birthdays)

for birthday in birthdays:
    if birthday["month"] == now.month and birthday["day"] == now.day:
        letter_number = random.randint(1, 3)
        with open(f"letter_templates/letter_{letter_number}.txt") as letter:
            text = letter.read()
            text = text.replace("[NAME]", birthday["name"])
            print(text)


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




