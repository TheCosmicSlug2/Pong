from settings import *
from random import randint
from time import sleep
from player import Player
from ball import Ball
from main_menu import MainMenu

class Game:
    def __init__(self, fullscreen):
        pg.init()
        pg.mouse.set_visible(False)

        if fullscreen:
            scaling_settings.change_res_to_fullscreen()
            self.screen = pg.display.set_mode(scaling_settings.RES, FULLSCREEN)
        else:
            self.screen = pg.display.set_mode(scaling_settings.RES)
        pg.display.set_caption("Pong")

        self.font_score = pg.font.Font("ressources/fonts/pong_font.ttf", 74)
        self.font_countdown = pg.font.Font("ressources/fonts/pong_font.ttf", 120)

        pg.mixer.init()

        self.sound_paddle = pg.mixer.Sound("ressources/audio/paddle.mp3")
        self.sound_wall = pg.mixer.Sound("ressources/audio/wall.mp3")
        self.sound_score = pg.mixer.Sound("ressources/audio/score.mp3")

        self.clock = pg.time.Clock()
        self.max_score = 10

    def new_game(self, ai_difficulty):
        p1 = Player(player="1", screen_width=scaling_settings.SCREEN_WIDTH, screen_height=scaling_settings.SCREEN_HEIGHT)
        p2 = Player(player="2", ai=True, ai_difficulty=ai_difficulty, screen_width=scaling_settings.SCREEN_WIDTH, screen_height=scaling_settings.SCREEN_HEIGHT)
        ball = Ball(speed=BALL_SPEED, game=self, player1=p1, player2=p2, screen_width=scaling_settings.SCREEN_WIDTH, screen_height=scaling_settings.SCREEN_HEIGHT)
        return p1, p2, ball

    def update(self):
        pg.display.flip()
        pg.display.set_caption(f"Pong : {self.clock.get_fps():.2f} FPS")
        self.clock.tick(FPS)

    def fill_random_color(self):
        self.screen.fill((randint(0, 255), 0, 0))

    @staticmethod
    def init_background(surface):
        surface.fill(BLACK)
        filet = pg.Rect(scaling_settings.HALF_WIDTH - LARGEUR_FILET // 2, 0, LARGEUR_FILET, scaling_settings.SCREEN_HEIGHT)
        pg.draw.rect(surface, WHITE, filet)
        return surface

    def draw_background(self):
        self.screen.blit(background, (0, 0))

    def init_score_player_1(self, score: int):
        score_text_1 = self.font_score.render(str(score), True, WHITE)
        return score_text_1

    def init_score_player_2(self, score: int):
        score_text_2 = self.font_score.render(str(score), True, WHITE)
        return score_text_2

    def draw_sprite(self, sprite):
        pg.draw.rect(self.screen, WHITE, sprite)



    def update_visible_score(self):
        # Cacher les joueurs et la balle
        self.draw_background()
        self.screen.blit(score_1, (scaling_settings.TEXT_MARGIN_X, TEXT_MARGIN_Y))
        self.screen.blit(score_2, (scaling_settings.SCREEN_WIDTH - score_2.get_width() // 2 - scaling_settings.TEXT_MARGIN_X, TEXT_MARGIN_Y))
        self.update()
        self.sound_score.play()
        sleep(0.5)

    def countdown(self):
        for countdown_nb in range(3, 0, -1):
            self.screen.fill(BLACK)
            countdown_screen = self.font_countdown.render(str(countdown_nb), True, WHITE)
            self.screen.blit(countdown_screen, (scaling_settings.HALF_WIDTH - countdown_screen.get_width() // 4, # normalement // 2 mais c'est pas centré
                                                scaling_settings.HALF_HEIGHT - countdown_screen.get_height() // 2))
            self.update()
            sleep(0.3)

    def check_global_win(self):
        if Player1.get_score() == self.max_score:
            return Player1.ID
        if Player2.get_score() == self.max_score:
            return Player2.ID
        return False


    @staticmethod
    def check_events():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()



if __name__ == "__main__":

    Main_menu = MainMenu()
    FULLSCREEN = Main_menu.get_fullscreen()
    scaling_settings = ScalingSettings()

    game = Game(FULLSCREEN)
    Player1, Player2, Ball = game.new_game(Main_menu.get_ai_difficulty())
    background = game.init_background(pg.Surface((scaling_settings.SCREEN_WIDTH, scaling_settings.SCREEN_HEIGHT)))
    score_1 = game.init_score_player_1(Player1.get_score())
    score_2 = game.init_score_player_2(Player2.get_score())

    game.countdown()

    game_running = True
    while game_running:
        game.check_events()
        # On calcule d'abord
        Player1.move_to_mouse_y()
        if Player2.AI:
            Player2.move_to_ball_y(Ball.posy)
        else:
            Player2.move_to_mouse_y()


        Ball.move()

        win = Ball.check_collision_line()
        if win[0]:
            Player1.reinit()
            Player2.reinit()
            Player1.add_score() if win[1] == Player1.ID else Player2.add_score()
            score_1 = game.init_score_player_1(Player1.get_score())
            score_2 = game.init_score_player_2(Player2.get_score())
            Ball.reinit()

            game.update_visible_score()


            global_win = game.check_global_win()
            if global_win:
                game_running = False
            else:
                game.countdown()



        # On dessine
        game.draw_background()
        game.draw_sprite(Player1.get_player_sprite())
        game.draw_sprite(Player2.get_player_sprite())
        game.screen.blit(score_1, (scaling_settings.TEXT_MARGIN_X, TEXT_MARGIN_Y))
        game.screen.blit(score_2, (scaling_settings.SCREEN_WIDTH - score_2.get_width() // 2 - scaling_settings.TEXT_MARGIN_X, TEXT_MARGIN_Y))
        game.draw_sprite(Ball.get_sprite())
        game.update()


