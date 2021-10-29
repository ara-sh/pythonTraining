import pyxel

# ウィンドウの高さと幅を作成
WINDOW_H = 120
WINDOW_W = 160
CAT_H = 16
CAT_W = 16

# 猫をマウスで動かすクラス
class App:
    def __init__(self):
        # 描画するウィンドウの作成
        pyxel.init(WINDOW_W, WINDOW_H, caption="Hello Pyxel")
        # 描画するイラストの指定(0~2までしか指定は出来ない)
        pyxel.image(0).load(0, 0, "assets/pyxel_logo_38x16.png")
        pyxel.image(1).load(0, 0, "assets/cat_16x16.png")
        # マウスの矢印を表示する
        # pyxel.mouse(True)
        # デフォルトがFalseのため明示する必要は無い
        # pyxel.mouse(False)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(55, 41, "Hello, Pyxel!", pyxel.frame_count % 16)
        pyxel.blt(61, 66, 0, 0, 0, 38, 16)
        # 猫を動かすメソッドの呼び出し
        self.cat()

    def cat(self):
        # マウスの位置を変数に格納
        x = pyxel.mouse_x
        y = pyxel.mouse_y
        # 指定イラストの選択
        img = 1
        # 指定イラストの領域始点位置
        u = 0
        v = 0
        # 透過したい色
        colkey = 13
        # 左クリックを押している間画像の向きを反転させる処理
        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
            pyxel.blt(x, y, img, u, v, -CAT_W, CAT_H, colkey)
        else:
            pyxel.blt(x, y, img, u, v, CAT_W, CAT_H, colkey)

App()
