import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
host_address="sender_emai"
host_pass ="sender_password"
guest_address ="rec_email"
subject ="Your system is fail"
content ="Hi vishnupal your webserver is fail" 
message=MIMEMultipart()
message['From'] =host_address
message['To']=guest_address
message['Subject'] =subject
message.attach(MIMEText(content,'plain'))
session=smtplib.SMTP('smtp.gmail.com',587)
session.starttls()
session.login(host_address,host_pass)
text=message.as_string()
session.sendmail(host_address,guest_address,text)
session.quit()
print("suucess ")
