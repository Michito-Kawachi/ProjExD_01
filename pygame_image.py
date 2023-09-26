import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    tmr = 0
    #問2
    kt3_img = pg.image.load("ex01/fig/3.png")
    kt3_img = pg.transform.flip(kt3_img, True, False)
    #問3
    img_lst = []
    for i in range(10):
        img_lst.append(pg.transform.rotozoom(kt3_img, i, 1.0))
    for i in range(10, -1, -1):
        img_lst.append(pg.transform.rotozoom(kt3_img, i, 1.0))
    

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        #問6 
        screen.blit(bg_img, [-tmr, 0])
        screen.blit(bg_img, [1600-tmr, 0])
        if tmr >= 1599:
            tmr = 0
        #問5
        n = tmr % 20
        screen.blit(img_lst[n], [300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()