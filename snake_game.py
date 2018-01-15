import pygame
import random
pygame.init()
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
display_width=800
display_height=600
gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Slither')
pygame.display.update()

font = pygame.font.SysFont(None,25)
clock=pygame.time.Clock()
def snake(block_size, snakelist):
    for XnY in snakelist:
        pygame.draw.rect(gameDisplay,black,[XnY[0],XnY[1],block_size,block_size])
def message_to_screen(msg,color):
    screen_text=font.render(msg,True,color)
    gameDisplay.blit(screen_text,[display_width/2,display_height/2])
def gameLoop():
    lead_x=display_width/2
    lead_y=display_height/2
    lead_x_change=0
    lead_y_change=0
    block_size=10
    FPS=30
    
    snakelist=[]
    gameExit=False
    gameOver=False
    snakeLength=1
    RandAppleX=random.randrange(0,display_width-block_size,10)
    RandAppleY=random.randrange(0,display_height-block_size,10)
    while not gameExit:
        while gameOver:
            gameDisplay.fill(white)
            message_to_screen("Game Over, Press C to play again and Q to quit",red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        gameOver=False
                        gameExit=True
                    elif event.key==pygame.K_c:
                        gameLoop()
        for evet in pygame.event.get():
            if evet.type==pygame.QUIT:
                gameExit=True
                
            if evet.type==pygame.KEYDOWN:
                if evet.key==pygame.K_LEFT:
                    lead_x_change=-block_size
                    lead_y_change=0
                if evet.key==pygame.K_RIGHT:
                    lead_x_change=block_size
                    lead_y_change=0
                if evet.key==pygame.K_DOWN:
                    lead_y_change=block_size
                    lead_x_change=0
                if evet.key==pygame.K_UP:
                    lead_y_change=-block_size
                    lead_x_change=0
        gameDisplay.fill(white)
        lead_x+=lead_x_change
        lead_y+=lead_y_change
        snakeHead=[]
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakelist.append(snakeHead)
        if len(snakelist)>snakeLength:
            del snakelist[0]
        for eachsegment in snakelist[:-1]:
            if eachsegment == snakeHead:
                gameOver=True
        snake(block_size,snakelist)
        pygame.draw.rect(gameDisplay,red,[RandAppleX,RandAppleY,block_size,block_size])
        if RandAppleX==lead_x and RandAppleY==lead_y:
            RandAppleX=random.randrange(0,display_width-block_size,10)
            RandAppleY=random.randrange(0,display_height-block_size,10)
            snakeLength+=1
        if lead_x>=display_width or lead_x<0 or lead_y>=display_height or lead_y<0:
            gameOver=True
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()
gameLoop()
