# NetLookApp

Sovellus tarjoaa osoitteisiin liittyviä tietoverkkopalveluja:

- Verkkotunnusten saatavuushaku IP-osoitteen tai domainnimen perusteella
  - Varatun domainin IP:n tai FQDN:n nouto riippuen haun tyypistä
  - Latenssin mittaus
- Oman yksityisen ja julkisen IP:n nouto
  - IPv4- ja IPv6-osoitetyypin tarkastus
- Oman MAC-osoitteen nouto
  - UAA- ja LAA-osoitetyypin tarkastus

## Dokumentaatio

- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)
- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)
- [Changelog](./dokumentaatio/changelog.md)

## Alustus ja lataus

[Tarkista](https://wiki.python.org/moin/BeginnersGuide/Download) ensin, että Python-versiosi on 3.8 tai uudempi, ja asenna Poetry koneellesi [ohjeiden](https://python-poetry.org/docs/#installation) mukaisesti.

Lataa sitten sovellus [release-linkin](https://github.com/weverhall/ot-harjoitustyo/releases/tag/viikko5) kautta. 

Varmista vielä, että olet terminaalissa "ot-harjoitustyo" kansiossa, niin olet valmis suorittamaan Poetry-komentoja.

## Asennus ja käynnistys

Linux/Mac:

```bash
poetry install
poetry run invoke start
```

Windows:

```bash
poetry install
poetry run invoke start-windows
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
