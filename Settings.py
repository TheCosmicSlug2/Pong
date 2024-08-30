import pygame as pg

FPS = 30

LARGEUR_FILET = 5

PLAYER_WIDTH = 15
PLAYER_HEIGHT = 80
ECART_BORD_JOUEUR = 40
AI_SCALING_FACTOR = 0

BALL_SPEED = 10
BALL_WIDTH = 10

TEXT_MARGIN_Y = 40

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)



class ScalingSettings:
    def __init__(self):
        self.RES = (800, 600)
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = self.RES[0], self.RES[1]
        self.HALF_WIDTH, self.HALF_HEIGHT = self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2
        self.TEXT_MARGIN_X = self.SCREEN_WIDTH // 4  # 1/4 de largeur >>>>>

    def change_res_to_fullscreen(self):
        self.RES = (pg.display.Info().current_w, pg.display.Info().current_h)
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = self.RES[0], self.RES[1]
        self.HALF_WIDTH, self.HALF_HEIGHT = self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2
        self.TEXT_MARGIN_X = self.SCREEN_WIDTH // 4  # 1/4 de largeur >>>>>



