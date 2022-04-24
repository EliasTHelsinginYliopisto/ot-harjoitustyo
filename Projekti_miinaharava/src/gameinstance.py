import pygame
from themes import GameTheme
from random import randint

class GameLogic:
    def __init__(self):
        self.mineamount = 0
        self.gridsize = 0

        # bring display here
        self.window = None

        #ui elements. 0:Mines, 1:Flags, 2:Points
        self.ui = [None, None, None]

        # Define Clock
        self.clock = pygame.time.Clock()

        # Import theme
        self._theme = GameTheme()

        # Minefield grid
        self.minefield = None

        self.running = False
    
    def run(self, settings):
        self.apply_settings(settings)

        self.ui = [self.mineamount, 0, 0]

        self.minefield = self.create_grid()

        self.running = True

        while self.running:
            self.window.fill(self._theme.background_colour)
            self.update_ui()
            #self.display_grid()
            status = self.events()
            if status == 'return_to_menu':
                return 'return_to_menu'

            self.clock.tick(60)
            pygame.display.update()

    def events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    return 'return_to_menu'
    
    def set_mines(self, start):

        w = self.gridsize
        start = start[0]*w + start[1]
        spots = w ** 2 -1
        places = list(range(spots))
        start_protection = [start-w-1, start-w, start-w+1, start-1,
                            start, start+1, start+w-1, start+w, start+w+1]
        for spot in start_protection:
            if 0 <= spot <= spots:
                places.remove(spot)
        spots = spots-9

        i = 0
        while i < self.mineamount:
            placement = randint(0, spots)
            del places[placement]
            p_y = placement // w
            p_x = placement % w
            self.minefield[placement[0]][placement[1]] = 'M'

            increase_heat = [
            [p_x-1, p_y-1], [p_x-1, p_y], [p_x-1, p_y+1],
            [p_x, p_y]-1, [p_x, p_y+1],
            [p_x+1, p_y-1], [p_x+1, p_y], [p_x+1, p_y+1]
            ]
            for spot in increase_heat:
                if 0 <= p_x <= w-1 and 0 <= p_y <= w-1:
                    if self.minefield[p_x][p_y] != "M":
                        self.minefield[p_x][p_y] += 1

            spots = spots-1
            i += 1



    def create_grid(self):
        grid = [[]] * self.gridsize
        i = 0
        while i < 5:
            grid[i] = [0] * 5
            i += 1
        return grid


    def update_ui(self):
        ui_text = self._theme.text_font.render(
            f'Miinoja: {self.ui[0]} | Liput {self.ui[1]} | Pisteet {self.ui[2]} |', True, self._theme.text_colour
        )
        self.window.blit(ui_text, (10, 10))

    def apply_settings(self, settings):
        if settings[0] == '':
            settings[0] = '10'
        if settings[1] == '':
            settings[1] = '20'

        self.gridsize = int(settings[0])
        self.mineamount = int(settings[1])
        if self.gridsize < 5:
            self.gridsize = 5

        if self.gridsize > 20:
            self.gridsize = 20

        if self.mineamount > (self.gridsize ** 2)*0.5:
            self.mineamount = (self.gridsize ** 2)*0.5
        
        window_x = 30*self.gridsize
        if window_x < 700:
            window_x = 700
        self.window = pygame.display.set_mode(
            (window_x, 60+30*self.gridsize)
        )
