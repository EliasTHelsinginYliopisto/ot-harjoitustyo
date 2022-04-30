from random import randint
import pygame
from themes import GameTheme



class GameLogic:
    def __init__(self):
        self.mineamount = 0
        self.gridsize = 0

        # bring display here
        self.window = None

        # ui elements. 0:Mines, 1:Flags, 2:Points
        self.user_interface = [0, 0, 0]

        # Define Clock
        self.clock = pygame.time.Clock()

        # Import theme
        self._theme = GameTheme()

        # Minefield grid
        self.minefield = None

        # Game progress
        self.in_progress = False

        self.running = False

    def run(self, settings):
        self.apply_settings(settings)

        self.user_interface = [self.mineamount, 0, 0]

        self.minefield = self.create_grid()

        self.window.fill(self._theme.background_colour)
        self.display_grid()

        self.running = True

        while self.running:
            self.update_ui()
            status = self.events()
            if status == 'return_to_menu':
                return 'return_to_menu'

            self.clock.tick(60)
            pygame.display.update()

    def display_grid(self):
        i = 0
        j = 0
        while i < self.gridsize:
            while j < self.gridsize:
                pygame.draw.rect(
                    self.window, self._theme.closed_colour, pygame.Rect((i*30, 60+j*30), (28, 28)))
                j += 1
            j = 0
            i += 1

    def events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.in_progress = False
                    return 'return_to_menu'

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                line = mouse_pos[0] // 30
                row = (mouse_pos[1]-60) // 30
                if event.button == 1:
                    self.reveal_square(line, row)
                elif event.button == 3:
                    self.set_flag(line, row)

    def set_flag(self, line, row):
        if line < 0 or line >= self.gridsize or row < 0 or row >= self.gridsize:
            return
        if self.minefield[row][line][1] == 'open':
            return
        
        if self.minefield[row][line][1] == 'flagged':
            self.minefield[row][line][1] = 'closed'
            self.user_interface[1] -= 1
            pygame.draw.rect(
                    self.window, self._theme.closed_colour, pygame.Rect((line*30, 60+row*30), (28, 28)))
        
        else:
            self.minefield[row][line][1] = 'flagged'

            self.user_interface[1] += 1

            text = self._theme.mines_font.render(
                'F', True, self._theme.text_colour
            )
            self.window.blit(text, (5+line*30, 65+row*30))
        
        


    def reveal_square(self, line, row):
        if line < 0 or line >= self.gridsize or row < 0 or row >= self.gridsize:
            return
        if self.minefield[row][line][1] != 'closed':
            return
        if not self.in_progress:
            self.in_progress = True
            self.set_mines([line, row])

        pygame.draw.rect(
                    self.window, self._theme.button_colour, pygame.Rect((line*30, 60+row*30), (28, 28)))

        self.minefield[row][line][1] = 'open'

        self.user_interface[2] += 10

        content = self.minefield[line][row][0]

        if content == 0:

            surrounding = [(row-1, line-1), (row-1, line), (row-1, line+1),
                           (row, line-1), (row, line+1),
                           (row+1, line-1), (row+1, line), (row+1, line+1)]
            for square in surrounding:
                self.reveal_square(square[1], square[0])
            return

        if content == 'M':
            self.user_interface[2] -= 10
            self.end_game()

        text = self._theme.mines_font.render(
            str(content), True, self._theme.text_colour
        )
        self.window.blit(text, (5+line*30, 65+row*30))

    def end_game(self):
        for i in range(self.gridsize):
            for j in range(self.gridsize):
                if self.minefield[i][j][0] == 'M':
                    if self.minefield[i][j][1] == 'flagged':
                        self.user_interface[2] += 100
                    else:
                        text = self._theme.mines_font.render(
                        str('M'), True, self._theme.text_colour
                    )
                        self.window.blit(text, (5+i*30, 65+j*30))

    def set_mines(self, start):

        width = self.gridsize
        start = start[0]*width+ start[1]
        spots = width ** 2
        places = list(range(spots))
        start_protection = [start-width-1, start-width, start-width+1, start-1,
                            start, start+1, start+width-1, start+width, start+width+1]
        for spot in start_protection:
            if 0 <= spot <= spots:
                places.remove(spot)
        spots = spots-10

        i = 0
        while i < self.mineamount:
            placement = randint(0, spots)
            spot = places[placement]
            del places[placement]
            p_y = spot // width
            p_x = spot % width
            self.minefield[p_y][p_x][0] = 'M'

            increase_heat = [
                [p_x-1, p_y-1], [p_x-1, p_y], [p_x-1, p_y+1],
                [p_x, p_y-1], [p_x, p_y+1],
                [p_x+1, p_y-1], [p_x+1, p_y], [p_x+1, p_y+1]
            ]
            for spot in increase_heat:
                if spot[0] >= 0 and spot[0] < width and spot[1] >= 0 and spot[1] < width:
                    if self.minefield[spot[1]][spot[0]][0] != "M":
                        self.minefield[spot[1]][spot[0]][0] += 1

            spots = spots-1
            i += 1

    def create_grid(self):
        grid1 = []
        for _ in range(self.gridsize):
            grid2 = []
            for _ in range(self.gridsize):
                grid2.append([0, 'closed'])
            grid1.append(grid2)
        return grid1

    def update_ui(self):
        ui_text = self._theme.text_font.render(
            f"""Miinoja: {self.user_interface[0]} | Liput {self.user_interface[1]}| Pisteet {self.user_interface[2]} |""",
            True, self._theme.text_colour
        )
        pygame.draw.rect(
            self.window, self._theme.background_colour, pygame.Rect((0, 0), (700, 60))
        )
        self.window.blit(ui_text, (10, 10))

    def apply_settings(self, settings):
        if settings[0] == '':
            settings[0] = '10'
        if settings[1] == '' or settings[1] == 0:
            settings[1] = '20'

        self.gridsize = int(settings[0])
        self.mineamount = int(settings[1])

        self.gridsize = max(self.gridsize, 5)
        self.gridsize = min(self.gridsize, 20)

        if self.mineamount > (self.gridsize ** 2)*0.5:
            self.mineamount = int((self.gridsize ** 2)*0.5)

        window_x = 30*self.gridsize
        window_x = max(window_x, 700)
        self.window = pygame.display.set_mode(
            (window_x, 80+30*self.gridsize)
        )
