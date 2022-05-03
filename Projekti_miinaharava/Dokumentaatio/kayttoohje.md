# Käyttöohje
Lataa viimeisin release [täältä](https://github.com/EliasTHelsinginYliopisto/ot-harjoitustyo/releases/tag/v0.0.1)

## Ohjelman käynnistäminen

1. Asenna sovelluksen riippuvuudet
```bash
poetry install
```
2. Suorita alustustoimenpiteet
```bash
poetry run invoke build
```
3. Käynnistä sovellus
```bash
poetry run invoke start
```

## Päävalikko
Sovellus avautuu päävalikkoon
![Päävalikko](/Projekti_miinaharava/Dokumentaatio/päävalikko_ver.0.0.2.png)
Voit määrittää miinakentän koon ja miinojen määrän kirjoittamalla tekstikenttiin. miinakentän koko pitää olla välillä 5-20. Maksimissaan puolet kentästä voi olla miinoja.  
Alota peli painamalla 'Aloita', sulje sovellus painamalla 'Poistu'

## Peli
![Pelin_kuvaus](/Projekti_miinaharava/Dokumentaatio/peli_ver.0.0.2.png)
pelin yläreunassa näkyy kuinka monta miinaa on kentässä, kuinka monta lippua on sijoitettu, ja kuinka paljon on pisteitä. Jos osut miinaan, tai avaat kaikki turvalliset luukut, peli päättyy.

### Pisteytys
- Luukun avaaminen - 10p
- Oikein sijoitettu lippu - 100p
- Voitto - 1000p

### Ohjaaminen
- Voit avata luukun hiiren vasemmalla näppäimellä
- Voit pystyttää lipun hiiren oikealla näppäimellä
- Voit palata menuun askelpalauttimella