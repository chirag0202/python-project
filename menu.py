import os
import getpass

def drive():
    os.system("clear")
    print("""Press a: List all the drives and their partition details
Press b: List the partiions of a drive
Press c: Partition a drive
Press d: Format a drive
Press e: Mount a drive
Press f: Unount a drive
Press g: Exit to main menu""")
    dc=input("Enter you choice : ")
    if dc=='a':
     os.system("fdisk -l")
    elif dc=='b':
     os.system("fdisk -l /dev/{}".format(input("Enter the disk name")))
    elif dc=='c':
     dname=input("Enter the disk name")
     os.system("fdisk /dev/{}".format(dname))
     os.system("udevadm settle")
    elif dc=='d':
     os.system("mkfs.ext3 /dev/{}".format(dname))
    elif dc=='e':
     dname=input("Enter the disk name")
     mname=input("Input name of mount point-")
     os.system("mkdir {}".format(mname))
     os.system("mount /dev/{}/{}".format(dname,mname))
    elif dc=='f':
     os.system("unmount /dev/{}".format(dname))
    elif dc=='g':
     return
    else:
     os.system("""echo "$(tput setaf 1) $(tput blink) WRONG CHOICE!!! $(tput sgr0) $(tput setaf 7)" """)


def docker():
   os.system("clear")
   print("""Press a: Start docker\nPress b: Stop docker
Press c: Install a new image
Press d: Open a container
Press e: Print already installed Images
Press f: Display running containers
Press g: Display all containers
Press h: Go back to main menu""")
   dchoice=input("Enter your choice : ")
   if dchoice=='a':
    os.system("systemctl start docker")	
    print(os.system("systemctl status docker"))
   elif dchoice=='b':
    os.system("systemctl stop docker")
    print(os.system("systemctl status docker"))	
   elif dchoice=='c':
     os.system("docker pull {}".format(input("Enter the name of image :\n(format)  <image name>  if you want the latest version else <image name>:<version>     :")))
   elif dchoice=='d':
     os.system("docker run -t -i {}".format(input("Enter the name of image :\n(format)  <container name>  if you want the latest version else <container  name>:<version>     :")))
   elif dchoice=='e':
    print(os.system("docker images"))
   elif dchoice=='f':
    print(os.system("docker ps"))
   elif dchoice=='g':
    print(os.system("docker ps -a"))
   elif dchoice=='h':
    return
   else:
    os.system("""echo "$(tput setaf 1) $(tput blink) WRONG CHOICE!!! $(tput sgr0) $(tput setaf 7)" """)


os.system("clear")
os.system("tput setaf 1")
print("\t\t\t\t",end='')
os.system("tput bold")

os.system("""COLUMNS=$(tput cols) 
title="WELCOME To My TUI" 
printf "%*s\n"  $(((${#title}+$COLUMNS)/2)) $(tput smul)"$title"  """)
os.system("tput rmul")
os.system("tput sgr0")
os.system("tput setaf 7")

os.system("tput setaf 3")

print("\n")
os.system("""COLUMNS=$(tput cols) 
design="RRRRRRR II NN   NN GGGGGGG SSSSSS  OOOOOO FFFFFF  FFFFFF II RRRRRR EEEEEE" 
printf "%*s\n"  $(((${#design}+$COLUMNS)/2)) "$design"  """)

os.system("""COLUMNS=$(tput cols) 
design="RR   RR II NNNN NN GG      SS      OO  OO FF      FF     II RR  RR EE" 
printf "%*s\n"  $(((${#design}+$COLUMNS)/2-2)) "$design"  """)

os.system("""COLUMNS=$(tput cols) 
design="RRRRRRR II NN NNNN GG  GGG SSSSSS  OO  OO FFFFFF  FFFFFF II RRRRRR EEEEEE" 
printf "%*s\n"  $(((${#design}+$COLUMNS)/2)) "$design"  """)

os.system("""COLUMNS=$(tput cols) 
design="RR  RR  II NN  NNN GG   GG     SS  OO  OO FF      FF     II RR RR  EE" 
printf "%*s\n"  $(((${#design}+$COLUMNS)/2-2)) "$design"  """)

os.system("""COLUMNS=$(tput cols) 
design="RR   RR II NN   NN GGGGGGG SSSSSS  OOOOOO FF      FF     II RR  RR EEEEEE" 
printf "%*s\n"  $(((${#design}+$COLUMNS)/2)) "$design"  """)
print("""
""")
os.system("tput setaf 7")

passwd=getpass.getpass("Enter the password : ")
if passwd!="redhat":
 input(os.system("""echo "$(tput setaf 1) $(tput blink) WRONG CHOICE!!! $(tput sgr0) $(tput setaf 7)" """))
 os.system("clear")
 exit()

location=input("""Where would you like to perform your job?\na)Local\nb)Remote\nEnter your Choice- """)
if location=='b':
    ip_r=input("Enter your IP : ")
os.system("clear")


