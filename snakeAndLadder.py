import pygame,random,pyttsx3,time
pygame.init()
pygame.mixer.init()
sound1=pygame.mixer.Sound("ladder.wav")
sound2=pygame.mixer.Sound("snake.mp3")

engine = pyttsx3.init()
from pygame.constants import KEYDOWN, MOUSEBUTTONDOWN, QUIT
from pygame.surfarray import pixels_alpha
size = (600,450)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Moksha Patam") 
pic = pygame.image.load("game.jpg")
start_img = pygame.transform.scale(pygame.image.load("start_btn.png"),(200,150))
quit_img = pygame.transform.scale(pygame.image.load("quit_btn.png"),(100,100))
info_img = pygame.image.load("Button_Info_Icon_96.png")
playAgain_img = pygame.transform.scale(pygame.image.load("play again btn.png"),(150,50))
back_img = pygame.transform.scale(pygame.image.load("back btn.png"),(50,50))
info_Win_img = pygame.transform.scale(pygame.image.load("infoImg.jpeg"),(400,450))
pic1 = pygame.transform.scale(pic, (450, 450))
def reset():
    global x,gameOver,blackX,whiteX,blackY,whiteY,player1_row,player2_row,player
    x=0
    gameOver =False
    blackX,whiteX=185,185
    blackY,whiteY=400,400
    player1_row=1
    player2_row=1
    player=1

reset()






def set_text(string, coordx, coordy, fontSize): 

    font = pygame.font.Font('freesansbold.ttf', fontSize) 
    text = font.render(string, True, (0, 0, 0)) 
    textRect = text.get_rect()
    textRect.center = (coordx, coordy) 
    return (text, textRect)


 

    


def clickHere():
    global gameOver
    a = random.randint(0,100)
    b = random.randint(0,100)
    if a<b:
        a = str(b)
        b = str(a)
    else:
        a = str(a)
        b = str(b)
    c = random.sample(['+','-'],1)
    ans = eval(f"{a}{c[0]}{b}")
    print(ans)
    t =10
    uans=''

    clickHerePressed = True
    
    while clickHerePressed:

        
        #screen.fill((205, 205, 205))
        mainImage()
        goti()
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        totalText = set_text(timer, 80, 50, 30)
        screen.blit(totalText[0], totalText[1])

        totalText = set_text(f"{a}{c[0]}{b}=?", 80, 100, 20)
        screen.blit(totalText[0], totalText[1])

        totalText = set_text(f"{uans}", 80, 150, 25)
        screen.blit(totalText[0], totalText[1])

        pygame.display.update()
        time.sleep(1)
        if t>0:
            t -= 1
        else:
            timeTaken = t 
            clickHerePressed = False


        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    uans = int(uans)
                    #screen.fill((205,205,205))
                    mainImage()
                    timeTaken = t
                    t=0
                    if(ans == uans):
                        totalText = set_text(f"Correct answer", 75, 200, 20)
                        totalText1 = set_text(f"saved {timeTaken} second",75,230,20)
                        screen.blit(totalText[0], totalText[1])
                        screen.blit(totalText1[0],totalText1[1])
                    else:
                        totalText = set_text(f"Wrong Answer", 75, 200, 20)
                        timeTaken = 0
                        screen.blit(totalText[0], totalText[1])
                    goti()
                    time.sleep(2)
                    clickHerePressed = False
                    
                if event.key == pygame.K_0:
                    uans = uans+'0'
                if event.key == pygame.K_1:
                    uans = uans+'1'
                if event.key == pygame.K_2:
                    uans = uans+'2'
                if event.key == pygame.K_3:
                    uans = uans+'3'
                if event.key == pygame.K_4:
                    uans = uans+'4'
                if event.key == pygame.K_5:
                    uans = uans+'5'
                if event.key == pygame.K_6:
                    uans = uans+'6'
                if event.key == pygame.K_7:
                    uans = uans+'7'
                if event.key == pygame.K_8:
                    uans = uans+'8'
                if event.key == pygame.K_9:
                    uans = uans+'9'
                if event.key == pygame.K_BACKSPACE:
                    uans = uans[:-1]





    
    return timeTaken









def goti_position(guess):
    global gameOver,blackX,blackY,player1_row,player2_row,player,whiteX,whiteY
    i=1
    engine.say(guess)
    if(guess==0):
        if player:
            player = 0
        else:
            player = 1
    #print(guess)
    if player:

        while i<=guess:
            if i == 1:
                if blackX-77*guess<185 and player1_row == 6:
                    player=0
                    break
            if blackX<600 and player1_row%2!=0:    
                blackX+=77
            elif player1_row%2==0 and blackX>=185:
                blackX-=77
            if blackX>600 or blackX<=108:
                if player1_row+1!=7:
                    player1_row+=1
                blackY-=76
                if blackX>600:
                    blackX-=77
                else:
                    blackX+=77
            player=0
            i+=1
            mainImage()
            time.sleep(0.25)
            goti()
            if blackX==185 and player1_row==6:
                engine.say("Congratulations black won the game")
                #print("Game over black won")
                gameOver=True
                break
                
    else:    
        while i<=guess:
            if i==1:
                if whiteX-(77*guess)<185 and player2_row == 6:
                    player =1
                    break
            if whiteX<600 and player2_row%2!=0:    
                whiteX+=77
            elif player2_row%2==0 and whiteX>=185:
                whiteX-=77
            if whiteX>600 or whiteX<=108:  
                if player2_row+1!=7:
                    player2_row+=1
                whiteY-=76
                if whiteX>600:
                    whiteX-=77
                else:
                    whiteX+=77
            player=1
            i+=1
            mainImage()
            time.sleep(0.25)
            goti()
            if whiteX==185 and player2_row==6:
                engine.say("Congratulations white won the game")
                #print("Game over white won")
                gameOver = True
                break
