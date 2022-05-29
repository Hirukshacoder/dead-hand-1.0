# Owner @TreveenHirukshaBastian
# copy rights are strictly avoided

# moudules
import itertools
import threading
import time
import sys

# banner
print("________                     .___   ___ ___                    .___  ____    _______") 
print("\______ \   ____ _____     __| _/  /   |   \_____    ____    __| _/ /_   |   \   _  \ ")   
print("|    |  \_/ __ \\__  \   / __ |    /    ~    \__  \  /    \  / __ |   |   |   /  /_\  \ ")  
print("|    `   \  ___/ / __ \_/ /_/ |   \    Y    // __ \|   |  \/ /_/ |   |   |   \  \_/   \ ") 
print("/_______  /\___  >____  /\___ |   \___|_  /(____  /___|  /\____ |   |___| /\ \_____  /")
print("        \/     \/     \/      \/         \/      \/     \/      \/         \/       \/")
print("")


print("")
print("")

# intro
print("Welcome to Dead Hand 1.0")

print("")

print("\rDead Hand is a dangerous malware |")


# virus
print("You are responsible for anything that happens to this computer \n ")
virus = input("Do you want to run the virus y/n: ")


if virus == 'y':

    done = False
    #here is the animation
    def animate():
      for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\r Instalizing dead hand 1.0 ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')

    t = threading.Thread(target=animate)
    t.start()

    #long process here
    time.sleep(10)
    done = True

    print("")
    print("")

    print("Dead Hand 1.0 is activated")
    print("Dead")
 
    from virus import *

else:
    print("virus is deactivated")