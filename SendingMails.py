from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import time
import os

# Sender and receiver email details
email = "yourEmail@gmail.com"
receive_email = ["receive1@gmail.com", "receive2@surveoo.com"]

# Email subject and message
subject = "test"
message = "test"

# Create the MIMEMultipart message
myCV = MIMEMultipart()
myCV['From'] = email
myCV['To'] = ', '.join(receive_email)
myCV['Subject'] = subject

# Attach the message body as plain text
myCV.attach(MIMEText(message, 'plain'))

# Attach the PDF file
pdf_path = 'C:/Users/public/Downloads/nameYourPDF.pdf'
with open(pdf_path, 'rb') as pdf_file:
    part = MIMEApplication(pdf_file.read(), _subtype='pdf')
    part.add_header('Content-Disposition', 'attachment', filename=os.path.basename(pdf_path))
    myCV.attach(part)

# Set up the SMTP server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

# Login to the SMTP server
server.login(email, "fgzs qzfv ytre qdzi")  # Replace this with your actual password or an app-specific password if 2FA is enabled

# Convert the MIMEMultipart message to a string
text = myCV.as_string()

# Timer function to send emails at intervals
def timer(second):
    hour, minutes, seconds = 0, 0, 0
    index = 0

    print("The timer starts !!\n")
    while second > 0:
        time.sleep(1)
        if second >= 3600:
            hour = second // 3600
            min_sec = second % 3600
            minutes = min_sec // 60    
            seconds = min_sec % 60
        else:
            minutes = second // 60
            seconds = second % 60

        second -= 1

        if second % 60 == 0 and index < len(receive_email):
            server.sendmail(email, receive_email[index], text)
            print(f"Email has been sent to {receive_email[index]}")
            index += 1
            print("\n")

# Start the timer for 120 seconds (adjust as necessary)
timer(120)

# User input to exit
x = input("Hit Enter to Exit, or Input any other key to continue ")
if not x:
    exit()

# Close the server connection
server.quit()
