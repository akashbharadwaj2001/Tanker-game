import math
import pygame
import random
import time
from pygame import mixer

pygame.init()
mixer.init()

#count variables
no_of_cannonball1 = 0
no_of_cannonball2 = 0
no_of_camps = 0

#tank variables
tank_x = 10
tank_y = 375
tank_x_change = 0
tank_direction = 'stop'

#angle of projection
angle = 45
angle_change = 0
angle_collission = 0

#cannonball variables
cannon_x = tank_x + 120
cannon_y = tank_y + 14
cannon_x_change = 0
cannon_y_collission = 0
cannon_state = 'ready'

#velocity of projection
velocity = 4.0
velocity_change = 0

#wall variables
wall_state = 'not present'
wall_x = 0
wall_y = 235
wall_collission_status = 'not collided'

#camp variables
camp_x = 0
camp_y = 402
camp_state = 'destroyed'

#display font
font_angle = pygame.font.Font('freesansbold.ttf',24)
font_velocity = pygame.font.Font('freesansbold.ttf',24)
font_cannonball = pygame.font.Font('freesansbold.ttf',24)
font_camp = pygame.font.Font('freesansbold.ttf',24)
font_player =  pygame.font.Font('freesansbold.ttf',30)
font_screen1 = pygame.font.Font('freesansbold.ttf',50)

#cannonball display
def cannon(x,y):
    screen.blit(pygame.image.load('cannonball.png'),(x,y))

#tank display
def tank(x,y):
    screen.blit(pygame.image.load('tank.png'),(x,y))

#angle display
def show_angle(angle):
    angle_display = font_angle.render('Angle: ' + str(angle) + ' degrees', True, (0,0,0))
    screen.blit(angle_display, (10,10))

#velocity display
def show_velocity(velocity):
    velocity_display = font_velocity.render('Velocity: ' + str(velocity) + ' units', True, (0,0,0))
    screen.blit(velocity_display, (300,10))

#no of cannonballs used display
def show_cannonball(no_of_cannonball):
    cannonball_display = font_cannonball.render('No of cannonball used: ' + str(no_of_cannonball1), True, (0,0,0))
    screen.blit(cannonball_display, (600,10))

#player no display
def show_player():
    player_display = font_player.render('PLAYER 1' , True, (250,0,0))
    screen.blit(player_display, (590,45))

#no of camps destroyed display
def show_camp(no_of_camps):
    camp_display = font_camp.render('camps destroyed: ' + str(no_of_camps) + '/10', True, (0,0,0))
    screen.blit(camp_display, (990,10))

#wall display
def wall():
    global wall_x, wall_y
    if wall_state == 'not present':
        wall_x = random.randint(250,1200)
    screen.blit(pygame.image.load('wall.png'),(wall_x,wall_y))

#checking collission of cannonball with wall
def wall_collission(cannon_x, cannon_y, wall_x):
    global wall_collission_status, cannon_y_collission, angle_collission, fire_angle, fire_velocity
    if wall_x - cannon_x < 9 and wall_x > cannon_x and cannon_y > 226:
        wall_collission_status = 'collided'
        cannon_y_collission = cannon_y
        angle_collission = math.atan(math.tan(fire_angle) - (cannon_x/((fire_velocity*math.cos(fire_angle))**2))/25)
        return True
    return False

#camp display
def camp():
    global camp_x, camp_y
    if camp_state == 'destroyed':
        camp_x = random.randint(wall_x + 50, 1300)
    screen.blit(pygame.image.load('camp.png'),(camp_x,camp_y))

#checking collission of cannonball with camp
def camp_collission(cannon_x, cannon_y, camp_x):
    if cannon_x - camp_x < 60 and cannon_x - camp_x > -7 and cannon_y > 393:
        return True
    return False

#blast image
def blast(camp_x, camp_y):
    screen.blit(pygame.image.load('blast.png'),(camp_x,camp_y))

