# NetLookApp

Sovellus tarjoaa osoitteisiin liittyviä tietoverkkopalveluja:

- Verkkotunnusten saatavuushaku IP-osoitteen tai domain-nimen perusteella
  - Varatun domainin IP:n tai FQDN:n nouto riippuen haun tyypistä
  - Latenssin mittaus
  - Hakuhistorian tallennus ja poisto
- Oman yksityisen ja julkisen IP:n nouto
  - IPv4- ja IPv6-osoitetyypin tarkastus
- Oman MAC-osoitteen nouto
  - UAA- ja LAA-osoitetyypin tarkastus

Ohjelma toimii yleisimmillä Linux, macOS ja Windows versioilla.

## Dokumentaatio

- [Käyttöohje](./dokumentaatio/kayttoohje.md)
- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)
- [Testausdokumentti](./dokumentaatio/testaus.md)
- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)
- [Changelog](./dokumentaatio/changelog.md)

## Valmistelut

- [Tarkista](https://wiki.python.org/moin/BeginnersGuide/Download), että Python-versiosi on 3.8 tai uudempi
- [Asenna](https://python-poetry.org/docs/#installation) Poetry koneellesi
- [Lataa](https://github.com/weverhall/ot-harjoitustyo/releases/tag/viikko6) ja pura sovelluksen viimeisin GitHub-julkaisu

Siirry vielä komentorivillä "ot-harjoitustyo" kansioon, niin olet valmis suorittamaan Poetry-komentoja.

## Käynnistys

Asenna riippuvuudet, alusta tietokanta ja käynnistä sovellus:

```bash
poetry install
poetry run invoke build
poetry run invoke start
```

## Testaus ja Pylint

Suorita testit (Windows toimivuudesta ei takeita):

```bash
poetry run invoke test
```

Luo testikattavuusraportti htmlcov-kansioon:

```bash
poetry run invoke coverage-report
```

Tee [Pylint-tiedoston](./.pylintrc) määrittelemät kooditarkistukset:

```bash
poetry run invoke lint
```
