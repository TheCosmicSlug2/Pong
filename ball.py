from settings import *
from math import cos, sin, radians
from random import randint
from pygame import Rect

class Ball:
    def __init__(self, speed, game, player1, player2, screen_width, screen_height):
        self.speed = speed
        self.game = game
        self.player1 = player1
        self.player2 = player2
        self.screen_width, self.screen_height = screen_width, screen_height
        self.half_screen_width, self.half_screen_height = self.screen_width // 2, self.screen_height // 2
        self.posx = self.half_screen_width
        self.posy = self.half_screen_height
        self.direction = randint(110, 250) if randint(0, 1) == 0 else randint(-50, 50)

    def reinit(self):
        self.posx = self.half_screen_width
        self.posy = self.half_screen_height
        self.direction = randint(110, 250) if randint(0, 1) == 0 else randint(-50, 50)

    def check_collision_player(self, player):
        # Trouver le bon côté de la ball que l'on souhaite tester
        side_x = self.posx if player == self.player1 else self.posx + BALL_WIDTH

        return player.posx < side_x < player.posx + PLAYER_WIDTH  and player.posy < self.posy < player.posy + PLAYER_HEIGHT

    def check_collision_wall(self):
        return self.posy <= 0 or self.posy >= self.screen_height - BALL_WIDTH

    def check_out_of_bounds(self):
        if self.posx < 0:
            self.posx = 0
        if self.posx > self.screen_width:
            self.posx = self.screen_width
        if self.posy < 0:
            self.posy = 0
        if self.posy > self.screen_height:
            self.posy = self.screen_height

    def check_collision_line(self):
        return self.posx <= 0 or self.posx >= self.screen_width, self.player2.ID if self.posx < self.screen_width else self.player1.ID
        # On renvoie le gagnant, c'est à dire celui qui n'a pas la balle dans son camp

    def move(self):
        dx = cos(radians(self.direction))
        dy = sin(radians(self.direction))

        if self.check_collision_player(self.player1):
            self.game.sound_paddle.play()
            self.posx = self.player1.posx + PLAYER_WIDTH
            self.direction = 180 - self.direction + randint(-10, 10)
            dx = - dx

        if self.check_collision_player(self.player2):
            self.game.sound_paddle.play()
            self.posx = self.player2.posx - BALL_WIDTH
            self.direction = 180 - self.direction + randint(-10, 10)
            dx = - dx

        if self.check_collision_wall():
            self.game.sound_wall.play()
            self.direction = - self.direction + randint(-10, 10)
            dy = - dy


        self.posx += dx * BALL_SPEED
        self.posy += dy * BALL_SPEED

        self.check_out_of_bounds()

    def get_sprite(self):
        ball_sprite = Rect(self.posx, self.posy, BALL_WIDTH, BALL_WIDTH)
        return ball_sprite
