import pygame
from circleshape import *
from constants import *  
import random  

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
    
    def draw(self,screen):
        pygame.draw.circle(screen, (255,255,255), (self.position.x, self.position.y), self.radius, 1)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return []
        else:
            random_angle = random.uniform(20,50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            velocity1 = self.velocity.rotate(random_angle) * 1.2
            velocity2 = self.velocity.rotate(-random_angle)* 1.2
            
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = velocity1
            
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = velocity2
            return [asteroid1, asteroid2]
            
            
            



        