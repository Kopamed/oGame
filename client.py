import pygame as pg
from network import Network


width = 500
height = 500
win = pg.display.set_mode((width, height))
pg.display.set_caption("Client")

clientNumber = 0



class Player():
    def __init__(self, x,y,width,height,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3
        
        
    def draw(self, win):
        pg.draw.rect(win, self.color, self.rect)
        
    
    def move(self):
        keys = pg.key.get_pressed()
        
        
        if keys[pg.K_LEFT]:
            self.x-=self.vel
            
        if keys[pg.K_RIGHT]:
            self.x+=self.vel
            
        if keys[pg.K_UP]:
            self.y-=self.vel
            
        if keys[pg.K_DOWN]:
            self.y+=self.vel
            
        self.update()


    def update(self):
        self.rect = (self.x,self.y,self.width,self.height)


def read_pos(string):
    string = string.split(",")
    return int(string[0]), int(string[1])


def make_pos(tup):
    return str(tup[0])+","+str(tup[1])


def redrawWindow(win, player, player2):
    
    win.fill((255,255,255))
    player.draw(win)
    player2.draw(win)
    pg.display.update()
    
 
def main():
    
    run = True
    n = Network()
    startPos = read_pos(n.getPos())
    p = Player(startPos[0],startPos[1],100,100, (0,255,0))
    p2 = Player(0,0,100,100, (255,0,0))
    clock = pg.time.Clock()
    
    while run:
        clock.tick(60)
        p2Pos = read_pos(n.send(make_pos((p.x, p.y))))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2.update()
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.quit()
                
        p.move()
        redrawWindow(win, p, p2)
        
        
main()