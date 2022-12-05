import arcade


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GAME_RUNNING = 1
GAME_OVER = 2
SPRITE_SCALING_SCISSOR =.5
MOVEMENT_SPEED = 5

class IntroView(arcade.View):
    def on_show_view(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Use the arrow keys to move", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 150,
                         arcade.color.BLACK, font_size=36, anchor_x="center")
        arcade.draw_text("the scissors to cut the bread ", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100,
                         arcade.color.BLACK, font_size=36, anchor_x="center")
        arcade.draw_text("if you get hit by the mold you lose", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50,
                         arcade.color.BLACK, font_size=36, anchor_x="center")
        arcade.draw_text("try to cut as much of the", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.BLACK, font_size=36, anchor_x="center")
        arcade.draw_text("bread as possible", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 50,
                         arcade.color.BLACK, font_size=40, anchor_x="center")
        arcade.draw_text("Click to advance", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 225,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = Game()
        game_view.setup()
        self.window.show_view(game_view)

#mold sprite
class Mold (arcade.Sprite):

    def __init__(self, image, scale, bounce_sound):
        super().__init__(image,scale)
        self.bounce_sound = arcade.load_sound(bounce_sound)

    def update(self):
        ## bounce off sides
        if self.left <= 0 or self.right >= SCREEN_WIDTH:
            arcade.play_sound(self.bounce_sound)
            self.change_x *= -1.01

        elif self.bottom <=0 or self.top >= SCREEN_HEIGHT:
            arcade.play_sound(self.bounce_sound)
            self.change_y *= -1.01

        self.center_x += self.change_x
        super(Mold,self).update()



# class Scissor(arcade.Sprite)


# class Game(arcade.Window):
#     """ Main application class """
#
#     def __init__(self, width, height):
#         super().__init__(width, height)
#         # Background image will be stored in this variable
#         self.background = None
#         self.lolli = None
#         self.frame_count = 0
#         self.all_sprites_list = []
#         self.sound = None
#
#
#
#         # Do show the mouse cursor
#         self.set_mouse_visible(True)
#
#         # Set the background color
#         arcade.set_background_color(arcade.color.BLACK)
#
#     def setup(self):
#
#         self.background = arcade.load_texture("images/bread.jpg")
#         self.all_sprites_list = arcade.SpriteList()
#         self.sound = "./images/jump4.wav"
#         self.current_state = GAME_RUNNING
#
#         self.mold = Mold("images/lollipopRed.png", .75, ":resources:sounds/hit5.wav")
#
#         self.mold.center_x = SCREEN_WIDTH // 2
#         self.mold.center_y = SCREEN_HEIGHT // 2
#         self.mold.angle = 0
#         self.mold.change_x = 1
#         self.mold.change_y  = 1
#         self.all_sprites_list.append(self.mold)
#
#         self.sound = "./images/jump4.wav"
#
#
#
#     def on_draw(self):
#         """Render the screen. """
#         arcade.start_render()
#         self.draw_game()
#
#
#
#     def draw_game(self):
#
#         # Draw the background texture
#         arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
#                                       SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
#
#
#         self.lolli.draw()
#
#
#
#     def update(self, delta_time):
#         """All the logic to move, and the game logic goes here. """
#
#         self.frame_count += 1
#
#         self.lolli.update()
#
#
#
#
def main():
    """ Main method """
    # window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
    # window.setup()
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Breadwinner remake")
    intro_view = IntroView()
    window.show_view(intro_view)
    arcade.run()



main()
#
#
#
