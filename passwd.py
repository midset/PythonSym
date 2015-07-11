#!/usr/bin/python3
import sys , os
if sys.platform == 'linux-i386' or sys.platform == 'linux2' or sys.platform == 'darwin':
    SysCls = 'clear'
uname = 'uname -a '

os.system(SysCls)

print "\n|---------------------------------------------|"
print "| ##~ Mid Set LoC ReAd                          |"
print "|   2013     midset.py                          |"
print "|    - Linux server read files                  |"
print "| Read /etc/passwd >> passwd.txt                |"
print "| GreeTz : HsN,Hiso,Fat7,vir,shagone,oudouz,ked |"
print "|          All Rights Reserved @ Mid-Set        |"
print "| C0ntact : http://fb.com/midset00              |"
print "|----------------------------------------------|\n"

os.system(uname)
		
def main():
    set = 5000
    passwd = open('/etc/passwd' , 'r')
    passinput = open ('passwd.txt' , 'w')
    buffer = passwd.read(set)
    while len(buffer) :
        passinput.write(buffer)
        buffer = passwd.read(set)
print ('Wait while copying ....')
print ('Done copying passwd file ^_^')
print ('''
Check passwd.txt
# type "cat passwd.txt"
<3  Mid Set ~ <3 
''')

	
if __name__ == "__main__": main()
