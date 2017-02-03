import pygame
import datetime
import socket
import os

black    =    (   0,   0,   0)
white    =    ( 255, 255, 255)
green    =    (   0, 255,   0)
red      =    ( 255,   0,   0)
blue     =    (   0,   0, 255)
yellow   =    ( 255, 255,   0)

# The mouse and toolbars are unnecessary, so the settings are as follows
pygame.init()
pygame.mouse.set_visible(0)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
SW = 480 # raspberry pi has a 480 pixel wide screen
SH = 320 # raspberry pi has a 320 pixel tall screen

# An equal space font with approprate font size for the screen
TextSize = 96
font = pygame.font.SysFont("Courier", TextSize)

screenMode = "Date/Time"; # The mode of the clock. Currently supports a date/time mode, as well as an IP Address mode

# Shows the date and time, with the colon blinking every second
def dateTimeMode(blink) :
    now = datetime.datetime.now()
    date = ""
    time = ""
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    lit = days[datetime.datetime.today().weekday()] # months[now.month - 1]

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

    colon = ":"
    if blink :
        colon = " "
       
    if hourNumber < 10 :
        if now.minute < 10 :
            time  = "0" + str(hourNumber) + colon + "0" + str(now.minute)
        else :
            time  = "0" + str(hourNumber) + colon + str(now.minute)
    else :
        if now.minute < 10 :
            time  = str(hourNumber) + colon + "0" + str(now.minute)
        else :
            time  = str(hourNumber) + colon + str(now.minute)

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


# Get's the ip address of the current ethernet connection
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

# Shows the IP Address, if possible, of the raspberry pi
def IPAddressMode() :
    try :
        address = get_ip_address().split('.');
    except Exception :
        address = ['Critical', ' ', 'Failure', ' ']

    address1Label = font.render('Server',  1, white)
    address1Cords = []
    address1Cords.append(SW * 0.5 - address1Label.get_rect().width * 0.5)
    address1Cords.append((SH - address1Label.get_rect().height) * 0.5 - TextSize)

    address2Label = font.render(address[0] + '.' + address[1],  1, white)
    address2Cords = []
    address2Cords.append(SW * 0.5 - address2Label.get_rect().width * 0.5)
    address2Cords.append((SH - address2Label.get_rect().height) * 0.5)

    address3Label = font.render(address[2] + '.' + address[3],  1, white)
    address3Cords = []
    address3Cords.append(SW * 0.5 - address3Label.get_rect().width * 0.5)
    address3Cords.append((SH - address3Label.get_rect().height) * 0.5 + TextSize)

    screen.fill(black)
    screen.blit(address1Label, address1Cords)
    screen.blit(address2Label, address2Cords)
    screen.blit(address3Label, address3Cords)

    pygame.display.flip()
    pygame.time.delay(2500)



cycleLength = 10 # The number of seconds before the screen quickly shows the IP Address screen
cycleCount  = 0  # The counter used for timing this automatic cycle
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if screenMode == "Date/Time" :
                screenMode = "IPAddress"
            else :
                running = False

    
    if screenMode == "IPAddress" or cycleCount > cycleLength :
        IPAddressMode()
        cycleCount = 0
    else :
        dateTimeMode(cycleCount % 2)
    cycleCount += 1
    

pygame.quit()
