import arcade as ar
import random

# задаем ширину, высоту и заголовок окна
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Circle Game"
SIDES = ["left", "right", "top", "bottom"]


class Ball(ar.Sprite):
    def __init__(self, scale):
        super().__init__("circle.png", scale)
        self.side = random.choice(SIDES)
        if self.side == "left":
            self.right = 0
            self.center_y = random.randint(0, SCREEN_HEIGHT)
            self.change_x = random.uniform(2, 5)
            self.change_y = random.uniform(-3, 2)
        elif self.side == "top":
            self.bottom = window.height
            self.center_x = random.randint(0, window.width)
            self.change_x = random.uniform(-2, 2)
            self.change_y = random.uniform(-3, -2)
        elif self.side == "right":
            self.left = window.width
            self.center_y = random.randint(0, window.height)
            self.change_x = random.uniform(-3, -2)
            self.change_y = random.uniform(-3, 2)
        else:
            self.top = 0
            self.center_x = random.randint(0, window.width)
            self.change_y = random.uniform(2, 3)
            self.change_x = random.uniform(-2, 3)

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.side == "left":
            if self.left > window.width or self.bottom > window.height or self.top < 0:
                self.kill()
        if self.side == "right":
            if self.right < 0 or self.bottom > window.height or self.top < 0:
                self.kill()
        if self.side == "top":
            if self.right < 0 or self.left > window.width or self.top < 0:
                self.kill()
        if self.side == "bottom":
            if (
                self.right < 0
                or self.left > window.width
                or self.bottom > window.height
            ):
                self.kill()


class Player(Ball):
    def __init__(self):
        super().__init__(0.3)
        self.center_x = window.width / 2
        self.center_y = window.height / 2
        self.change_y = 0
        self.change_x = 0


class OurGame(ar.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, fullscreen=False)
        self.balls = ar.SpriteList()
        # self.sound=ar.load_sound("Drip Drop.wav")
        self.is_pause=False
        self.text=""

    def ball_append(self):
        ball = Ball(random.uniform(0.09, 0.7))
        ball.color = (
            random.randint(20, 250),
            random.randint(20, 250),
            random.randint(20, 250),
        )
        self.balls.append(ball)

    # начальные значения
    def setup(self):
        for _ in range(30):
            self.ball_append()
        self.player = Player()
        
        # self.music=ar.play_sound(self.sound)
        # self.sound.set_volume(0.3,self.music)
        

    # отрисовка объектов
    def on_draw(self):
        ar.start_render()
        self.balls.draw()
        self.player.draw()
        
        ar.draw_text( self.text, (window.width / 2) - 200, window.height / 2, ar.color.WHITE, 80)

    # логика
    def update(self, _):
        if self.is_pause==False:
            self.balls.update()
            self.player.update()
            while len(self.balls) < 30:
                self.ball_append()
            collisions=ar.check_for_collision_with_list(self.player,self.balls)
            for circle in collisions:
                if circle.scale>self.player.scale:
                    exit()
                else:
                    circle.kill()
                    self.player.scale+=0.03
                    
            if self.player.scale>=4:
                exit()   
            # if self.sound.get_stream_position(self.music)==0: 
                # self.music=ar.play_sound(self.sound)
                # self.sound.set_volume(0.3,self.music)
                    
            

    def on_mouse_motion(self, x: int, y: int, _: int, __: int):
        if self.is_pause==False:
            self.player.center_x = x
            self.player.center_y = y
    def on_mouse_press(self, x, y, button, modifiers):
        if self.is_pause:
            self.is_pause = False
            self.set_mouse_visible(False)
            self.text = ""
        else:
            self.is_pause = True
            self.set_mouse_visible(True)
            self.text = "Pause"
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol==ar.key.ESCAPE:
            window.close()        
window = OurGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
ar.run()
