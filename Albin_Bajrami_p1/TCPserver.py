import socket
import threading
import datetime
import random

def IPADDRESS():    
    return 'IP Adresa e klientit eshte: %s' % address[0]

def PORT():
    return 'Klienti eshte duke perdorur portin %d' % address[1]

def COUNT(s):
	a = s.lower()
	b = "aeiouy"
	vowels = 0
	for letter in a:
		if letter in b:
			vowels = vowels + 1
	consonants = len(a) - vowels
	return 'Teksti i pranuar permban %d zanore dhe %d bashketingellore' % (vowels, consonants)

def REVERSE(s): 
	return s[::-1] 

def PALINDROME(s): 
	rev = REVERSE(s).lower()
	a = "Teksti i dhene eshte palindrome"
	b = "Teksti i dhene nuk eshte palindrome"
	if (s.lower() == rev): 
		return a
	else:
		return b

def TIME():
	time = datetime.datetime.now()
	return time.strftime("%d.%m.%Y %I:%M:%S %p")

def GAME():
	tup = (random.sample(range(1, 35),5))
	return sorted(tup)

def GCF(num1, num2):
    n1 = int(num1)
    n2 = int(num2)
    for x in range(n1 if n1<n2 else n2, 0, -1):
        if n1%x==0 and n2%x==0:
            return x

def CONVERT(convert, num):
    number = float(num)
    def cmToFeet():
        return number*0.0328084
    def FeetToCm():
        return number*30.48
    def kmToMiles():
        return number*0.621371
    def MileToKm():
        return number*1.60934
    def default():
        return "Incorrect convert call"
    switcher = {
        'cmToFeet': cmToFeet,
        'FeetToCm': FeetToCm,
        'kmToMiles': kmToMiles,
        'MileToKm': MileToKm
        }
    def switch(convert):
        return switcher.get(convert, default)()
    return '%.2f' %switch(convert)

def BMI(height1, weight1):
    height = float(height1)
    weight = float(weight1)
    bmi = weight/(height**2)
    if bmi<18.5:
        a = "nenpeshe"
    elif bmi>=18.5 and bmi<25:
        a = "i shendetshem"
    elif bmi>=25:
        a = "mbipeshe"
    return 'Indexi juaj BMI eshte %.2f dhe ju jeni %s' %(bmi, a) 

def PRIME_NUMBERS(start1, end1):
    start = int(start1)
    end = int(end1)
    list = []
    for i in range(start, end+1):
        if i>1:
            for j in range(3, i+1):
                if(i%(j-1))==0:
                    break
                if i==j:
                    list.append(i)
    return 'Ndermjet numrave '+start1+' dhe '+end1+' numra te thjeshte jane: %s' %list 

def THIRR(argumenti):
    arguments = argumenti.split(" ")
    
    if(arguments[0] == 'quit'):
        return 'quit'

    elif len(arguments)==1:
        function1 = {
            'IPADDRESS': 
            IPADDRESS,
            'PORT': 
            PORT,
            'TIME': 
            TIME,
            'GAME': 
            GAME
            }
        return function1.get(arguments[0], "Invalid functions")()

    elif len(arguments)==2:
        function2 = {
            'COUNT': 
            COUNT,
            'REVERSE': 
            REVERSE,
            'PALINDROME': 
            PALINDROME,
            }
        return function2.get(arguments[0], "Invalid functions")(arguments[1])

    elif len(arguments)==3:
        function3 = {
            'CONVERT': 
            CONVERT,
            'GCF': 
            GCF,
            'BMI': 
            BMI,
            'PRIME_NUMBERS': 
            PRIME_NUMBERS
            }
        return function3.get(arguments[0], "Invalid functions")(arguments[1], arguments[2])

    else:
        return 'Mungojne te hyrat ose jane jovalide!'


#e zgjerojme klasen threading.Thread dhe e mbishkruajme metoden run
class ClientThread(threading.Thread):

    #konstruktori i klases ClientThread
    def __init__(self, address, client):
        threading.Thread.__init__(self)
        self.client = client

    #mbishkrimi i metodes run
    def run(self):
        print("Eshte lidhur klienti me IP %s ne portin %d" %address)
        self.client.send(bytes("Jeni lidhur me serverin, shkruani kerkesen",'utf-8'))
        mesazhi = ''
        while True:
            #kerkesat nuk ia kalojne 128 byte-ve
            data = self.client.recv(124)
            print("Nga klienti ", str(data))
            mesazhi = str.encode(str(THIRR(data.decode("UTF-8"))))
            #msg = data.decode()
            if str(THIRR(data.decode("UTF-8")))=='quit':
              break
            print("Tek klienti ", mesazhi)
            self.client.send(mesazhi)
        self.client.close()
        print("Klienti me IP %s ne portin %d eshte shkycur me sukses!" %address)

serverName = 'localhost'
serverPort = 13000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((serverName, serverPort))

print('Serveri eshte startuar ne %s ne portin %d' %(serverName, serverPort))
server.listen(1)
print('Serveri eshte i gatshem te pranoje kerkesa')

while True:
    client, address = server.accept()
    #formojme objekt nga klasa e trasheguar ClientThread, e cila si parametra hyres ka
    #objektin "client" dhe listen "address" qe permbane IP dhe portin e hostit
    newthread = ClientThread(address, client)
    #funksioni start tek klasa threading.Thread i ekzekuton te gjitha funkionet
    newthread.start()