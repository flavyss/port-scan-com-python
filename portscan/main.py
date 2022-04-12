import socket,sys

print('''
PPPP   OOO  RRRR  TTTTTT      SSS   CCC  AA  N   N 
P   P O   O R   R   TT       S     C    A  A NN  N 
PPPP  O   O RRRR    TT   ---  SSS  C    AAAA N N N 
P     O   O R R     TT           S C    A  A N  NN 
P      OOO  R  RR   TT       SSSS   CCC A  A N   N 
                                                                           

by:KriptonFlavy
''')

ip = input('Digite o IP ou Dominio do Alvo: ')

while True:
    if 'www' in ip:
        ip = input('Digite Corretamente apenas o dominio [sem http, https ou www]: ')

    elif 'http' in ip:
        ip = input('Digite Corretamente apenas o dominio [sem http, https ou www]: ')

    elif 'https' in ip:
        ip = input('Digite Corretamente apenas o dominio [sem http, https ou www]: ')

    else:
        break;

doors = [21, 23, 80, 443, 1900, 8080, 5050, 5555, 8300]

for door in doors:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.1)
    code = sock.connect_ex((ip, door))
    if code == 0:
        print(door, 'OPEN')