def btns():
    global gameOver,blackX,blackY,player1_row,player2_row,player,whiteX,whiteY,startButton
    i=1
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_SPACE:
                guessTime=clickHere()
                goti_position(guessTime)
        if event.type== MOUSEBUTTONDOWN:
            x,y = event.pos
            
            if x>40 and x<90 and y>345 and y<390:
                guessTime=clickHere()
                goti_position(guessTime)
def mainImage():
    screen.fill((150,90,70))
    screen.blit(pic1,(150,0))

def luck():
    global gameOver,blackX,blackY,player1_row,player2_row,player,whiteX,whiteY,sound1,sound2
    
#black bad luck
    if (blackX == 262 and player1_row ==2) or(blackX == 185 and player1_row ==5):
        sound2.play()
        pygame.time.delay(50)
        blackX+=77
        blackY+=76
        player1_row-=1


    if (blackX == 493 and player1_row ==4) or(blackX == 493 and player1_row ==6):
        sound2.play()
        pygame.time.delay(50)
        blackX-=77
        blackY+=76
        player1_row-=1

#white bad luck
    if (whiteX == 262 and player2_row ==2) or (  whiteX == 185 and player2_row ==5):
        sound2.play()
        pygame.time.delay(50)
        whiteX+=77
        whiteY+=76
        player2_row-=1 

    if (whiteX == 493 and player2_row ==6)  or ( whiteX == 493 and player2_row ==4):
        sound2.play()
        pygame.time.delay(50)
        whiteX-=77
        whiteY+=76
        player2_row-=1

#black good luck
    if(blackX == 570 and player1_row == 1) or (blackX == 185 and player1_row == 2) or (blackX ==339 and player1_row == 3):
        sound1.play()
        blackY-=76*2
        player1_row+=2

#white good luck
    if(whiteX == 570 and player2_row == 1) or (whiteX == 185 and player2_row == 2) or (whiteX ==339 and player2_row == 3):
        sound1.play()
        whiteY-=76*2
        player2_row+=2




def goti():
    pygame.draw.line(screen,(200,200,200),(149,0),(149,500))
    pygame.draw.rect(screen,(0,200,255),pygame.Rect(35, 340, 60, 60),15)
    pygame.draw.rect(screen,(150,50,50),pygame.Rect(43,347,45,45))
    totalText = set_text("Click", 65, 360, 17)
    totalText1 = set_text("Here", 65, 380, 17)
    screen.blit(totalText[0], totalText[1])
    screen.blit(totalText1[0], totalText1[1])

    pygame.draw.circle(screen,(0,0,0),(blackX,blackY),(15))
    pygame.draw.circle(screen,(255,255,255),(whiteX,whiteY+25),(15))
    pygame.display.update()
    

class Button():
    def __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
    def draw(self):
        screen.blit(self.image,(self.rect.x,self.rect.y))

started = False
start_btn = Button(200,30,start_img)
info_btn =Button(250,150,info_img)
quit_btn = Button(250,260,quit_img)


def infoWindow():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if 0<x<50 and 0<y<50:
                    return    
        screen.fill((215,215,215))
        Button(0,0,back_img).draw()

        screen.blit(info_Win_img,(100,0))
        pygame.display.update()

def startWindowEvents():
    global started,gameOver,playedFirstTime
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            start_x,start_y = event.pos
                                                            
            if 220<start_x<=380 and 80<start_y<=130:        #for start button
                started = True 
                                                            
            if 250<start_x<350 and 265<start_y<360:         #for exit button

                exit()
                                                        
            if 260<start_x<340 and 150<start_y<240:         #for info window
                infoWindow()
            #print(start_x,start_y)    
        
playedFirstTime = True      

while not started:                                          #activity1
    startWindowEvents()
    screen.fill((215,215,215))
    start_btn.draw()
    info_btn.draw()
    quit_btn.draw()
    pygame.display.update()

def activity2():
    global gameOver,engine
    while not gameOver:
        mainImage()
        btns()
        goti()
        luck()

        engine.runAndWait()
if playedFirstTime == True:
    activity2()
    playedFirstTime = False
while not playedFirstTime:                                  #activity3
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
            #print(x,y)
            if 230<=x<=370 and 160<=y<=210:                 #play again
                gameOver =False
                reset()
                activity2()

    screen.fill((215,215,215))
    Button(230,160,playAgain_img).draw()                 
    pygame.display.update()
    
    



