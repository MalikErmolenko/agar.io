import arcade as ar 

 # задаем ширину, высоту и заголовок окна
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Circle Game"

class OurGame(ar.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

# начальные значения
    def setup(self):
        pass

    # отрисовка объектов
    def on_draw(self):
        ar.start_render()

    # логика
    def update(self, delta_time):
        pass


window = OurGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
ar.run()
