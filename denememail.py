import smtplib, ssl, getpass
import os

class Email(object):
    def __init__(self):
        self.port = 465  # SSL port
        self.smtp_server = "smtp.gmail.com" 
        creds = self.login_credentials()   
        self.sender_email = creds["email"] 
        self.password = creds["pass"]      
        self.context = ssl.create_default_context()


        self.body = ""
        with open("/root/Masaüstü/sonuclar.txt", "r") as file:
            self.body = file.read()
    

    def login_credentials(self):
        sender_email = "mail-alani"
        password = "sifre-alani"
        return {"email":sender_email, "pass":password}

    def message(self):
        subject = "Başlık Gelecek"
        message = self.body
        #return str(f"Subject: {subject}\n" f"{message}")
        return "Subject: {0}\n{1}".format(subject, self.body)

    def send_mail(self):
        receiver_email = str(input(r"Alici Mail: "))
        message = self.message()
        try:
            with smtplib.SMTP_SSL(self.smtp_server, self.port, context=self.context) as server:
                server.login(self.sender_email, self.password)
                server.sendmail(self.sender_email, receiver_email, message)
                print("\nBasari ile gönderildi!")
        except Exception as e:
            print("\nHATA!!", e)


if __name__ == "__main__":
    email = Email()
    email.send_mail()