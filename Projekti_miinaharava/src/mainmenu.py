import pygame
from themes import GameTheme
from buttons import Button

pygame.init()


class MainMenu:
    def __init__(self):
        self._theme = GameTheme()

        self.running = False

        self.window_size_x = 720
        self.window_size_y = 480
        self.titlemarginal = 20
        self.buttonmarginal = self.titlemarginal+120
        self.buttonsize = 1.3
        self.start_text = self._theme.text_font.render('Aloita', True, self._theme.text_colour)
        self.quit_text = self._theme.text_font.render('Poistu', True, self._theme.text_colour)
        self.title_text = self._theme.title_font.render('MIINAHARAVA', True, self._theme.text_colour)

        self.window = pygame.display.set_mode((self.window_size_x,self.window_size_y))


    def events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 2*self.window_size_x/3 <= self.mousepos[0] <= 2*self.window_size_x/3+100 and self.buttonmarginal <= self.mousepos[1] <= self.buttonmarginal+50:
                    pygame.quit()


    def run(self):
        self.running = True
        
        while self.running:

            self.events()


            self.window.fill(self._theme.background_colour)

            #Title_text
            self.window.blit(self.title_text, (self.titlemarginal, self.titlemarginal))

            self.mousepos = pygame.mouse.get_pos()

            #Start Button
            Button(self.window_size_x/3-50,self.buttonmarginal,self.buttonsize,self.window,self._theme.button_colour)
            self.window.blit(self.start_text, (self.window_size_x/3-40, self.buttonmarginal+10))

            #Quit Button
            Button(2*self.window_size_x/3-50,self.buttonmarginal,self.buttonsize,self.window,self._theme.button_colour)
            self.window.blit(self.quit_text, (2*self.window_size_x/3-40, self.buttonmarginal+10))

            pygame.display.update()