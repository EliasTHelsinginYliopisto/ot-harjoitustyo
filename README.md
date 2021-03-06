# Miinaharava
Sovellus klassinen tietokonepeli Miinaharava. Käyttäjä voi pelata sovelluksella Miinaharavaa ja tallettaa huipputulokset tulostauluun.




## Dokumentaatio:  
- [vaatimusmäärittely](Projekti_miinaharava/Dokumentaatio/vaatimusmaarittely.md)  
- [työaikakirjanpito](Projekti_miinaharava/Dokumentaatio/tyoaikakirjanpito.md)  
- [arkkitehtuurikuvaus](Projekti_miinaharava/Dokumentaatio/arkkitehtuurikuvaus.md)   
- [changelog](changelog.md)  
- [käyttöohje](Projekti_miinaharava/Dokumentaatio/kayttoohje.md)

## Sovelluksen Käyttö

Käynnistettyäsi sovelluksen pääset menuun. Menussa voit määrittää kentän koon ja miinojen määrän klikkaamalla asetuksia ja kirjoittamalla määrän.  
Kentän koko voi olla välillä 5-20, miinoja voi olla vähintään 1, ja enintään puolet kentästä.  
Aloita peli painamalla 'Aloita', voit avata luukkuja painamalla niitä pelissä.  
Palaa menuun BACKSPACE-näppäimellä ja sule peli klikkaamalla 'Lopeta'

## Komentorivitoiminnot:

### Asennus
Lataa uusin julkaisu
- [Release Loppupalautus](https://github.com/EliasTHelsinginYliopisto/ot-harjoitustyo/releases/tag/v1.0.0)

1. 
```bash
poetry install
```
2.  
```bash
poetry run invoke build
```
3.  
```bash
poetry run invoke start
```

### Käynnistys

    poetry run invoke start
saatat joutua siirtymään 'Projekti_miinaharava' hakemistoon

### Testaus

    poetry run invoke test

### Testikattavuusreportin luonti

    poetry run invoke coverage-report
Testikattavuus luodaan htmlcov hakemistoon

### Pylint

    poetry run invoke lint
