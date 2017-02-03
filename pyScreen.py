import pygame
import datetime
import os

black    =    (   0,   0,   0)
white    =    ( 255, 255, 255)
green    =    (   0, 255,   0)
red      =    ( 255,   0,   0)
blue     =    (   0,   0, 255)
yellow   =    ( 255, 255,   0)

pygame.init()
pygame.mouse.set_visible(0)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
SW = 480
SH = 320

TextSize = 96


font = pygame.font.SysFont("Courier", TextSize)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            running = False

    now = datetime.datetime.now()
    date = ""
    time = ""
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    lit = days[datetime.datetime.today().weekday()] #months[now.month - 1]

    hourNumber = now.hour - 12 * (now.hour > 12)

    if now.month < 10 :
        if now.day < 10 :
            date  = "0" + str(now.month) + "/0" + str(now.day)
        else :
            date  = "0" + str(now.month) + "/" + str(now.day)
    else :
        if now.day < 10 :
            date  = str(now.month) + "/0" + str(now.day)
        else :
            date  = str(now.month) + "/" + str(now.day)

    if hourNumber < 10 :
        if now.minute < 10 :
            time  = "0" + str(hourNumber) + ":0" + str(now.minute)
        else :
            time  = "0" + str(hourNumber) + ":" + str(now.minute)
    else :
        if now.minute < 10 :
            time  = str(hourNumber) + ":0" + str(now.minute)
        else :
            time  = str(hourNumber) + ":" + str(now.minute)

    lLabel = font.render(lit,  1, white)
    lCords = []
    lCords.append(SW * 0.5 - lLabel.get_rect().width * 0.5)
    lCords.append((SH - lLabel.get_rect().height) * 0.5 - TextSize)

    dLabel = font.render(date,  1, white)
    dCords = []
    dCords.append(SW * 0.5 - dLabel.get_rect().width * 0.5)
    dCords.append((SH - dLabel.get_rect().height) * 0.5)

    tLabel = font.render(time,  1, white)
    tCords = []
    tCords.append(SW * 0.5 - tLabel.get_rect().width * 0.5)
    tCords.append((SH - tLabel.get_rect().height) * 0.5 + TextSize)

    screen.fill(black)
    screen.blit(dLabel, dCords)
    screen.blit(tLabel, tCords)
    screen.blit(lLabel, lCords)

    pygame.display.flip()
    pygame.time.delay(1000)

pygame.quit()
