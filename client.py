import pygame as pg
from network import Network
from player import Player

width = 500
height = 500
win = pg.display.set_mode((width, height))
pg.display.set_caption("Client")



def redrawWindow(win, player, player2):
    
    win.fill((255,255,255))
    player.draw(win)
    player2.draw(win)
    pg.display.update()
    
 
def main():
    
    run = True
    n = Network()
    p = n.getP() 
    clock = pg.time.Clock()
    
    while run:
        clock.tick(60)
        p2 = n.send(p)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.quit()
                
        p.move()
        redrawWindow(win, p, p2)
        
        
main()