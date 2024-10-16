import smtplib
import time

email = "yourEmailName@gmail.com"
receive_email = ["receiveemail1@gmail.com","receiveemail2@outlook.com"]

subject = "test"
message = "test"

text = f"Subject: {subject}\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

server.login(email,"your password from the account password application")

def timer(second):
    hour, minutes, seconds = 0,0,0
    index = 0

    print ("The timer starts !!")
    while second> 0:
        time.sleep(1)
        if second >= 3600 :
            hour = second // 3600
            if hour > 0:
                min_sec = second % 3600
                minutes = min_sec // 60    
                seconds = min_sec % 60
        else:
            minutes = second // 60
            seconds = second % 60
 
        second -=1 
        if second % 60 == 0:
            server.sendmail(email, receive_email[index], text)
            print("Email has been sent to "+ receive_email[index])
            index = index + 1

 
timer(120)

x = input("Hit Enter to Exit, or Input any other key to continue ")

if not x :
    exit()