import pygame
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
    
    def draw(self,screen):
        pygame.draw.circle(screen, (255,255,255), (self.position.x, self.position.y), self.radius, 1)
    
    def update(self, dt):
        #fix the parameter. How to get the velocity. "circle(surface, color, center, radius) -> Rect"
        self.position += self.velocity * dt
                

        