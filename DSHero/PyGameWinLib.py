import pygame

class Screen():
    def __init__(self, size, title):
        self.size = size
        self.title = title
        
        pygame.init()
        pygame.display.init()
        
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.title)
    
    def write_text(self, pos, text, font, color, antialias = True):
        self.screen.blit(font.render(text, antialias, [color.r, color.g, color.b]), pos)
    
    def flip(self): pygame.display.flip()
    def blit(self, *args, **kwargs): self.screen.blit(*args, **kwargs)
    def fill(self, *args, **kwargs): self.screen.fill(*args, **kwargs)
