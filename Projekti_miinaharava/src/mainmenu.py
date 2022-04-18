import pygame
from themes import GameTheme
from buttons import Button

pygame.init()


class MainMenu:
    def __init__(self):

        # Define Clock
        self.clock = pygame.time.Clock()

        # Call GameTheme Class
        self._theme = GameTheme()

        # While True - menu is active
        self.running = False

        # menu entities
        self.buttons = [None, None, None] # Start, Quit, Leaderboards
        self.input_rects = [None, None] # Size, Mines
        self.inputs = [str(''), str('')]

        # State of setting inputboxes 0 = size, 1 = mines.
        self.settingsactive = [False, False]

        # Pygame display
        window_size_x = 720
        window_size_y = 480
        self.window = pygame.display.set_mode(
            (window_size_x, window_size_y))

    # Pylint says this function is highly problematic
    def events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.buttons[1].rect.collidepoint(mouse_pos):
                    pygame.quit()
                elif self.input_rects[0].rect.collidepoint(mouse_pos):
                    self.settingsactive = [True, False]
                elif self.input_rects[1].rect.collidepoint(mouse_pos):
                    self.settingsactive = [False, True]
                else:
                    self.settingsactive = [False, False]

            if event.type == pygame.KEYDOWN:
                num09 = "1234567890"
                if event.unicode in num09:
                    if self.settingsactive[0] and len(self.inputs[0]) < 4:
                        self.inputs[0] += event.unicode
                    elif self.settingsactive[1] and len(self.inputs[1]) < 4:
                        self.inputs[1] += event.unicode
                if event.key == pygame.K_BACKSPACE:
                    if self.settingsactive[0]:
                        self.inputs[0] = self.inputs[0][:-1]
                    elif self.settingsactive[1]:
                        self.inputs[1] = self.inputs[1][:-1]


    def run(self):
        # To have less instance attributes there's some repetition.
        # maybe fix by creating new classes for different entities
        buttonsize = 1.3
        titlemarginal = 20
        buttonmarginal = 140
        window_size_x = 720

        self.running = True

        while self.running:

            self.window.fill(self._theme.background_colour)

            # Title_text
            title_text = self._theme.title_font.render(
                'MIINAHARAVA', True, self._theme.text_colour)
            self.window.blit(
                title_text, (titlemarginal, titlemarginal))

            # Start Button
            self.buttons[0] = Button(window_size_x/3-50, buttonmarginal,
                   buttonsize, self.window, self._theme.button_colour)
            start_text = self._theme.text_font.render(
                'Aloita', True, self._theme.text_colour)
            self.window.blit(
                start_text, (window_size_x/3-40, buttonmarginal+10))

            # Quit Button
            self.buttons[1] = Button(2*window_size_x/3-50, buttonmarginal,
                   buttonsize, self.window, self._theme.button_colour)
            quit_text = self._theme.text_font.render(
                'Poistu', True, self._theme.text_colour)
            self.window.blit(
                quit_text, (2*window_size_x/3-40, buttonmarginal+10))

            self.input_boxes()
            self.events()
            self.clock.tick(60)
            pygame.display.update()

    def input_boxes(self):
        buttonsize = 1
        window_size_x = 720

        # Size input
        settingsmarginal = 240
        sizeset_text = self._theme.text_font.render(
            'Koko:', True, self._theme.text_colour)
        self.window.blit(sizeset_text, (window_size_x/3-100, settingsmarginal+10))
        self.input_rects[0] = Button(window_size_x/3+10, settingsmarginal+10,
                              buttonsize, self.window, self._theme.button_colour)
        sizes_input = self._theme.text_font.render(self.inputs[0], True, self._theme.text_colour)
        self.window.blit(sizes_input, (window_size_x/3+10, settingsmarginal+20))

        # Mine input
        mines_text = self._theme.text_font.render(
            'Miinat:', True, self._theme.text_colour)
        self.window.blit(
            mines_text, (2*window_size_x/3-100, settingsmarginal+10))
        self.input_rects[1] = Button(2*window_size_x/3+30, settingsmarginal+10,
                            buttonsize, self.window, self._theme.button_colour)

        mines_input = self._theme.text_font.render(self.inputs[1], True, self._theme.text_colour)
        self.window.blit(mines_input, (2*window_size_x/3+40, settingsmarginal+20))
