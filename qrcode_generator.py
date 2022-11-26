import qrcode
import smtplib
from email.message import EmailMessage
import imghdr
import os
import time

groups = ["Group1","Group2","Group3","Group4"]

def openCSV(csv_file):
    csv_list = []
    with open(csv_file,'r') as f:
        for line in f:
            if line == "\n":
                continue
            row=line.strip().split(',')
            csv_list.append(row)
    return csv_list

def sendQrImages(csv_file:str, group:int):
    csv_list = openCSV(csv_file)
    for row in csv_list:    
        email = row[0]
        name = row[1] + " " + row[2]
        address = "wameedh.reg@gmail.com"
        password = "tniezkrcxrkesjxv"
        link = "https://drive.google.com/drive/u/1/folders/174QIJKFFSB2RzGEx4J7MRfCubu__plJ_?fbclid=IwAR3zWXlDZzARxY6K6Tqc2wUp9Mcwl_CWAUzErleIqCUtnvZDE6cupO1YCE8"
        msg = EmailMessage()
        msg["Subject"] = "Arduino Bootcamp"
        msg["From"] = address
        msg["To"] = email 
        msg.set_content(f"Dear ARDUINO BOOTCAMP applicant,\n\nWe hope this email finds you well, It pleases us to inform you that you have been SELECTED to participate in the Arduino Bootcamp, which will take place Saturday the 29th \n\nyou're assigned to || GROUP {group} ||, find the attached file of your group's schedule. Make sure to download and install these resources: {link} \n\nImportant remarks :\n-the event starts at 8 Am until 3:30pm\n-What you must bring with you:\n    -QR code attached below.\n    -Your laptop.(there is no problem if you can’t since you are going to work in groups)\n    -The schedule below.\n    -The provided resources.\n\n-In order to benefit the most from our program, we trust you to be punctual and respect your schedule.\nWe're excited to see you!!\nBest regards\n\nWAMEEDH SC")
        
        with open("qr_codes" + "/" + name + ".png","rb") as f:
            file_data = f.read()
            file_type = imghdr.what(f.name)
            file_name = f.name
        msg.add_attachment(file_data,maintype="image",subtype = file_type,filename = file_name)
        with open("schedule.png","rb") as f:
            file_data = f.read()
            file_type = imghdr.what(f.name)
            file_name = f.name
        msg.add_attachment(file_data,maintype="image",subtype = file_type,filename = file_name)

        with smtplib.SMTP("smtp.gmail.com",587) as s:   
            s.starttls()
            s.login(address,password)
            s.send_message(msg)
        time.sleep(0.1)



# sendQrImages()
def generateQRCodes(csv_file:str): 
        participants = openCSV(csv_file)
                
        for row in participants:
            print(row)
            file_name = row[1] + " " + row[2]
            print(file_name)
            img = qrcode.make(file_name)
            img.save("qr_codes/" + file_name + ".png")


# for file in os.listdir("groups_with_emails"):
#     generateQRCodes("groups_with_emails/" + file)

# sendQrImages("groups_with_emails/Arduino BootCamp V7.0 (Responses) - Group 1.csv", 1)
# sendQrImages("groups_with_emails/Arduino BootCamp V7.0 (Responses) - Group 2.csv", 2)
# sendQrImages("groups_with_emails/Arduino BootCamp V7.0 (Responses) - Group 3.csv", 3)
# sendQrImages("groups_with_emails/Arduino BootCamp V7.0 (Responses) - Group 4.csv", 4)
