import socket  #Importamo library
import datetime
from Local_Machine_Info import print_machine_info
print("Danasnji datum: " + str(datetime.datetime.now()) + "\n")
print("Pokus se izvodi na racunalu: ")
print_machine_info()
print("\n")
x = int(input("OD kojeg porta zelite da trazi: "))
y = int(input("DO kojeg porta zelite da trazi: "))

#ip = socket.gethostbyname(socket.gethostname())  # IP adresa od hosta
ip = "www.aspira.com"
for port in range(x, y):  # prolazi kroz sve portove od x do y
    try:
        serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # stvara novi socket
        serv.bind((ip, port))  # povezuje socket sa adresom
    except:
        print('Otvoreni port: ', port)  # isprintat ce sve otvorene portove
    serv.close()  # zatvara konekciju