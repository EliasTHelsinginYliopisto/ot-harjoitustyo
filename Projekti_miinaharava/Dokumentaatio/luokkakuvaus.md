```mermaid
classDiagram
    class Miinaharava
    class MainMenu
    class GameTheme

    Miinaharava --> MainMenu
    MainMenu ..> GameTheme
    Miinaharava --> TulevaLuokka_peli
    TulevaLuokka_peli ..> GameTheme
    TulevaLuokka_tulostaulu ..> GameTheme
    TulevaLuokka_tulostaulu ..> TulevaTietokanta_Huipputulokset
    Miinaharava --> TulevaLuokka_tulostaulu
```