##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib

data = pandas.read_csv('birthdays.csv', index_col=False)
# print(data)

my_email = 'mallalikhitha9@gmail.com'
password = "rkzdqfjnwgvwnflr"

for index, row in data.iterrows():
    # print(type(row.month))
    # print(row.name_)
    now = dt.datetime.now()
    if now.month == row.month and now.day == row.day:
        # print(f'Happy Birthday {row.name_}!!')

        with open(f'letter_templates/letter_{random.randint(1, 3)}.txt') as template:
            contents = template.read()

        contents = contents.replace('[NAME]', row.name_)
        # print(contents)

        with open(f'letters/letter_to_{row.name_}', mode='w') as letter:
            letter.write(contents)

        # print(''.join(contents))  if contents was a list

        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=row.email,
                msg=f'Subject:Happy Birthday!!\n\n{contents}'
            )
