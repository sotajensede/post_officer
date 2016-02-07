#!/bin/python

import smtplib
import imapy
import getpass

def send_some_mail():
    smtpObj = smtplib.SMTP('smtp.gmail.com',587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(username = input('Username: '),
                            password = getpass.getpass())
    #I guess sendmal() needs 2 newlines after the subject??
    subject = input('Subject: ')
    body = input('Body: ')
    smtpObj.sendmail(username,
                                  recipient = input('Recipient: '),
                                  'Subject: %s\n\n%s' % (subject,body))
    smtpObj.quit()

def get_some_mail():
    imapObj = imapy.connect(
        host = 'imap.gmail.com',
        username = input('Username: '),
        password = getpass.getpass(),
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
