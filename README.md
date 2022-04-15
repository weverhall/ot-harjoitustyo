# NetLookApp
Sovellus tarjoaa tietoverkon osoitehakupalveluja:

- Verkkotunnusten saatavuushaku
  - Varatun verkkotunnuksen IP:n nouto
- Oman yksityisen ja julkisen IP-osoitteen nouto
  - IPv4- ja IPv6-osoitetyypin tarkastus
- Oman MAC-osoitteen nouto
  - UAA- ja LAA-osoitetyypin tarkastus

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
