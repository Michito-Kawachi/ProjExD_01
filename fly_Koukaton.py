import pygame as pg
import sys

def main():
    pg.display.set_mode((1600, 900))
    back_img = pg.image.load("./fig/pg_bg.jpg")
    kt3_img = pg.image.load("./fig/3.png")
    kt3_img = pg.transform.flip(kt3_img, True, False)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
