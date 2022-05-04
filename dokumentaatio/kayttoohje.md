# Käyttöohje

## Valmistelut

- [Tarkista](https://wiki.python.org/moin/BeginnersGuide/Download), että Python-versiosi on 3.8 tai uudempi
- [Asenna](https://python-poetry.org/docs/#installation) Poetry koneellesi
- [Lataa](https://github.com/weverhall/ot-harjoitustyo/releases/tag/viikko6) ja pura sovelluksen viimeisin GitHub release

Siirry vielä komentorivillä "ot-harjoitustyo" kansioon, niin olet valmis suorittamaan Poetry-komentoja.

## Käynnistys

Asenna riippuvuudet, alusta tietokanta ja käynnistä sovellus:

```bash
poetry install
poetry run invoke build
poetry run invoke start
```

## Navigointi ja toiminnallisuus

Aloitusnäkymässä käyttäjälle näkyy keskeisimmät verkkosovitinosoitteet sekä kaksi nappia: Domain Lookup ja Domain History.

Domain Lookup -nappia painaessa siirrytään näkymään, jossa voi antaa domainin joko IP- tai nimimuotoisena. Domainin ollessa varattu, näytetään sen tietoja ja samalla tallennetaan ne automaattisesti tietokantaan. Tietoja tallentuu vain, jos samannimistä domainia ei ole haettu samana päivänä. Tietty domainhaku tallentuu siis vain kerran päivässä toiston estämiseksi.

Domain History -napilla pääsee näkemään kyseisiä taulukkotietoja (haettu domain, sen erimuotoinen osoite, latenssi ja hakupäivämäärä). Tiedot on järjestetty taulukossa ensisijaisesti päivämäärän mukaan ja toissijaisesti haetun domainin ensimmäisen aakkosen tai numeron mukaan. Näkymässä on Clear History -nappi, joka tyhjentää tietokannan.

Molemmista näkymistä pääsee takaisin aloitusnäkymään vasemmassa ylälaidassa sijaitsevaa nuolta painamalla.