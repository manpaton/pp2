import pygame
import sys
import math
from datetime import datetime

pygame.init()

cl_img = pygame.image.load("mickeyclock.jpeg")
cl_img = pygame.transform.scale(cl_img, (int(cl_img.get_width() * 0.6), int(cl_img.get_height() * 0.6)))
cl_rc = cl_img.get_rect()


wd, ht = cl_rc.width, cl_rc.height
sc = pygame.display.set_mode((wd, ht), pygame.RESIZABLE)
pygame.display.set_caption("clock")

# центр
ct = (wd // 2, ht // 2)

def dr_hd(ang, ln, col, thk):
    end_x = ct[0] + ln * math.cos(math.radians(-ang))
    end_y = ct[1] - ln * math.sin(math.radians(-ang))
    pygame.draw.line(sc, col, ct, (end_x, end_y), thk)

rn = True
while rn:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            rn = False
    
    sc.fill((255, 255, 255))
    sc.blit(cl_img, (0, 0))

    now = datetime.now()
    hour = now.hour % 12
    min = now.minute
    sec = now.second

    hour_ang = -90 + (hour * 30) + (min * 0.5)
    min_ang = -90 + (min * 6)
    sec_ang = -90 + (sec * 6)

    # Draw hands with adjusted lengths
    dr_hd(hour_ang, ht // 5.5, (0, 0, 0), 8)
    dr_hd(min_ang, ht // 4, (0, 0, 0), 6)
    dr_hd(sec_ang, ht // 3.5, (255, 0, 0), 3)

    pygame.display.flip()

pygame.quit()
sys.exit()
