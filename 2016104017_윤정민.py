import pygame
import random
import time
from datetime import datetime
import sys  


pygame.init()

size = [700, 600]
screen = pygame.display.set_mode(size)

title = '외계인 피하기 게임'
pygame.display.set_caption(title)


clock = pygame.time.Clock()

class obj:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.move = 0

    def put_img(self, address):
        if address[-3:] == "png":
            self.img = pygame.image.load(address).convert_alpha()
        else:
            self.img = pygame.image.load(address) 
            self.sx, self.sy = self.img.get_size()

    def change_size(self, sx, sy):
        self.img = pygame.transform.scale(self.img, (sx, sy))
        self.sx, self.sy = self.img.get_size()

    def show(self):
        screen.blit(self.img, (self.x, self.y))


def crash(a, b): 
    if (a.x - b.sx /2 <= b.x) and (b.x <= a.x + a.sx - b.sx/2):
        if (a.y - b.sy <= b.y) and (b.y <= a.y+a.sy-20):
            return True
        else:
            return False
    else:
        return False

def crash_big(a, b): 
    if (a.x +5 - b.sx /2 <= b.x) and (b.x <= a.x-5 + a.sx - b.sx/2):
        if (a.y + 5 - b.sy <= b.y) and (b.y <= a.y+a.sy-20):
            return True
        else:
            return False
    else:
        return False


ss = obj()
ss.put_img("ss.png")
ss.change_size(100, 130)
ss.x = round(size[0]/2) - round(ss.sx/2)
ss.y = size[1] - ss.sy - 15
ss.move = 15 


left_go = False
right_go = False
space_go = False

mp3_file = 'some.mp3'
pygame.mixer.init()
pygame.mixer.music.load(mp3_file)
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1) 

game_over = 0
score = 0

a_list = []
a_big_list = []
a_speed_list = []
  

smallfont = pygame.font.SysFont('Corbel',35)
  
color = (255,255,255)  
 
color_light = (170,170,170)  
  
color_dark = (100,100,100)  
  
 
text = smallfont.render('Quit' , True , color)  
text_level_1 = smallfont.render('LEVEL 1' , True , color) 
text_level_2 = smallfont.render('LEVEL 2' , True , color) 
text_level_3 = smallfont.render('LEVEL 3' , True , color) 

SB = 0
while SB == 0 :  
    clock.tick(60)
    for ev in pygame.event.get():  
          
        if ev.type == pygame.QUIT:  
            pygame.quit()  
              
         
        if ev.type == pygame.MOUSEBUTTONDOWN:  
            if size[0]/2-80 <= mouse[0] <= size[0]/2+100 and size[1]/4 <= mouse[1] <= size[1]/4+40:  
                SB = 1 

            if size[0]/2-80 <= mouse[0] <= size[0]/2+100 and size[1]/4+80 <= mouse[1] <= size[1]/4+120:  
                SB = 2
            
            if size[0]/2-80 <= mouse[0] <= size[0]/2+100 and size[1]/4 + 160<= mouse[1] <= size[1]/4+200:  
                SB = 3

            if size[0]/2-80 <= mouse[0] <= size[0]/2+100 and size[1]/4 + 250<= mouse[1] <= size[1]/4+290:  
                pygame.quit()
     
    background_menu = pygame.image.load("background_menu.png")  
    screen.blit(background_menu, (0, 0))

    mouse = pygame.mouse.get_pos()  
      
    if size[0]/2-80 <= mouse[0] <= size[0]/2+100 and size[1]/4 <= mouse[1] <= size[1]/4+40:  
        pygame.draw.rect(screen,color_light,[size[0]/2 - 80, size[1]/4, 180, 40])  
          
    else:  
        pygame.draw.rect(screen,color_dark,[size[0]/2 - 80,size[1]/4,180,40]) 

    if size[0]/2-80 <= mouse[0] <= size[0]/2+100 and size[1]/4 +80 <= mouse[1] <= size[1]/4+120:  
        pygame.draw.rect(screen,color_light,[size[0]/2 - 80,size[1]/4+80,180,40])  
          
    else:  
        pygame.draw.rect(screen,color_dark,[size[0]/2 - 80,size[1]/4+80,180,40]) 

    if size[0]/2-80 <= mouse[0] <= size[0]/2+100 and size[1]/4 + 160 <= mouse[1] <= size[1]/4 + 200:  
        pygame.draw.rect(screen,color_light,[size[0]/2 - 80,size[1]/4 + 160,180,40])  
          
    else:  
        pygame.draw.rect(screen,color_dark,[size[0]/2 - 80,size[1]/4 + 160,180,40])   
    
    if size[0]/2-80 <= mouse[0] <= size[0]/2+100 and size[1]/4 + 250 <= mouse[1] <= size[1]/4 + 290:  
        pygame.draw.rect(screen,color_light,[size[0]/2 - 80,size[1]/4 + 250 ,180,40])  
          
    else:  
        pygame.draw.rect(screen,color_dark,[size[0]/2 - 80,size[1]/4 + 250,180,40]) 
      
    screen.blit(text_level_1, (size[0]/2-45,size[1]/4))
    screen.blit(text_level_2 , (size[0]/2-45,size[1]/4+80))   
    screen.blit(text_level_3 , (size[0]/2-45,size[1]/4+160)) 
    screen.blit(text , (size[0]/2-20,size[1]/4+250)) 
 
    pygame.display.update()


