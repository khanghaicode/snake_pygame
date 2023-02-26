import pygame,sys,random
from pygame.locals import *
pygame.init()
random.seed()
#sys var
scr_in4=pygame.display.Info()
scr_w,scr_h=scr_in4.current_w,scr_in4.current_h
score=0
screen=pygame.display.set_mode((scr_w,scr_h),pygame.FULLSCREEN)
pygame.display.set_caption("Snake game")
clock=pygame.time.Clock()
keypressing=False
pv_w=(scr_w*3//4)
pv_h=(scr_h*3//4)
pv_w-=pv_w%(scr_h//15)
pv_h-=pv_h%(scr_h//15)
pv_x=(scr_w-pv_w)//2
pv_y=(scr_h-pv_h)//2
tieudepos=10
try:
    font=pygame.font.Font("FVF Fernando 08.ttf",(pv_y//5))
except:
    font=pygame.font.SysFont("bahnschrift",(pv_y//5))
#fps=snake.speed
lose_mod=False
#rgb
white=(255,255,255)
black=(0,0,0)
blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)

class snake:
    size=scr_h//15
    pos_X=pv_x
    pos_Y=pv_y
    speed=8
    pos_X_change=0
    pos_Y_change=0
    direction="up"
    lis=[]
    head=[pos_X,pos_Y]
    leght=1
    default_color=blue
    color=blue
    eyecolor=white
    def update_pos():
        snake.pos_X+=snake.pos_X_change
        snake.pos_Y+=snake.pos_Y_change
        if snake.pos_X<pv_x:
            snake.pos_X=pv_x+pv_w-snake.size
        elif snake.pos_X>pv_x+pv_w-snake.size:
            snake.pos_X=pv_x
        if snake.pos_Y<pv_y:
            snake.pos_Y=pv_y+pv_h-snake.size
        elif snake.pos_Y>pv_y+pv_h-snake.size:
            snake.pos_Y=pv_y
    def update_list():
        snake.head=[]
        snake.head.append(snake.pos_X)
        snake.head.append(snake.pos_Y)
        snake.lis.append(snake.head)
        if len(snake.lis)>snake.leght:
            del snake.lis[0]
    def drawhead():
        if snake.direction=="up":
            pygame.draw.circle(screen,snake.eyecolor,(snake.pos_X+snake.size//3,snake.pos_Y+snake.size//3),snake.size//12)
            pygame.draw.circle(screen,snake.eyecolor,(snake.pos_X+snake.size*2//3,snake.pos_Y+snake.size//3),snake.size//12)
        elif snake.direction=="down":
            pygame.draw.circle(screen,snake.eyecolor,(snake.pos_X+snake.size//3,snake.pos_Y+snake.size*2//3),snake.size//12)
            pygame.draw.circle(screen,snake.eyecolor,(snake.pos_X+snake.size*2//3,snake.pos_Y+snake.size*2//3),snake.size//12)
        elif snake.direction=="right":
            pygame.draw.circle(screen,snake.eyecolor,(snake.pos_X+snake.size*2//3,snake.pos_Y+snake.size//3),snake.size//12)
            pygame.draw.circle(screen,snake.eyecolor,(snake.pos_X+snake.size*2//3,snake.pos_Y+snake.size*2//3),snake.size//12)
        elif snake.direction=="left":
            pygame.draw.circle(screen,snake.eyecolor,(snake.pos_X+snake.size//3,snake.pos_Y+snake.size//3),snake.size//12)
            pygame.draw.circle(screen,snake.eyecolor,(snake.pos_X+snake.size//3,snake.pos_Y+snake.size*2//3),snake.size//12)
    def draw():
        global keypressing
        for pos in snake.lis[1:-1]:
            pygame.draw.rect(screen, snake.color, (pos[0], pos[1], snake.size,snake.size))
            pygame.draw.rect(screen,white,(pos[0]+1,pos[1]+1,snake.size-1,snake.size-1),5)
        for pos in snake.lis[:-1]:
            if (abs(pos[0]-snake.lis[snake.lis.index(pos)+1][0])<=snake.size) and (abs(pos[1]-snake.lis[snake.lis.index(pos)+1][1])<=snake.size):
                pygame.draw.line(screen,white,(pos[0]+snake.size/2,pos[1]+snake.size/2),(snake.lis[snake.lis.index(pos)+1][0]+snake.size/2,snake.lis[snake.lis.index(pos)+1][1]+snake.size/2),snake.size//4)
        pygame.draw.rect(screen, snake.default_color, (snake.lis[-1][0], snake.lis[-1][1], snake.size,snake.size))
        pygame.draw.rect(screen,white,(snake.lis[-1][0]+1,snake.lis[-1][1]+1,snake.size-1,snake.size-1),5)
        snake.drawhead()
        keypressing=False
    def colhand(): 
        global lose_mod
        for part in snake.lis[:-4]:
            if part==snake.head:
                snake.color=red
                snake.eyecolor=red
                lose_mod=True
    def all():
        snake.update_pos()
        snake.update_list()
        snake.colhand()
        snake.draw()
class apple:
    pos_x=random.randrange(0,pv_w//snake.size)*snake.size+pv_x
    pos_y=random.randrange(0,pv_h//snake.size)*snake.size+pv_y
    color=red
    def draw():
        pygame.draw.rect(screen,apple.color,(apple.pos_x,apple.pos_y,snake.size,snake.size))
        pygame.draw.rect(screen,green,(apple.pos_x,apple.pos_y,snake.size,snake.size),5)
    def update_pos():
        apple.pos_x=random.randrange(0,pv_w//snake.size)*snake.size+pv_x
        apple.pos_y=random.randrange(0,pv_h//snake.size)*snake.size+pv_y
        for i in snake.lis:
            if(apple.pos_x==i[0] and apple.pos_y==i[1]):
                apple.update_pos()
class display:
    def drawline():
        pygame.draw.rect(screen,white,(pv_x,pv_y,pv_w,pv_h),5)
    def drawscore():
        screen.blit(font.render("Score: "+str(score),True,white),(pv_x,pv_y//4))
    def drawin4():
        global tieudepos
        screen.blit(font.render("Rắn săn MOI",True,white),(pv_x+pv_w*7/16,pv_y+pv_h))
        screen.blit(font.render("KHANGCIU",True,white),(pv_x+pv_w*29/64,pv_y*3/2+pv_h))
        tieudepos-=10
        if tieudepos<-scr_h*7/8:
            tieudepos=0
        screen.blit(font.render("Nhấn Esc để thoát|Khi thua nhấn P để chơi lại",True,white),(tieudepos,0))
        screen.blit(font.render("Nhấn Esc để thoát|Khi thua nhấn P để chơi lại",True,white),(tieudepos+scr_h*7/8,0))
        screen.blit(font.render("Nhấn Esc để thoát|Khi thua nhấn P để chơi lại",True,white),(tieudepos+scr_h*7/4,0))
        print(tieudepos)
    def all():
        display.drawline()
        display.drawscore()
        display.drawin4()
def pyquit():
    pygame.quit()
    sys.exit()
def snakeeatapple():
    if(snake.head[0]==apple.pos_x and snake.head[1]==apple.pos_y):
        global score
        score+=1
        snake.leght+=1
        apple.update_pos()
def reset():
    global snake,lose_mod,score
    snake.pos_X=pv_x
    snake.pos_Y=pv_y
    snake.speed=8
    snake.pos_X_change=0
    snake.pos_Y_change=0
    snake.direction="up"
    snake.lis=[]
    snake.head=[snake.pos_X,snake.pos_Y]
    snake.leght=1
    snake.color=blue
    lose_mod=False
    score=0
while True:
    while lose_mod:
        display.drawin4()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pyquit()
            elif event.type==pygame.KEYDOWN:
                if event.key==K_ESCAPE:
                    pyquit()
                if event.key==K_p:
                    reset()
    screen.fill(black)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pyquit()
        elif event.type==pygame.KEYDOWN:
            if event.key==K_ESCAPE:
                pyquit()
            elif event.key==K_UP and keypressing==False:
                if snake.pos_Y_change!=snake.size:
                    keypressing=True
                    snake.pos_Y_change=-snake.size
                    snake.pos_X_change=0
                    snake.direction="up"
            elif event.key==K_DOWN and keypressing==False:
                if snake.pos_Y_change!=-snake.size:
                    keypressing=True
                    snake.pos_Y_change=snake.size
                    snake.pos_X_change=0
                    snake.direction="down"
            elif event.key==K_LEFT and keypressing==False:
                if snake.pos_X_change!=snake.size:
                    keypressing=True
                    snake.pos_X_change=-snake.size
                    snake.pos_Y_change=0
                    snake.direction="left"
            elif event.key==K_RIGHT and keypressing==False:
                if snake.pos_X_change!=-snake.size:
                    keypressing=True
                    snake.pos_X_change=snake.size
                    snake.pos_Y_change=0
                    snake.direction="right"
            elif event.key==K_e:
                score+=1
                snake.leght+=1
            elif event.key==K_p:
                lose_mod=True
    snake.all()
    snakeeatapple()
    apple.draw()
    display.all()
    clock.tick(snake.speed)
    pygame.display.update()