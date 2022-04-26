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
