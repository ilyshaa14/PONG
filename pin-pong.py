import pygame
import os


image_files = os.listdir('sakura')

sakura_frames = [pygame.image.load(f'sakura/{i}') for i in image_files]



pygame.init()

class Game:
    def __init__(self, name):
        self.scene_width = 1000
        self.scene_height = 600

        self.SCENE = pygame.display.set_mode([self.scene_width, self.scene_height])
        self.name = name

        self.sakura_frame_index = 0

        self.ball_width = 100
        self.ball_speed_x = 5
        self.ball_speed_y = 5
        self.ball = pygame.Rect(self.scene_width/2 - self.ball_width/2, self.scene_height/2 - self.ball_width/2, self.ball_width, self.ball_width)
        self.player = pygame.Rect(0 + 25, 0, 30, 100)
        self.enemy = pygame.Rect(self.scene_width - 30 - 25, 0, 30, 100)
        self.enemy_ai_active = False
        self.running = True 
        self.fps = 60
        
    
        self.clock = pygame.time.Clock()
    def sakura_anim(self):
        frame = sakura_frames[self.sakura_frame_index]
        frame = pygame.transform.scale(frame, [frame.get_width() * 0.5, frame.get_height() * 0.5])
        self.SCENE.blit(frame, [self.scene_width - frame.get_width(), self.scene_height - frame.get_height()])
        self.sakura_frame_index += 1
        if self.sakura_frame_index >= len(sakura_frames):
            self.sakura_frame_index = 0
    def run(self):
        while self.running:
            self.clock.tick(self.fps)
            pygame.display.set_caption(f'{self.name} [{self.clock.get_fps():.1f}]')

            self.SCENE.fill([0, 0, 0])

            self.sakura_anim()

           # print(self.ball.x)

            self.ball.x += self.ball_speed_x
            self.ball.y += self.ball_speed_y

            
            if self.ball.x > self.scene_width + self.ball_width:
                self.ball.x = self.scene_width/2 - self.ball_width/2
                self.ball.y = self.scene_height/2 - self.ball_width/2
                self.ball_speed_x = 5
                self.ball_speed_y = 5
            if self.ball.x < 0 - self.ball_width*2:
                self.ball.x = self.scene_width/2 - self.ball_width/2
                self.ball.y = self.scene_height/2 - self.ball_width/2
                self.ball_speed_x = 5
                self.ball_speed_y = 5
            if self.ball.y > self.scene_height - self.ball_width:
                self.ball_speed_y *= -1
            if self.ball.y < 0:
                self.ball_speed_y *= -1
            pygame.draw.ellipse(self.SCENE, [252, 68, 237], self.ball)

            if self.ball.colliderect(self.player):
                self.ball_speed_x *= -1.1
            
            pygame.draw.rect(self.SCENE, [154, 212, 70], self.player)

            keys = pygame.key.get_pressed()

            if keys[pygame.K_w]:
                self.player.y -= 5

            if keys[pygame.K_s]:
                self.player.y += 5

            pygame.draw.rect(self.SCENE, [66, 245, 239], self.enemy)

            if keys[pygame.K_o]:
                self.enemy.y -= 5

            if keys[pygame.K_l]:
                self.enemy.y += 5
            
            if self.ball.colliderect(self.enemy):
                self.ball_speed_x *= -1.1
            #AI

            if self.enemy_ai_active:
                self.enemy.y = self.ball.y
            
            pygame.display.update()


            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                       self.enemy_ai_active = not self.enemy_ai_active 
            

            




game = Game('ping-pong')
game.run()

pygame.quit()
