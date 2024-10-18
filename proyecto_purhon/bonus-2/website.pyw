import time
from datetime import datetime as dt

host_temp = "hosts"
host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
websit_list=["wwww.facebook.com","facebook.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,9) < dt.now() < dt( dt.now().year,dt.now().month,dt.now().day,17):
        print( " hora del trabajo desgraciado")
        with open(host_temp, 'r+')as file:
            contenedor = file.read()
            for website in  websit_list:
                if website in contenedor:
                    pass
                else:
                    file.write(""+redirect+" "+ website+ "\n")
    else:
        with open(host_temp, 'r+') as file:
            contenedor = file.readlines() 
            file.seek(0) 
            for line in contenedor:
                if not any(website in line for website in websit_list):
                    file.write(line)
            file.truncate()  
        print("Hora de descansar")
    time.sleep(5)