# NetLookApp

Sovellus tarjoaa osoitteisiin liittyviä tietoverkkopalveluja:

- Verkkotunnusten saatavuushaku IP-osoitteen tai domainnimen perusteella
  - Varatun domainin IP:n tai FQDN:n nouto riippuen haun tyypistä
  - Latenssin mittaus
- Oman yksityisen ja julkisen IP:n nouto
  - IPv4- ja IPv6-osoitetyypin tarkastus
- Oman MAC-osoitteen nouto
  - UAA- ja LAA-osoitetyypin tarkastus

Ohjelma toimii useimmilla Windows, Linux ja macOS käyttöjärjestelmillä.

## Dokumentaatio

- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)
- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)
- [Changelog](./dokumentaatio/changelog.md)

## Alustus

- [Tarkista](https://wiki.python.org/moin/BeginnersGuide/Download), että Python-versiosi on 3.8 tai uudempi
- [Asenna](https://python-poetry.org/docs/#installation) Poetry koneellesi
- [Lataa](https://github.com/weverhall/ot-harjoitustyo/releases/tag/viikko5) ja pura sovelluksen viimeisin GitHub release

Siirry vielä komentorivillä "ot-harjoitustyo" kansioon, niin olet valmis suorittamaan Poetry-komentoja.

## Käynnistys

Asenna riippuvuudet ja käynnistä sovellus:

```bash
poetry install
poetry run invoke start
```

## Testaus ja Pylint

Suorita testit:

```bash
poetry run invoke test
```

Luo testikattavuusraportti index.html htmlcov-kansioon:

```bash
poetry run invoke coverage-report
```

Tee [Pylint-tiedoston](./.pylintrc) määrittelemät kooditarkistukset:

```bash
poetry run invoke lint
```
