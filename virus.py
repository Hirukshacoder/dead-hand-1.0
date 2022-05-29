import rotatescreen
import time
screen = rotatescreen.get_primary_display()
for a in range(1000):
    time.sleep(1)
    screen.rotate_to(a*90 % 360)