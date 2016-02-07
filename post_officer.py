#!/bin/python

import smtplib
import imapy

def send_some_mail():
    smtpObj = smtplib.SMTP('smtp.gmail.com',587)
    smtpObj.ehlo()
    smtpObj.starttls()
    username = input('Username: ')
    password = input('Password: ')
    recipient = input('Recipient: ')
    smtpObj.login(username,password)
    #Body is supposed to be separated by newline, but this has not worked in tests
    smtpObj.sendmail(username,recipient,'Subject: Hello World \n This is an email.')
    smtpObj.quit()

def get_some_mail():
    imapObj = imapy.connect(
        host = 'imap.gmail.com',
        username = input('Username: '),
        password = input('Password: '),
        ssl = True)
    folders = imapObj.folders()
    emails = imapObj.folders('Inbox').emails(-5)

def main():
    option = input('I\'ve never done this before.\n'
            '1: Get\n2: Send\nSelect: ')
    if option == '1':
        get_some_mail()
    elif option == '2':
        send_some_mail()
    else: print ("Wrong answer")

main()
