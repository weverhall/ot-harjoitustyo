# Network Lookup App

Sovellus tarjoaa pääasiassa osoitteisiin liittyviä tietoverkkopalveluja:

- Domainin IP- ja saatavuushaku
- Oman IP- ja MAC-osoitteen nouto
- ...lisäominaisuudet WIP :)

## Dokumentaatio

- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
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

## Testaus

Suorita testit:

```bash
poetry run invoke test
```

Luo testikattavuusraportti htmlcov-hakemistoon:

```bash
poetry run invoke coverage-report
```

## Pylint

Tee [Pylint-tiedoston](./.pylintrc) määrittelemät kooditarkistukset:

```bash
poetry run invoke lint
```