import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    tmr = 0
    #問2
    kt3_img = pg.image.load("./fig/3.png")
    kt3_img = pg.transform.flip(kt3_img, True, False)
    #問3
    kt3_img_rotate = pg.transform.rotate(kt3_img, 10)
    img_lst = [kt3_img, kt3_img_rotate]
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0])
        pg.display.update()
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()