start_time = datetime.now()
while SB == 1:
    clock.tick(100)  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            SB = 9 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left_go = True
            elif event.key == pygame.K_RIGHT: 
                right_go = True
            elif event.key == pygame.K_SPACE:
                space_go = True
                k = 0 

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_go = False
            elif event.key == pygame.K_RIGHT:
                right_go = False
            elif event.key == pygame.K_SPACE:
                space_go = False


    now_time = datetime.now()
    delta_time = round((now_time - start_time).total_seconds()) 

    if left_go == True:
        ss.x -= ss.move
        if ss.x <= 0:
            ss.x = 0

    elif right_go == True:
        ss.x += ss.move
        if ss.x >= size[0] - ss.sx:
            ss.x = size[0] - ss.sx 

    if random.random() > 0.6: 
        aa = obj()
        aa.put_img("enemy.png")
        aa.change_size(40, 40)
        aa.x = random.randrange(0,size[0]-aa.sx-round(ss.sx/2)) 
        aa.y = 10 
        aa.move = 20   
        a_list.append(aa)


    delete_list = []
    for i in range(len(a_list)):
        a = a_list[i]
        a.y += a.move 
        if a.y >= size[1]: 
            delete_list.append(i) 


    for i in range(len(a_list)):
        a = a_list[i]
        if crash(a, ss) == True:
            SB = 9  
            game_over = 9 
    

    background = pygame.image.load("background.png")  
    screen.blit(background, (0, 0))

    ss.show() 
    for a in a_list:
        a.show() 
    
    font = pygame.font.Font('C:/Windows/Fonts/calibrib.ttf', 20)
    text_Score = font.render('Score : {}'.format(delta_time), True, (255, 255, 255))
    screen.blit(text_Score, (size[0]-100, 5))

    pygame.display.flip()


start_time = datetime.now()
while SB == 2:
    clock.tick(100)  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            SB = 9 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left_go = True
            elif event.key == pygame.K_RIGHT: 
                right_go = True
            elif event.key == pygame.K_SPACE:
                space_go = True
                k = 0 

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_go = False
            elif event.key == pygame.K_RIGHT:
                right_go = False
            elif event.key == pygame.K_SPACE:
                space_go = False

    now_time = datetime.now()
    delta_time = round((now_time - start_time).total_seconds()) 

    if left_go == True:
        ss.x -= ss.move
        if ss.x <= 0:
            ss.x = 0

    elif right_go == True:
        ss.x += ss.move
        if ss.x >= size[0] - ss.sx:
            ss.x = size[0] - ss.sx 

    if random.random() > 0.7: 
        aa = obj()
        aa.put_img("enemy.png")
        aa.change_size(40, 40)
        aa.x = random.randrange(0,size[0]-aa.sx-round(ss.sx/2)) 
        aa.y = 10 
        aa.move = 20   
        a_list.append(aa)

    if random.random() > 0.95:
        aa_big = obj()
        aa_big.put_img("enemy.png")
        aa_big.change_size(130, 130)
        aa_big.x = random.randrange(0,size[0]-aa_big.sx-round(ss.sx/2)) 
        aa_big.y = 10
        aa_big.move = 10   
        a_big_list.append(aa_big)

    delete_list = []
    for i in range(len(a_list)):
        a = a_list[i]
        a.y += a.move 
        if a.y >= size[1]: 
            delete_list.append(i) 

    delete_big_list = []
    for i in range(len(a_big_list)):
        a = a_big_list[i]
        a.y += a.move
        if a.y >= size[1]: 
            delete_list.append(i) 


    for i in range(len(a_list)):
        a = a_list[i]
        if crash(a, ss) == True:
            SB = 9  
            game_over = 9 
    
    for i in range(len(a_big_list)):
        a_big = a_big_list[i]
        if crash_big(a_big, ss) == True:
            SB = 9 
            game_over = 9


    background = pygame.image.load("background.png")  
    screen.blit(background, (0, 0))
    ss.show() 

    for a in a_list:
        a.show()
    for a_big in a_big_list:
        a_big.show()


    font = pygame.font.Font('C:/Windows/Fonts/calibrib.ttf', 20)
    text_Score = font.render('Score : {}'.format(delta_time), True, (255, 255, 255))
    screen.blit(text_Score, (size[0]-100, 5))

    pygame.display.flip()


