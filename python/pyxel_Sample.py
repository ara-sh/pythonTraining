import pyxel

class App:
    def __init__(self):
        # 初期化
        pyxel.init(160, 120)
        self.x = 0
        
        # 画像の読み込み (※1)
        pyxel.image(0).load(0, 0, "cat.png")
        
        # 実行
        pyxel.run(self.update, self.draw)

    def update(self):
        # 更新
        self.x = (self.x + 1) % pyxel.width

    def draw(self):
        # 描画
        # 画面を消去
        pyxel.cls(0)
        # 矩形を描画
        pyxel.rect(self.x, 0, self.x + 7, 7, 9)
        
        # ニャンコをマウスカーソルに追従させる (※2)
        px = pyxel.mouse_x # マウスのX座標
        py = pyxel.mouse_y # マウスのY座標
        image_no = 0       # 画像の番号
        u = 0              # 切り出しの左側
        v = 0              # 切り出しの上側
        w = 16             # 切り出す幅
        h = 16             # 切り出す高さ
        pyxel.blt(px, py, image_no, u, v, w, h, 5)

App()