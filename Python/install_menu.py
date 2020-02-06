# /usr/bin/python2.7

import os
import argparse
import sys
import pty


print ' '
print '--------------------------------------------------'
print 'System Detection and Install Script : SDIS ver 0.1'
print '--------------------------------------------------'
print ' '
print '      *Custom scripts made by Denjiro*    '

print '\n'

print '                 Menu : \n       '
print '1. Base install to remote server using Ansible \n'
print '2. Base install to local server using Bash Script  \n '
print '- A : LAMP Stack install \n'
print '- B : LEMP Stack install \n'
print '3. Install by user using prompt \n'
print '4. Print various system info. \n'

try: 
 userChoice = raw_input("Choice : ")

 def installMenu(userChoice):
     
    if userChoice == '1':
     def choice(userChoice):
        print ' '
        print 'user choice is 1 : Base Install using Ansible for remote server. \n'

    elif userChoice == '2':
     def choice(userChoice):
        print ' '
        print 'user choice is 2 : Now choice between A or B according to your Web Stack usage'
        letter = raw_input('A or B : ')
        if letter == 'A' or 'a':
         webStack = 'wget https://github.com/jasodeep/ansible-lamp-stack-playbook/blob/master/lamp-playbook.yml'
         os.system(webStack)

    elif userChoice == '3':
     def choice(userChoice):
        print ' '
        print 'user choice is 3.'
        print 'Entering prompt ... \n'
        pty.spawn("/bin/bash")

 
    elif userChoice == '4':
     def choice(userChoice):
        print ''
        print 'user choice is 4'
        print ' '
        print 'which info would you want to see ? \n'
        print '1. Python Interpreter version \n'
        print '2. Kernel Version '
        print ' '
        info = raw_input("Choice : ")
        if info == '1':
            py = sys.path
            print py + '\n'
        elif info == '2':
            ops = sys.platform
            print ' '
            print ops + '\n'
            
    choice(userChoice)

 installMenu(userChoice)

except KeyboardInterrupt:
    print 'Script stopped by user, using keyboard interrupt.'

sys.exit(0)



