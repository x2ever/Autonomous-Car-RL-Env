#initialize the screen
import pygame, math, sys, time
from pygame.locals import *
from Trophy import TrophySprite
from Car import CarSprite
from Wall import WallSprite
import copy


class Game:
    def __init__(self, walls, trophies, car, lidar):
        self.init_args = [copy.copy(walls), copy.copy(trophies), copy.copy(car)]
        pygame.init()
        self.car = car
        self.screen = pygame.display.set_mode((1024, 768))
        self.clock = pygame.time.Clock()
        font = pygame.font.Font(None, 75)
        self.win_font = pygame.font.Font(None, 50)
        self.win_condition = None
        self.win_text = font.render('', True, (0, 255, 0))
        self.loss_text = font.render('', True, (255, 0, 0))
        pygame.mixer.music.load('My_Life_Be_Like.mp3')
        self.t0 = self.t1 = time.time()
        self.wall_group = pygame.sprite.RenderPlain(*walls)
        self.trophy_group = pygame.sprite.RenderPlain(*trophies)
        self.car_group = pygame.sprite.RenderPlain(car)
        self.rect = self.screen.get_rect()
        self.stop = False
        self.lidar = lidar
        self.lidar_data = None

    def run(self):
        while True:
            #USER INPUT
            self.t1 = time.time()
            dt = self.t1-self.t0

            deltat = self.clock.tick(30)
            seconds = round(dt, 2)
            for event in pygame.event.get():
                if not hasattr(event, 'key'): continue
                down = event.type == KEYDOWN 
                if self.win_condition == None: 
                    if event.key == K_RIGHT: self.car.k_right = down * -5 
                    elif event.key == K_LEFT: self.car.k_left = down * 5
                    elif event.key == K_UP: self.car.k_up = down * 2
                    elif event.key == K_DOWN: self.car.k_down = down * -2 
                    elif event.key == K_ESCAPE: sys.exit(0) # quit the game
                elif self.win_condition == True and event.key == K_SPACE: print(seconds); self.stop = True
                elif self.win_condition == False and event.key == K_SPACE:
                    print(seconds)
                    self.again()
                    t0 = t1
                elif event.key == K_ESCAPE: sys.exit(0)    
                
            #RENDERING
            self.screen.fill((0,0,0))
            self.car_group.update(deltat)
            collisions = pygame.sprite.groupcollide(self.car_group, self.wall_group, False, False, collided = None)
            if collisions != {}:
                self.win_condition = False
                self.car.image = pygame.image.load('images/collision.png')
                loss_text = self.win_font.render('Press Space to Retry', True, (255,0,0))
                seconds = 0
                self.car.MAX_FORWARD_SPEED = 0
                self.car.MAX_REVERSE_SPEED = 0
                self.car.k_right = 0
                self.car.k_left = 0

            trophy_collision = pygame.sprite.groupcollide(self.car_group, self.trophy_group, False, True)
            if trophy_collision != {}:
                seconds = seconds
                self.win_condition = True
                self.car.MAX_FORWARD_SPEED = 0
                self.car.MAX_REVERSE_SPEED = 0
                pygame.mixer.music.play(loops=0, start=0.0)
                self.win_text = self.win_font.render('Press Space to Advance', True, (0,255,0))
                if self.win_condition == True:
                    car.k_right = -5
                    

            self.wall_group.update(collisions)
            self.wall_group.draw(self.screen)
            self.car_group.draw(self.screen)
            self.trophy_group.draw(self.screen)
            #Counter Render
            self.screen.blit(self.win_text, (250, 700))
            self.screen.blit(self.loss_text, (250, 700))
            pygame.display.flip()

            self.lidar.data = self.screen
    
    def again(self):
        self.__init__(*self.init_args)
        self.run()

    def make_lidar_data(self):
        self.lidar.get_data(self.lidar_data)

if __name__ == "__main__":
    walls = [
        WallSprite((512, 2.5), 1024, 5),
        WallSprite((512, 765.5), 1024, 5),
        WallSprite((2.5, 384), 5, 768),
        WallSprite((1021.5, 384), 5, 768)
    ]
    trophies = [
        TrophySprite((300,50))
    ]
    car = CarSprite('images/car.png', (50, 700))
    g = Game(walls, trophies, car)
    g.run()

