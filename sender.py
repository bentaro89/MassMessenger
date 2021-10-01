# we import the Twilio client from the dependency we just installed
from twilio.rest import Client
import np
import pandas as pd
import re

# the following line needs your Twilio Account SID and Auth Token
SID = 'xxxxxxxxxxxxxx'  # NOT A REAL SID
AUTH_TOKEN = '1111111111111'  # NOT A REAL AUTH TOKEN
SENDER_NUMBER = 5149759436  # NOT A REAL NUMBER
EXCEL_SHEET = 'numbers.xlsx'
client = Client(SID, AUTH_TOKEN)

MESSAGE = "Put your message here! "


# Given a number, send the message
def send_to(num):

    # Ensure that message sent to number
    try:
        # change the "from_" number to your Twilio number and the "to" number
        # to the phone number you signed up for Twilio with, or upgrade your
        # account to send SMS to any phone number
        client.messages.create(to="+1" + str(num),
                               from_=str(SENDER_NUMBER),
                               body=MESSAGE)

        print('Sent perfectly to ' + str(int(num)))

    except:
        print('Unable to Send Num to ' + str(num))


# Ensure that given number contains only integers
def strip_number(str1):
    new_string = str(str1)
    digits = re.sub("[^0-9]", "", str(new_string.split('.')[0]))
    return digits


def send_to_excel():
    data = pd.read_excel(EXCEL_SHEET) # retrieve data from excel
    df = pd.DataFrame(data, columns=['pc_phone_home', 'pc_phone_cell']) # read columns that has phone numbers

    # loop through the columns, stripping the numbers and calling the function with the number
    for i in range(len(df.values)):

        if df.values[i][1] is not np.nan and len(str(df.values[i][1])) > 9: # cell
            print('cell:' + strip_number(df.values[i][1]))
            send_to(strip_number(df.values[i][1]))
        elif df.values[i][0] is not np.nan and len(str(df.values[i][0])) > 9: # home phone
            print('home:' + strip_number(df.values[i][0]))
            send_to(strip_number(df.values[i][0]))
        else:
            print("Does not have number")

send_to_excel()
print("DONE")
