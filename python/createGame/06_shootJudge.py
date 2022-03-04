from xmlrpc.server import DocXMLRPCRequestHandler
import pyxel

# ウィンドウの高さと幅を作成
WINDOW_H = 120
WINDOW_W = 160
CAT_H = 16
CAT_W = 16
ENEMY_H = 12
ENEMY_W = 12

# 座標を決めるクラス
class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# 猫クラス
class Cat:
    def __init__(self, img_id):
        self.pos = Vec2(0, 0)
        self.img_cat = img_id
        # 猫の向きを決めるための変数
        self.vec = 0

    def update(self, x, y, dx):
        self.pos.x = x
        self.pos.y = y
        # 猫の向きを更新する
        self.vec = dx

# ボールクラス
class Ball:
        def __init__(self):
            self.pos = Vec2(0, 0)
            self.vec = 0
            self.size = 2
            self.speed = 3
            self.color = 10

        def update(self, x, y, dx, size, color):
            self.pos.x = x
            self.pos.y = y
            self.vec = dx
            self.size = size
            self.color = color

# 敵クラス
class Enemy:
    def __init__(self, img_id):
        self.pos = Vec2(0, 0)
        self.vec = 0
        self.speed = 0.02
        self.img_enemy = img_id

    def update(self, x, y, dx):
        self.pos.x = x
        self.pos.y = y
        self.vec = dx

