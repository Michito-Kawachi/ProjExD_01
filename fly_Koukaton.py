import pygame as pg
import sys

def main():
    pg.display.set_mode((1600, 900))
    #問1
    back_img = pg.image.load("./fig/pg_bg.jpg")
    #問2
    kt3_img = pg.image.load("./fig/3.png")
    kt3_img = pg.transform.flip(kt3_img, True, False)
    #問3
    kt3_img_rotate = pg.transform.rotate(kt3_img, 10)
    img_lst = [kt3_img, kt3_img_rotate]

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