start_time = datetime.now()
while SB == 3:
    clock.tick(100)  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            SB = 9
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left_go = True
            elif event.key == pygame.K_RIGHT: 
                right_go = True
            elif event.key == pygame.K_SPACE:
                space_go = True
                k = 0 

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_go = False
            elif event.key == pygame.K_RIGHT:
                right_go = False
            elif event.key == pygame.K_SPACE:
                space_go = False


    now_time = datetime.now()
    delta_time = round((now_time - start_time).total_seconds())

    if left_go == True:
        ss.x -= ss.move
        if ss.x <= 0:
            ss.x = 0

    elif right_go == True:
        ss.x += ss.move
        if ss.x >= size[0] - ss.sx:
            ss.x = size[0] - ss.sx 


    if random.random() > 0.7: 
        aa = obj()
        aa.put_img("enemy.png")
        aa.change_size(40, 40)
        aa.x = random.randrange(0,size[0]-aa.sx-round(ss.sx/2)) 
        aa.y = 10 
        aa.move = 11   
        a_list.append(aa)


    if random.random() > 0.95:
        
        aa_big = obj()
        aa_big.put_img("enemy.png")
        aa_big.change_size(130, 130)
        aa_big.x = random.randrange(0,size[0]-aa_big.sx-round(ss.sx/2)) 
        aa_big.y = 10
        aa_big.move = 10   
        a_big_list.append(aa_big)


    if random.random() > 0.95:
        
        aa_speed = obj()
        aa_speed.put_img("enemy.png")
        aa_speed.change_size(20, 20)
        aa_speed.x = random.randrange(0,size[0]-aa_speed.sx-round(ss.sx/2)) 
        aa_speed.y = 10
        aa_speed.move = 25   
        a_speed_list.append(aa_speed)

    delete_list = []
    for i in range(len(a_list)):
        a = a_list[i]
        a.y += a.move 
        if a.y >= size[1]:
            delete_list.append(i) 

    delete_big_list = []
    for i in range(len(a_big_list)):
        a = a_big_list[i]
        a.y += a.move 
        if a.y >= size[1]: 
            delete_list.append(i) 

    delete_speed_list = []
    for i in range(len(a_speed_list)):
        a = a_speed_list[i]
        a.y += a.move 
        if a.y >= size[1]: 
            delete_list.append(i) 


    for i in range(len(a_list)):
        a = a_list[i]
        if crash(a, ss) == True:
            SB = 9  
            game_over = 9 

    for i in range(len(a_big_list)):
        a_big = a_big_list[i]
        if crash_big(a_big, ss) == True:
            SB = 9  
            game_over = 9 

    for i in range(len(a_speed_list)):
        a_speed = a_speed_list[i]
        if crash(a_speed, ss) == True:
            SB = 9  
            game_over = 9 


    background = pygame.image.load("background.png")  
    screen.blit(background, (0, 0))
    ss.show() 

    for a in a_list:
        a.show() 
    for a_big in a_big_list:
        a_big.show() 
    for a_speed in a_speed_list:
        a_speed.show() 


    font = pygame.font.Font('C:/Windows/Fonts/calibrib.ttf', 20) 
    text_Score = font.render('Score : {}'.format(delta_time), True, (255, 255, 255)) 
    screen.blit(text_Score, (size[0]-100, 5))

    pygame.display.flip()


while game_over == 9 : 
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = 0 

    font = pygame.font.Font('C:/Windows/Fonts/calibrib.ttf', 60) 
    text = font.render('Game Over', True, (255, 0, 0)) 
    screen.blit(text, (round(size[0]/2-130), round(size[1]/2-50)))
    pygame.display.flip()

pygame.quit()

