import pyxel

# ウィンドウの高さと幅を作成
WINDOW_H = 120
WINDOW_W = 160
CAT_H = 16
CAT_W = 16

# 座標を決めるクラス
class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# 猫クラス
class cat:
    def __init__(self, img_id):
        self.pos = Vec2(0, 0)
        self.img_cat = img_id

    def update(self, x, y):
        self.pos.x = x
        self.pos.y = y

# 猫をマウスで動かすクラス
class App:
    def __init__(self):
        # イラストのID
        self.IMG_ID0 = 0
        self.IMG_ID1 = 1
        # イラストID0の描画位置
        self.IMG_ID0_X = 61
        self.IMG_ID0_Y = 66

        # 描画するウィンドウの作成
        pyxel.init(WINDOW_W, WINDOW_H, caption="Hello Pyxel")
        # 描画するイラストの指定(0~2までしか指定は出来ない)
        pyxel.image(0).load(0, 0, "assets/pyxel_logo_38x16.png")
        pyxel.image(1).load(0, 0, "assets/cat_16x16.png")
        # マウスの矢印を表示する
        # pyxel.mouse(True)
        # デフォルトがFalseのため明示する必要は無い
        # pyxel.mouse(False)

        # 猫
        self.mcat = cat(self.IMG_ID1)
        # 実施
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        # ====== ctrl cat(猫座標の更新、マウスに追従する仕様) ======
        self.mcat.update(pyxel.mouse_x, pyxel.mouse_y)

    def draw(self):
        pyxel.cls(0)
        pyxel.text(55, 41, "Hello, Pyxel!", pyxel.frame_count % 16)
        pyxel.blt(self.IMG_ID0_X, self.IMG_ID0_Y, 0, 0, 0, 38, 16)
        # 猫の描画
        pyxel.blt(self.mcat.pos.x, self.mcat.pos.y, self.mcat.img_cat, 0, 0, -CAT_W, CAT_H, 13)

App()
