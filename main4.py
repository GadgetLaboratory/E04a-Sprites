#!/usr/bin/env python3

import utils, os, random, time, open_color, arcade

utils.check_version((3,7))

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprites Example"


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        arcade.set_background_color(open_color.white)


    def setup(self):
        gems = ["ruby", "citrine", "topaz", "peridot", "emerald", "aquamarine", "sapphire", "amethyst", "opal", "tourmaline", "onyx", "diamond"]
        for i in range(100):
            gem = random.choice(gems)
            x = random.randint(50,750)
            y = random.randint(30,570)
            self.gemSprite = arcade.Sprite("assets/{gem}.png".format(gem=gem), 0.5)
            self.gemSprite.center_x = x
            self.gemSprite.center_y = y
            self.gemList.append(self.gemSprite)        

    def on_draw(self):
        arcade.start_render()
        self.gemList.draw()

    def on_mouse_press(self, x, y):
        if x and y in self.gemSprite:
            del self

    def update(self, delta_time):
        pass


    def on_mouse_motion(self, x, y, dx, dy):
        xChange = dx - x
        yChange = dy - y
        self.gemSprite.center_x += xChange
        self.gemSprite.center_y += yChange

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()