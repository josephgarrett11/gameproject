import arcade
import random


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GAME_RUNNING = 1
GAME_OVER = 2
SPRITE_SCALING_SCISSOR =.2
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
        arcade.draw_text("try to last as", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.BLACK, font_size=36, anchor_x="center")
        arcade.draw_text("long as you can", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 50,
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
            self.change_x *= -1.1

        elif self.bottom <=0 or self.top >= SCREEN_HEIGHT:
            arcade.play_sound(self.bounce_sound)
            self.change_y *= -1.1

        self.center_x += self.change_x
        super(Mold,self).update()



class Scissor(arcade.Sprite):
    def update(self):
        ## bounce off sides
        if self.left <= 0:
          self.center_x=30


        elif self.bottom <= 0:
            self.center_y=30

        elif self.top >=SCREEN_HEIGHT:
            self.center_y=SCREEN_HEIGHT-30


        elif self.right >=SCREEN_WIDTH:
            self.center_x=SCREEN_WIDTH-30


        super().update()

class Game(arcade.View):
    """ Main application class """

    def __init__(self):
        super().__init__()
        # Background image will be stored in this variable
        self.background = None
        self.mold = None
        self.frame_count = 0
        self.all_sprites_list = []
        self.sound = None
        self.score = 0
        self.total_time = 0.0
        self.timer_text = arcade.Text(
            text="00:00:00",
            start_x=50,
            start_y=20,
            color=arcade.color.BLACK,
            font_size=14,
            anchor_x="center",
        )
        #
#
#
#
        # Do show the mouse cursor
        # self.set_mouse_visible(True)

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
#
        self.background = arcade.load_texture("bread.jpg")
        self.all_sprites_list = arcade.SpriteList()
        self.allmoldlist = arcade.SpriteList()
        self.sound = "./images/jump4.wav"
        self.current_state = GAME_RUNNING
        for item in range(3):
            mold = Mold("mold.jpg", .1, ":resources:sounds/hit5.wav")
    #
            mold.center_x = random.randrange(0,SCREEN_WIDTH)
            mold.center_y = random.randrange(0,SCREEN_HEIGHT)
            mold.angle = 0
            mold.change_x = 1
            mold.change_y  = 1
            self.all_sprites_list.append(mold)
            self.allmoldlist.append(mold)
        self.sound = "./images/jump4.wav"
        self.total_time = 0.0
#

#scissors
        self.player_list = arcade.SpriteList()
        self.player_list = None
        self.player_sprite = None
        img = "scissors.jpg"
        self.player_sprite = Scissor(img, SPRITE_SCALING_SCISSOR)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.all_sprites_list.append(self.player_sprite)


    def on_draw(self):
        """Render the screen. """
        arcade.start_render()
        self.draw_game()
        self.timer_text.draw()




    def draw_game(self):

        # Draw the background texture
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)


        self.allmoldlist.draw()
        self.all_sprites_list.draw()
        # output = f"Score: {self.score}"
        # arcade.draw_text(output, 10, 20, arcade.color.BLACK, 14)



    def update(self, delta_time):
        """All the logic to move, and the game logic goes here. """

        self.frame_count += 1

        self.allmoldlist.update()
        # Accumulate the total time
        self.total_time += delta_time

        # Calculate minutes
        minutes = int(self.total_time) // 60

        # Calculate seconds by using a modulus (remainder)
        seconds = int(self.total_time) % 60

        # Calculate 100s of a second
        seconds_100s = int((self.total_time - seconds) * 100)

        # Use string formatting to create a new text string for our timer
        self.timer_text.text = f"{minutes:02d}:{seconds:02d}:{seconds_100s:02d}"

        self.player_sprite.update()
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.allmoldlist)

        # Loop through each colliding sprite, remove it, and add to the score.
        for mold in hit_list:
            game_view = EndView(self.timer_text.text)
            self.window.show_view(game_view)

    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed.
        """
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED
#for releasing key
    def on_key_release(self, key, modifiers):
        """
        Called when the user releases a key.
        """
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

class EndView(arcade.View):
    def __init__(self,time):
        super().__init__()
        self.time = time
    def on_show_view(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Your time was:", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 150,
                         arcade.color.BLACK, font_size=36, anchor_x="center")
        arcade.draw_text(self.time,SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100,
                         arcade.color.BLACK, font_size=36, anchor_x="center")


    def on_mouse_press(self, _x, _y, _button, _modifiers):
        arcade.exit()
# # #
# #
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
