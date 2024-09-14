import arcade  # Импортировали аркаду

SCREEN_WIDTH = 800  # Константа ширины окна
SCREEN_HEIGHT = 600  # Константа высоты окна
SCREEN_TITLE = 'Арканоид'  # Заголовок окна


class Bar(arcade.Sprite):  # Класс ракетки
    def __init__(self):
        super().__init__('bar.png', 1.0)  # Передали картинку и масштаб


class Game(arcade.Window):  # создали класс
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bar = Bar()  # Отрисовали ракетку

    def on_draw(self):
        self.clear((255, 255, 255))  # По умолчанию окно чёрное, меняем на белое
        self.bar.draw()


if __name__ == '__main__':
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)  # создаём классоввую переменную (Передали параметры окна)
    arcade.run()  # Запускаем окно
