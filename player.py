from settings import *
from pygame import mouse, Rect

class Player:
    def __init__(self, player: str, screen_width, screen_height, ai_difficulty=None, ai=None):
        self.screen_width, self.screen_height = screen_width, screen_height
        self.half_screen_width, self.half_screen_height = self.screen_width // 2, self.screen_height // 2
        self.width, self.height = PLAYER_WIDTH, PLAYER_HEIGHT

        self.dic_player_start_pos = {"1": ECART_BORD_JOUEUR, "2": self.screen_width - ECART_BORD_JOUEUR}
        self.ID = player
        self.posx, self.posy = self.dic_player_start_pos[self.ID], self.half_screen_height - self.height // 2

        self.score = 0
        self.AI = ai
        if self.AI:
            self.AI_difficulty = ai_difficulty
            self.AI_speed = self.AI_difficulty + AI_SCALING_FACTOR

    def reinit(self):
        self.posy = self.half_screen_height - self.height // 2

    def add_score(self):
        self.score += 1

    def get_score(self):
        return self.score

    def check_border_collisions(self):
        if self.posy < 0:
            self.posy = 0
        if self.posy > self.screen_height - PLAYER_HEIGHT:
            self.posy = self.screen_height - PLAYER_HEIGHT

    def move_to_mouse_y(self):
        self.posy = mouse.get_pos()[1] - self.height // 2
        self.check_border_collisions()

    def move_to_ball_y(self, ball_pos_y):
        if ball_pos_y > self.posy + self.height // 2:
            self.posy += self.AI_speed
        else:
            self.posy -= self.AI_speed
        self.check_border_collisions()

    def get_player_sprite(self):
        player_sprite = Rect(self.posx, self.posy, PLAYER_WIDTH, PLAYER_HEIGHT)
        return player_sprite
