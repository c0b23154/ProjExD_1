import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")     #背景画像「pg_bg.jpg」（画像サイズ：幅1600 高さ900）を読み込み，Surfaceを生成せよ．
    k3_img = pg.image.load("fig/3.png")     #こうかとん画像「3.png」を読み込み，Surfaceを生成せよ．
    k3_img = pg.transform.flip(k3_img, True, False)   #そして，左右を反転せよ．
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0])    #背景画像を表示せよ．
        #横300，縦200の位置に，こうかとんSurfaceをblitせよ．
        k3_rct = k3_img.get_rect()  #画像Surfaceに対応する画像Rectを取得する
        k3_rct.center = 300, 200    
        screen.blit(k3_img, k3_rct)     #画像SurfaceをスクリーンSurfaceにRectに従って貼り付ける
        pg.display.update()
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()