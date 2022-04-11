# NetLookApp
Sovellus tarjoaa osoitteisiin liittyviä tietoverkkopalveluja:

- Verkkotunnusten IP- ja saatavuushaku
- Oman IP- ja MAC-osoitteen nouto
  - IP:stä tarkastetaan, onko osoite yksityinen vai julkinen
  - MAC:n osalta selvitetään, onko se UAA- vai LAA-tyyppinen (jos löytyy molemmat, näytetään yksilöivämpi UAA)
- Muut mahdolliset toiminnallisuudet = WIP :)

## Dokumentaatio

- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)
- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)
- [Changelog](./dokumentaatio/changelog.md)

## Asennus ja käynnistys

Asenna riippuvuudet ja käynnistä sovellus:

```bash
poetry install
poetry run invoke start
```

Tarkista myös, että Python-versiosi on 3.8 tai uudempi:

```bash
python3 --version
```

## Testaus ja Pylint

Suorita testit:

```bash
poetry run invoke test
```

Luo testikattavuusraportti htmlcov-hakemistoon:

```bash
poetry run invoke coverage-report
```

Tee [Pylint-tiedoston](./.pylintrc) määrittelemät kooditarkistukset:

```bash
poetry run invoke lint
```