#tanker sound
pygame.mixer.music.load('tanker.wav')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

#main game code

#prepare background     
screen = pygame.display.set_mode((1400,500))
pygame.display.set_caption('Tanker')
icon = pygame.image.load('tank icon.png')
pygame.display.set_icon(icon)
screen.fill((255,255,255))

#loop control variable for 4 screens
run1 = True
run2 = True
run3 = True
run4 = True
run5 = True

to_game1 = False
to_game2 = False

#player 1 screen
while run1:

    pygame.mixer.music.pause()
    screen = pygame.display.set_mode((1400,500))
    screen.fill((255,255,255))

    #input from keys
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run1 = False
            run2 = False
            run3 = False
            run4 = False
            run5 = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                to_game1 = True
                break
    
    #stop game
    if to_game1:
        break

    screen1_display = font_screen1.render('PLAYER 1', True, (250,0,0))
    screen.blit(screen1_display, (590,60))
    screen1_display = font_screen1.render('PRESS ENTER TO CONTINUE', True, (0,0,0))
    screen.blit(screen1_display, (380,130))
    instuctions = font_camp.render('"w" AND "s" TO CONTROL ANGLE', True, (0,0,0))
    screen.blit(instuctions, (500,210))
    instuctions = font_camp.render('UP AND DOWN KEYS TO CONTROL VELOCITY', True, (0,0,0))
    screen.blit(instuctions, (430,260))
    instuctions = font_camp.render('LEFT AND RIGHT KEYS TO MOVE TANKER', True, (0,0,0))
    screen.blit(instuctions, (450,310))
    instuctions = font_camp.render('SPACEBAR TO FIRE', True, (0,0,0))
    screen.blit(instuctions, (575,360))
    instuctions = font_camp.render('EACH PLAYER HAS TO DESTROY 10 CAMPS', True, (0,0,0))
    screen.blit(instuctions, (445,410))  
    instuctions = font_camp.render('PLAYER WITH LESS NO. OF CANNONBALLS USED WINS THE GAME', True, (0,0,0))
    screen.blit(instuctions, (300,460))
    
    pygame.display.update()
    