# 猫をマウスで動かすクラス
class App:
    def __init__(self):
        # イラストのID
        self.IMG_ID0 = 0
        self.IMG_ID1 = 1
        self.IMG_ID2 = 2
        # イラストID0の描画位置
        self.IMG_ID0_X = 61
        self.IMG_ID0_Y = 66


        # 描画するウィンドウの作成
        pyxel.init(WINDOW_W, WINDOW_H, caption="Hello Pyxel")
        # 描画するイラストの指定(0~2までしか指定は出来ない)
        pyxel.image(0).load(0, 0, "assets/pyxel_logo_38x16.png")
        pyxel.image(1).load(0, 0, "assets/cat_16x16.png")
        pyxel.image(self.IMG_ID2).load(0, 0, "assets/animal_mouse.png")
        # マウスの矢印を表示する
        # pyxel.mouse(True)
        # デフォルトがFalseのため明示する必要は無い
        # pyxel.mouse(False)

        # 猫
        self.mcat = Cat(self.IMG_ID1)
        # ボール(クリックしたときにインスタンスを生成し、リストに格納していく形にする)
        self.Balls = []
        # 敵
        self.Enemies = []
        # フラグ
        self.flag = 1
        self.GameOver_flag = 0

        # 実施
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        # ====== ctrl cat(猫座標の更新、マウスに追従する仕様) ======
        # x軸方向の移動量(マウス座標 - cat座標)
        dx = pyxel.mouse_x - self.mcat.pos.x
        # y軸方向の移動量(マウス座標 - cat座標)
        dy = pyxel.mouse_y - self.mcat.pos.y

        # もしxの移動量が0で無ければマウスが動いているため、猫の座標と向きを更新
        if dx != 0:
            self.mcat.update(pyxel.mouse_x, pyxel.mouse_y, dx)
        # dyが0で無ければ(マウスが真上or真下に移動)猫の座標のみを更新
        elif dy != 0:
            self.mcat.update(pyxel.mouse_x, pyxel.mouse_y, self.mcat.vec)

        # ====== ctrl enemy(敵座標の更新、4匹の敵キャラを実体化) ======
        if self.flag == 1:
            new_enemy = Enemy(self.IMG_ID2)
            new_enemy.update(WINDOW_W/2, WINDOW_H/2 + 30, self.mcat.vec)
            self.Enemies.append(new_enemy)

            new_enemy = Enemy(self.IMG_ID2)
            new_enemy.update(WINDOW_W/2 + 30, WINDOW_H/2 + 30, self.mcat.vec)
            self.Enemies.append(new_enemy)

            new_enemy = Enemy(self.IMG_ID2)
            new_enemy.update(WINDOW_W/2 - 30, WINDOW_H/2 + 30, self.mcat.vec)
            self.Enemies.append(new_enemy)

            new_enemy = Enemy(self.IMG_ID2)
            new_enemy.update(WINDOW_W/2 - 60, WINDOW_H/2 + 30, self.mcat.vec)
            self.Enemies.append(new_enemy)

            self.flag = 0

        enemy_count = len(self.Enemies)

        # 当たり判定(敵キャラと猫)
        for i in range(enemy_count):
            if ((self.mcat.pos.x < self.Enemies[i].pos.x < ENEMY_W) 
                and (self.Enemies[i].pos.x + ENEMY_W < self.mcat.pos.x + CAT_W)
                and (self.mcat.pos.y < self.Enemies[i].pos.y + ENEMY_H)
                and (self.Enemies[i].pos.y + ENEMY_H < self.mcat.pos.y + CAT_H)
                or (self.mcat.pos.x < self.Enemies[i].pos.x)
                and (self.Enemies[i].pos.x < self.mcat.pos.x + CAT_W)
                and (self.mcat.pos.y < self.Enemies[i].pos.y + ENEMY_H)
                and (self.Enemies[i].pos.y + ENEMY_H < self.mcat.pos.y + CAT_H)
                or (self.mcat.pos.x < self.Enemies[i].pos.x + ENEMY_W)
                and (self.Enemies[i].pos.x + ENEMY_W < self.mcat.pos.x + CAT_W)
                and (self.mcat.pos.y < self.Enemies[i].pos.y)
                and (self.Enemies[i].pos.y < self.mcat.pos.y + CAT_H)
                or (self.mcat.pos.x < self.Enemies[i].pos.x)
                and (self.Enemies[i].pos.x < self.mcat.pos.x + CAT_W)
                and (self.Enemies[i].pos.y < self.Enemies[i].pos.y)
                and (self.Enemies[i].pos.y < self.mcat.pos.y + CAT_H)):
                # GameOverフラグを立てる
                self.GameOver_flag = 1

        # ====== ctrl Ball(ボールを作成する処理) ======
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            new_ball = Ball()
            # 猫が右向きの場合、右横に作成
            if self.mcat.vec > 0:
                new_ball.update(self.mcat.pos.x + CAT_W/2 + 6, self.mcat.pos.y + CAT_H/2, self.mcat.vec, new_ball.size, new_ball.color)
            # 左向きの場合、左横に作成
            else:
                new_ball.update(self.mcat.pos.x + CAT_W/2 - 6, self.mcat.pos.y + CAT_H/2, self.mcat.vec, new_ball.size, new_ball.color)
            self.Balls.append(new_ball)

        # ボール数をカウント
        ball_count = len(self.Balls)
        # 全てのボールが消滅するまで繰り返す
        for i in range(ball_count):
            # ボールが画面内に存在するか確認
            if 0 < self.Balls[i].pos.x and self.Balls[i].pos.x < WINDOW_W:
                # 右向きの場合、右(プラス方向)にスピード変数分進んでいく
                if self.Balls[i].vec > 0:
                    self.Balls[i].update(self.Balls[i].pos.x + self.Balls[i].speed, self.Balls[i].pos.y, self.Balls[i].vec, self.Balls[i].size, self.Balls[i].color)
                # 左向きの場合、左(マイナス方向)にスピード変数分進んでいく
                else:
                    self.Balls[i].update(self.Balls[i].pos.x - self.Balls[i].speed, self.Balls[i].pos.y, self.Balls[i].vec, self.Balls[i].size, self.Balls[i].color)
            else:
                del self.Balls[i]
                break


    def draw(self):
        pyxel.cls(0)
        pyxel.text(55, 41, "Hello, Pyxel!", pyxel.frame_count % 16)
        pyxel.blt(self.IMG_ID0_X, self.IMG_ID0_Y, 0, 0, 0, 38, 16)

        # 猫の描画(向きまで考慮)
        # もし移動量が0より大きければ右向き
        if self.mcat.vec > 0:
            pyxel.blt(self.mcat.pos.x, self.mcat.pos.y, self.mcat.img_cat, 0, 0, -CAT_W, CAT_H, 13)
        # もし移動量が0より小さければ右向き
        else:
            pyxel.blt(self.mcat.pos.x, self.mcat.pos.y, self.mcat.img_cat, 0, 0, CAT_W, CAT_H, 13)            

        # ボールの描画
        for ball in self.Balls:
            pyxel.circ(ball.pos.x, ball.pos.y, ball.size, ball.color)

App()
