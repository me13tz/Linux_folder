#!/usr/bin/python3.5

import smtplib, sys, getpass

## get inputs
addr_input = input("Enter 'to' address: ")
msg_input = input("Message: ")

## establish connection
smtpObj = smtplib.SMTP('smtp.mail.yahoo.com', 587)
print('Establishing connection...')
smtpObj.ehlo()
smtpObj.starttls()

##get password
pwd_input = getpass.getpass("Enter your account password. When you hit enter, the email will be sent: ")

## login with credentials
smtpObj.login('YOUR_EMAIL_ADDR@yahoo.com', pwd_input)

## format object like so: ('from_addr', 'to_addr', 'message')
## send it off!
smtpObj.sendmail('YOUR_EMAIL_ADDR@yahoo.com', addr_input, msg_input)
print('Sending email...')
smtpObj.quit()
print('Done.') 