#game loop player 1
while run2:
    
    screen = pygame.display.set_mode((1400,500))
    screen.fill((255,255,255))

    #inputs from key
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run2 = False
            run3 = False
            run4 = False
            run5 = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if tank_direction == 'stop':
                    tank_x_change = -0.5
                    tank_direction = 'left'
                if tank_direction == 'right':
                    tank_x_change = 0
                    tank_direction = 'stop'

            if event.key == pygame.K_RIGHT:
                if tank_direction == 'stop':
                    tank_x_change = 0.5
                    tank_direction = 'right'
                if tank_direction == 'left':
                    tank_x_change = 0
                    tank_direction = 'stop'

            if event.key == pygame.K_w:
                angle_change = 1

            if event.key == pygame.K_s:
                angle_change = -1 

            if event.key == pygame.K_SPACE:
                if cannon_state == 'ready' and tank_direction == 'stop':     #fire only when cannonball is out of display and tanker is at rest
                    cannon_state = 'fire'
                    cannon_x_change = velocity * math.cos(angle_radians)     #horizontal velocity
                    fire_angle = angle_radians
                    fire_x_change = cannon_x_change                          #variable to store variables of motion so that path does 
                    fire_velocity = velocity                                 #not change abruptly during motion
                    
                    fire_sound = pygame.mixer.Sound('tankerfire.wav')
                    fire_sound.play()
                    time.sleep(0.5)                                          #to sync fire sound with ejection of cannonball

                    if velocity == 0:                                        #no motion and cannonball state is ready
                        cannon_state = 'ready'
                    no_of_cannonball1 +=1

            if event.key == pygame.K_UP:
                velocity_change = 0.1

            if event.key == pygame.K_DOWN:
                velocity_change = -0.1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                if tank_direction == 'right':
                    tank_x_change = 0.5
                if tank_direction == 'left':
                    tank_x_change = -0.5

            if event.key == pygame.K_w or event.key == pygame.K_s:
                angle_change = 0  

            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                velocity_change = 0

    #applying bounds to projection angle
    if angle > 89:
        angle = 89
    if angle < 0:
        angle = 0
    else:
        angle += angle_change
    
    angle_radians = math.pi * angle / 180.0               #change to radians
    
    #applying bounds to tanker
    if tank_x < 10:
        tank_x = 10
    if tank_x > wall_x - 160:
        tank_x = wall_x - 160
    else:                                                #move should not move during motio of cannonball
        if cannon_state == 'ready':
            tank_x += tank_x_change     

    #applying bounds to projection velocity
    if velocity > 10.0:
        velocity = 10.0
    if velocity < 0.0:
        velocity = 0
    else:
        velocity += velocity_change

    velocity = round(velocity, 1)                        

    #cannonball out of display
    if cannon_x > 1400 or cannon_y > 500 or cannon_state == 'ready':
        cannon_state = 'ready'
        wall_collission_status = 'not collided'
        cannon_x = tank_x + 120                                          #update position of cannonball back to tanker after motion
        cannon_y = tank_y + 14

    if cannon_state == 'fire':
        #equation of path when no collission occurs with wall
        if ((not wall_collission(cannon_x, cannon_y, wall_x)) and wall_collission_status == 'not collided'):
            cannon_x += fire_x_change
            cannon_y = (cannon_x-tank_x-120)*math.tan(fire_angle) - (((cannon_x-tank_x-120)**2)/((fire_velocity*math.cos(fire_angle))**2))/50
            cannon_y = tank_y + 14 - cannon_y
        #cannonball drops down when collission occurs
        else:
            cannon_x -= fire_x_change * math.cos(angle_collission)/4

            if angle_collission > math.pi/4:
                angle_collission = math.pi/2 - angle_collission
            if angle_collission < -math.pi/4:
                angle_collission = -math.pi/2 - angle_collission
            
            cannon_y = (((wall_x - cannon_x)/fire_velocity)**2)/0.6
            cannon_y = cannon_y + cannon_y_collission
        cannon(cannon_x, cannon_y)
    
    #collission with camp 
    if camp_collission(cannon_x, cannon_y, camp_x):    
        cannon_state = 'ready'                            
        wall_state = 'not present'
        camp_state = 'destroyed'
        tank_x = 10
        no_of_camps += 1
        
       
        fire_sound = pygame.mixer.Sound('destruction.wav')
        fire_sound.play()
            
        for i in range(500):
            blast(camp_x - 14, camp_y - 43)
            pygame.display.update(pygame.Rect(camp_x - 14, camp_y - 43, 113, 113))
                
    if no_of_camps == 10:
        break
    
    if tank_direction == 'stop':
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()    
    
    #create wall after destroying camp
    if wall_state == 'not present':
        wall()
        wall_state = 'present'

    #create camp again after destroying camp
    if camp_state == 'destroyed':
        camp()
        camp_state = 'present'

    #display objects
    tank(tank_x, tank_y)
    show_angle(angle)
    show_velocity(velocity)
    show_cannonball(no_of_cannonball1)
    show_camp(no_of_camps)
    show_player()
    wall()
    camp()

    pygame.display.update()


no_of_cannonball2 = 0
no_of_camps = 0

#tank variables
tank_x = 10
tank_y = 375
tank_x_change = 0

#angle of projection
angle = 45
angle_change = 0

#cannonball variables
cannon_x = tank_x + 120
cannon_y = tank_y + 14
cannon_x_change = 0
cannon_state = 'ready'

#velocity of projection
velocity = 4.0
velocity_change = 0

#wall variables
wall_state = 'not present'
wall_x = 0
wall_y = 235
wall_collission_status = 'not collided'

