# Miinaharava
Sovellus klassinen tietokonepeli Miinaharava. Käyttäjä voi pelata sovelluksella Miinaharavaa ja tallettaa huipputulokset tulostauluun.

**HUOM:** Sovelluksella ei voi vielä pelata miinaharavaa


## Dokumentaatio:  
[vaatimusmäärittely](Projekti_miinaharava/Dokumentaatio/vaatimusmaarittely.md)  
[työaikakirjanpito](Projekti_miinaharava/Dokumentaatio/tyoaikakirjanpito.md)  
[changelog](changelog.md)  

## Komentorivitoiminnot:

### Asennus

    poetry install

### Käynnistys

    poetry run invoke start

### Testaus

    poetry run invoke test

### Testikattavuusreportin luonti

    poetry run invoke coverage-report
Testikattavuus luodaan htmlcov hakemistoon
