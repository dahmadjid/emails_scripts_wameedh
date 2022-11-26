import qrcode
import smtplib
from email.message import EmailMessage
import imghdr
import os
import time




def openCSV(csv_file):
    csv_list = []
    with open(csv_file,'r') as f:
        for line in f:
            if line == "\n":
                continue
            row=line.strip().split(',')
            csv_list.append(row)
    return csv_list

def sendCertificates(csv_file:str, certificates_folder:str, extension:str):
    csv_list = openCSV(csv_file)
    new_certificates = []
    certificates = sorted(os.listdir(certificates_folder))
    for i in certificates:
        if len(i.split('.')[0].split(' ')[-1]) == 1:
            os.rename(certificates_folder+ '/' + i,certificates_folder+ '/' + i.split(' ')[0] + ' '+ i.split(' ')[1] + ' 0' + i.split(' ')[2])
   
    i = 0
    for row in csv_list:  

        email = row[0]
        name = row[1]
        if email == 'no_email':
            i+=1
            continue
        address = "wameedh.reg@gmail.com"
        password = "tniezkrcxrkesjxv"
        msg = EmailMessage()
        msg["Subject"] = "Arduino Bootcamp"
        msg["From"] = address
        msg["To"] = email 
        msg.set_content(f"Hello dear participant!\nWe hope this email finds you well, Sorry for the mistake on the certificates\n\nWe would like to inform you that your ARDUINO BOOTCAMP journey is successfully done!  \nKindly check your certificate  ( see attached file below) \n\nExcited to learn more? We invite you to pass by Wameedh and get your hands dirty ! \n\nStay tuned for our upcoming events! \n\nBest wishes,")     
        with open(certificates_folder + "/"+ certificates[i],"rb") as f:
            file_data = f.read()
            file_type = imghdr.what(f.name)
            file_name = name
            msg.add_attachment(file_data,maintype="image",subtype = file_type,filename = file_name)
        

        with smtplib.SMTP("smtp.gmail.com",587) as s:   
            s.starttls()
            s.login(address,password)
            s.send_message(msg)
        time.sleep(0.1)
        i+=1
sendCertificates("Participants.csv", "Participants", ".jpg")