while location=='a':
    print("""Press 1 : Print Date
Press 2 : Print Calendar
Press 3 : Configure the web Server if already installed
Press 4 : Create or Remove  User 
Press 5 : View all folders and files
Press 6 : Create a folder
Press 7 : Create a file
Press 8 : Edit a file
Press 9 : Check if a software is already installed
Press 10: Install a software from existing repo
Press 11: Open a pre-installed software
Press 12: Docker
Press 13: Drives and Partition Management
Press 14: Start an installed service
Press 0 : Exit""")
    c=int(input("Enter a choice: "))
    if c==0:
        os.system("clear")
        exit()
    elif c==1:
    	print(os.system("date"))
    elif c==2:
    	print(os.system("cal"))
    elif c==3:
     os.system("systemctl stop firewalld")
     os.system("systemctl start httpd")	
     print(os.system("systemctl status httpd"))
    elif c==4:
        c1=input("""Choice:\na) Create User\nb) Remove User\nEnter choice-""")
        if c1=='a':
         u=input("Input username:")
         os.system("useradd {}".format(u))
         print(os.system("id {}".format(u)))
        elif c1=='b':
         u=input("Input user to be deleted:")
         os.system("userdel -r {}".format(u))
         print(os.system("id {}".format(u)))
    elif c==5:
    	print(os.system("ls"))
    elif c==6:
     folder_name=input("Enter folder name: ")
     os.system("mkdir {}".format(folder_name))
    elif c==7:
     file_name=input("Enter file name: ")
     os.system("touch {}".format(file_name))
    elif c==8:
     file_name=input("Enter file name: ")
     os.system("gedit {}".format(file_name))
    elif c==9:
     soft_name=input("Enter the name of software: ")
     print(os.system("rpm -q {}".format(soft_name)))
    elif c==10:
     soft_name=input("Enter the name of software: ")
     print(os.system("dnf install {}".format(soft_name)))
    elif c==11:
     os.system(input("Enter the name of software : "))
    elif c==12:
     docker()
    elif c==13:
     drive()
    elif c==14:
     os.system("systemctl start {}".format(input("Enter the name of service : ")))
    else:
     os.system("""echo "$(tput setaf 1) $(tput blink) WRONG CHOICE!!! $(tput sgr0) $(tput setaf 7)" """)
    input("Press Enter to continue...")
    os.system("clear")


while location=='b':
    print("""Press 1 : Print Date
Press 2 : Print Calendar
Press 3 : Configure the web Server if already installed
Press 4 : Create or Remove  User
Press 5 : View all folders and files
Press 6 : Create a folder
Press 7 : Create a file
Press 8 : Edit a file
Press 9 : Check if a software or service is already installed
Press 10: Install a software or service from existing repo
Press 11: Open an installed software
Press 12: Change IP
Press 13: Start an installed service
Press 0 : Exit""")
    c=int(input("Enter a choice: "))
    if c==0:
         os.system("clear")
         exit()
    elif c==1:
    	print(os.system("ssh {} date".format(ip_r)))
    elif c==2:
    	print(os.system("ssh {} cal".format(ip_r)))
    elif c==3:
     os.system("ssh {} systemctl stop firewalld".format(ip_r))
     os.system("ssh {} systemctl start httpd".format(ip_r))	
     print(os.system("ssh {} systemctl status httpd".format(ip_r)))
    elif c==4:
        c1=input("""Choice:\na) Create User\nb) Remove User\nEnter choice-""")
        if c1=='a':
         u=input("Input username:")
         os.system("ssh {} useradd {}".format(ip_r,u))
         print(os.system("ssh {} id {}".format(ip_r,u)))
        elif c1=='b':
         u=input("Enter the user to be deleted:")
         os.system("ssh {} userdel -r {}".format(ip_r,u))
         print(os.system("ssh {} id {}".format(ip_r,u)))
    elif c==5:
    	print(os.system("ssh {} ls".format(ip_r)))
    elif c==6:
     folder_name=input("Enter folder name: ")
     os.system("ssh {} mkdir {}".format(ip_r,folder_name))
    elif c==7:
     file_name=input("Enter file name: ")
     os.system("ssh {} touch {}".format(ip_r,folder_name))
    elif c==8:
     file_name=input("Enter file name: ")
     os.system("ssh {} gedit {}".format(ip_r,folder_name))
    elif c==9:
     soft_name=input("Enter the name of software or service: ")
     print(os.system("ssh {} rpm -q {}".format(ip_r,soft_name)));
    elif c==10:
     soft_name=input("Enter the name of software or service: ")
     print(os.system("ssh {} dnf install {}".format(ip_r,soft_name)));
    elif c==12:
     ip_r=input("Enter your IP");
    elif c==11:
     os.system("ssh {} {}".format(ip_r,input("Enter the name of software : ")))
    elif c==13:
     os.system("ssh {} systemctl start {}".format(ip_r,input("Enter the name of service : ")))
    else:
     os.system("""echo "$(tput setaf 1) $(tput blink) WRONG CHOICE!!! $(tput sgr0) $(tput setaf 7)" """)
    input("Press Enter to continue...")
    os.system("clear")

if location!='a' or location!='b':
    input(os.system("""echo "$(tput setaf 1) $(tput blink) WRONG CHOICE!!! $(tput sgr0) $(tput setaf 7)" """))
    os.system("clear")

