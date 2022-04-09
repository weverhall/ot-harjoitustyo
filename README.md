# Network Lookup App

Sovellus tarjoaa pääasiassa osoitteisiin liittyviä tietoverkkopalveluja:

- Domainin IP- ja saatavuushaku
- Oman IP- ja MAC-osoitteen nouto

## Dokumentaatio

- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)
- [Changelog](./dokumentaatio/changelog.md)

## Asennus

Asenna ensin sovelluksen riippuvuudet, sitten käynnistä se komennoilla:

```bash
poetry install
poetry run invoke start
```

## Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

Testikattavuusraportti tehdään komennolla:

```bash
poetry run invoke coverage-report
```