#camp variables
camp_x = 0
camp_y = 402
camp_state = 'destroyed'
#player 2 screen
while run3:

    pygame.mixer.music.pause()
    screen = pygame.display.set_mode((1400,500))
    screen.fill((255,255,255))

    #input from keys
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run3 = False
            run4 = False
            run5 = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                to_game2 = True
                break
    
    #start player 2
    if to_game2:
        break

    screen1_display = font_screen1.render('PLAYER 2', True, (250,0,0))
    screen.blit(screen1_display, (590,100))
    screen1_display = font_screen1.render('PRESS ENTER TO CONTINUE', True, (0,0,0))
    screen.blit(screen1_display, (380,170))
    instuctions = font_camp.render('"w" AND "s" TO CONTROL ANGLE', True, (0,0,0))
    screen.blit(instuctions, (500,275))
    instuctions = font_camp.render('UP AND DOWN KEYS TO CONTROL VELOCITY', True, (0,0,0))
    screen.blit(instuctions, (430,325))
    instuctions = font_camp.render('LEFT AND RIGHT KEYS TO MOVE TANKER', True, (0,0,0))
    screen.blit(instuctions, (450,375))
    instuctions = font_camp.render('SPACEBAR TO FIRE', True, (0,0,0))
    screen.blit(instuctions, (575,425))

    pygame.display.update()
    

