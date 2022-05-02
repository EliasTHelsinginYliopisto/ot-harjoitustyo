import pygame
from themes import GameTheme
from buttons import Button

pygame.init()


class MainMenu:
    """Luokka joka suorittaa pelin päävalikkoa
    Attributes:
        clock:
            pygamen kello
        theme:
            Sovelluksen värit ja fontit
        running:
            boolean muuttuja siitä onko menu käynnissä
        buttons:
            Pygamen rect luokat menun napeista. 0 = Aloita,
            1 = lopeta, 2 = tulostaulukko
        input_rects:
            pygamen rect luokat pelin asetuksia varten
            0 = koko, 1 = miinat
        self.inputs:
            asetuksiin syötetty tieto.
            0 = koko, 1 = miinat.
        settingsactive:
            Pitää muistissa mitkä tekstikentät ovat aktiivisia
        window:
            pygamen näyttö
    """

    def __init__(self):
        """Luokan konstruktori"""
        
        self.clock = pygame.time.Clock()

        self._theme = GameTheme()

        self.running = False

        self.buttons = [None, None, None]  
        self.input_rects = [None, None]  
        self.inputs = [str(''), str('')]

        self.settingsactive = [False, False]

        self.window = None

    def events(self):
        """Lukee käyttäjän syötteet

        Returns:
            'quit_game': jos painetaan 'lopeta'-nappia
            'start_game': Jos painetaan 'aloita'-nappia
        """
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False
                return 'quit_game'

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.buttons[1].rect.collidepoint(mouse_pos):
                    pygame.display.quit()
                elif self.buttons[0].rect.collidepoint(mouse_pos):
                    return "start_game"
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
        """suorittaa päävalikkoa
        
        Args:
        buttonsize: määrittää nappejen koon
        titlemarginal: marginaali näytön yläreunasta otsikkoon
        buttonmarginal: marginaali yläreunasta nappeihin
        window_size_x: näytön leveys
        window_size_y: näytön korkeus"""
        
        buttonsize = 1.3
        titlemarginal = 20
        buttonmarginal = 140
        window_size_x = 720
        window_size_y = 480
        self.window = pygame.display.set_mode(
            (window_size_x, window_size_y))

        self.running = True

        while self.running:

            self.window.fill(self._theme.background_colour)

            title_text = self._theme.title_font.render(
                'MIINAHARAVA', True, self._theme.text_colour)
            self.window.blit(
                title_text, (titlemarginal, titlemarginal))

            self.buttons[0] = Button(window_size_x/3-50, buttonmarginal,
                                     buttonsize, self.window, self._theme.button_colour)
            start_text = self._theme.text_font.render(
                'Aloita', True, self._theme.text_colour)
            self.window.blit(
                start_text, (window_size_x/3-40, buttonmarginal+10))

            self.buttons[1] = Button(2*window_size_x/3-50, buttonmarginal,
                                     buttonsize, self.window, self._theme.button_colour)
            quit_text = self._theme.text_font.render(
                'Poistu', True, self._theme.text_colour)
            self.window.blit(
                quit_text, (2*window_size_x/3-40, buttonmarginal+10))

            self.input_boxes()

            status = self.events()
            if status == "start_game":
                return self.inputs
            if status == 'quit_game':
                return status

            self.clock.tick(60)
            pygame.display.update()

    def input_boxes(self):
        """sijoittaa tekstikentät näytölle
        
        Args:
        buttonsize: määrittää tekstikenttien koon
        window_size_x: näytön leveys
        settingsmarginal: marginaali näytön yläreunasta asetuksiin"""

        buttonsize = 1
        window_size_x = 720
        settingsmarginal = 240

        sizeset_text = self._theme.text_font.render(
            'Koko:', True, self._theme.text_colour)
        self.window.blit(
            sizeset_text, (window_size_x/3-100, settingsmarginal+10))
        self.input_rects[0] = Button(window_size_x/3+10, settingsmarginal+10,
                                     buttonsize, self.window, self._theme.button_colour)
        sizes_input = self._theme.text_font.render(
            self.inputs[0], True, self._theme.text_colour)
        self.window.blit(
            sizes_input, (window_size_x/3+10, settingsmarginal+20))

        mines_text = self._theme.text_font.render(
            'Miinat:', True, self._theme.text_colour)
        self.window.blit(
            mines_text, (2*window_size_x/3-100, settingsmarginal+10))
        self.input_rects[1] = Button(2*window_size_x/3+30, settingsmarginal+10,
                                     buttonsize, self.window, self._theme.button_colour)

        mines_input = self._theme.text_font.render(
            self.inputs[1], True, self._theme.text_colour)
        self.window.blit(
            mines_input, (2*window_size_x/3+40, settingsmarginal+20))
