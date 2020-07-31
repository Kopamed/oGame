import pygame as pg


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