#game loop player 2
while run4:
    
    screen = pygame.display.set_mode((1400,500))
    screen.fill((255,255,255))

    #inputs from key
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run4 = False
            run5 = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if tank_direction == 'stop':
                    tank_x_change = -0.5
                    tank_direction = 'left'
                if tank_direction == 'right':
                    tank_x_change = 0
                    tank_direction = 'stop'

            if event.key == pygame.K_RIGHT:
                if tank_direction == 'stop':
                    tank_x_change = 0.5
                    tank_direction = 'right'
                if tank_direction == 'left':
                    tank_x_change = 0
                    tank_direction = 'stop' 

            if event.key == pygame.K_w:
                angle_change = 1

            if event.key == pygame.K_s:
                angle_change = -1 

            if event.key == pygame.K_SPACE:
                if cannon_state == 'ready' and tank_direction == 'stop':     #fire only when cannonball is out of display
                    cannon_state = 'fire'
                    cannon_x_change = velocity * math.cos(angle_radians)     #horizontal velocity
                    fire_angle = angle_radians
                    fire_x_change = cannon_x_change                          #variable to store variables of motion so that path does 
                    fire_velocity = velocity 
                    
                    mixer.music.load('tankerfire.wav')
                    mixer.music.play()
                    time.sleep(0.5)                                
                    
                    if velocity == 0:                                        #no motion and cannonball state is ready
                        cannon_state = 'ready'
                    no_of_cannonball2 +=1

            if event.key == pygame.K_UP:
                velocity_change = 0.1

            if event.key == pygame.K_DOWN:
                velocity_change = -0.1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                if tank_direction == 'right':
                    tank_x_change = 0.5
                if tank_direction == 'left':
                    tank_x_change = -0.5

            if event.key == pygame.K_w or event.key == pygame.K_s:
                angle_change = 0  

            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                velocity_change = 0

    #applying bounds to projection angle
    if angle > 89:
        angle = 89
    if angle < 0:
        angle = 0
    else:
        angle += angle_change
    
    angle_radians = math.pi * angle / 180.0               #change to radians
    
    #applying bounds to tanker
    if tank_x < 10:
        tank_x = 10
    if tank_x > wall_x - 160:
        tank_x = wall_x - 160
    else:                                                #move should not move during motio of cannonball
        if cannon_state == 'ready':
            tank_x += tank_x_change     

    #applying bounds to projection velocity
    if velocity > 10.0:
        velocity = 10.0
    if velocity < 0.0:
        velocity = 0
    else:
        velocity += velocity_change

    velocity = round(velocity, 1)                        

    #cannonball out of display
    if cannon_x > 1400 or cannon_y > 500 or cannon_state == 'ready':
        cannon_state = 'ready'
        wall_collission_status = 'not collided'
        cannon_x = tank_x + 120                                          #update position of cannonball back to tanker after motion
        cannon_y = tank_y + 14

    if cannon_state == 'fire':
        #equation of path when no collission occurs with wall
        if ((not wall_collission(cannon_x, cannon_y, wall_x)) and wall_collission_status == 'not collided'):
            cannon_x += fire_x_change
            cannon_y = (cannon_x-tank_x-120)*math.tan(fire_angle) - (((cannon_x-tank_x-120)**2)/((fire_velocity*math.cos(fire_angle))**2))/50
            cannon_y = tank_y + 14 - cannon_y
        #cannonball drops down when collission occurs
        else:
            cannon_x -= fire_x_change * math.cos(angle_collission)/4

            if angle_collission > math.pi/4:
                angle_collission = math.pi/2 - angle_collission
            if angle_collission < -math.pi/4:
                angle_collission = -math.pi/2 - angle_collission
            
            cannon_y = (((wall_x - cannon_x)/fire_velocity)**2)/0.6
            cannon_y = cannon_y + cannon_y_collission
        cannon(cannon_x, cannon_y)
    
    #collission with camp 
    if camp_collission(cannon_x, cannon_y, camp_x):    
        cannon_state = 'ready'                            
        wall_state = 'not present'
        camp_state = 'destroyed'
        tank_x = 10
        no_of_camps += 1

        mixer.music.load('destruction.wav')
        mixer.music.play()


        for i in range(500):
            blast(camp_x - 14, camp_y - 43)
            pygame.display.update(pygame.Rect(camp_x - 14, camp_y - 43, 113, 113))
    
    if no_of_camps == 10:
        break

    if tank_direction == 'stop':
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()
    
    #create wall after destroying camp
    if wall_state == 'not present':
        wall()
        wall_state = 'present'

    #create camp again after destroying camp
    if camp_state == 'destroyed':
        camp()
        camp_state = 'present'

    #display objects
    tank(tank_x, tank_y)
    show_angle(angle)
    show_velocity(velocity)

    cannonball_display = font_cannonball.render('No of cannonball used: ' + str(no_of_cannonball2), True, (0,0,0))
    screen.blit(cannonball_display, (600,10))

    player_display = font_player.render('PLAYER 2' , True, (250,0,0))
    screen.blit(player_display, (590,45))

    player1_display = font_cannonball.render('Player 1 score: ' + str(no_of_cannonball1), True, (0,0,0))
    screen.blit(player1_display, (990,50))

    show_camp(no_of_camps)
    wall()
    camp()
    
    pygame.display.update()

while run5:

    pygame.mixer.music.pause()
    screen = pygame.display.set_mode((1400,500))
    screen.fill((255,255,255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run5 = False

    if no_of_cannonball1 > no_of_cannonball2:    
        screen1_display = font_screen1.render('PLAYER 2 WINS!', True, (250,0,0))
        screen.blit(screen1_display, (520,150))

    elif no_of_cannonball1 < no_of_cannonball2:
        screen1_display = font_screen1.render('PLAYER 1 WINS!', True, (250,0,0))
        screen.blit(screen1_display, (520,150))
    
    else:
        screen1_display = font_screen1.render('MATCH DRAWN!', True, (250,0,0))
        screen.blit(screen1_display, (520,150))

    player_a = font_player.render(f'PLAYER 1: {no_of_cannonball1}', True, (250,0,0))
    screen.blit(player_a, (600,240))

    player_b = font_player.render(f'PLAYER 2: {no_of_cannonball2}', True, (250,0,0))
    screen.blit(player_b, (600,290))

    pygame.display.update()
