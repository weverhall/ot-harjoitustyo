# Käyttöohje

## Valmistelut

- [Tarkista](https://wiki.python.org/moin/BeginnersGuide/Download), että Python-versiosi on 3.8 tai uudempi
- [Asenna](https://python-poetry.org/docs/#installation) Poetry koneellesi
- [Lataa](https://github.com/weverhall/ot-harjoitustyo/releases/tag/final) ja pura sovelluksen viimeisin GitHub-julkaisu

Siirry vielä komentorivillä `ot-harjoitustyo` kansioon, niin olet valmis suorittamaan Poetry-komentoja.

## Käynnistys

Asenna riippuvuudet, alusta tietokanta ja käynnistä sovellus:

```bash
poetry install
poetry run invoke build
poetry run invoke start
```

## Navigointi

Aloitusnäkymässä käyttäjä näkee keskeisimmät verkkosovitinosoitteensa sekä kaksi nappia: Domain Lookup ja Domain History.

![Main View](https://raw.githubusercontent.com/weverhall/ot-harjoitustyo/master/dokumentaatio/kuvat/main.png "Main View")

Domain Lookup -nappia painaessa siirrytään näkymään, jossa voi antaa domainin joko IP- tai nimimuotoisena. Domainin ollessa varattu, näytetään sen tietoja ja samalla tallennetaan ne automaattisesti tietokantaan. 

![Domain Lookup](https://raw.githubusercontent.com/weverhall/ot-harjoitustyo/master/dokumentaatio/kuvat/lookup.png "Domain Lookup")

Domain History -napilla pääsee näkemään kyseisiä taulukkotietoja (haettu domain, sen erimuotoinen osoite, latenssi ja hakupäivämäärä). Näkymässä on Clear History -nappi, joka tyhjentää tietokannan.

![Domain History](https://raw.githubusercontent.com/weverhall/ot-harjoitustyo/master/dokumentaatio/kuvat/history.png "Domain History")

Molemmista näkymistä pääsee takaisin aloitusnäkymään vasemmassa ylälaidassa sijaitsevaa nuolta painamalla.

## Tietokantataulukon yksityiskohdat

Tiedot on järjestetty taulukossa ensisijaisesti päivämäärän mukaan ja toissijaisesti haetun domainin ensimmäisen aakkosen tai numeron mukaan.

Toiston estämiseksi tietokantatauluun tallennetaan uusi rivi vain, jos samannimistä domainia ei ole haettu samana päivänä. Olemassa olevalle riville päivitetään kuitenkin viimeiseksi noudettu IP/FQDN ja latenssi.

Unix-pohjaisilla käyttöjärjestelmillä yli millisekunnin latenssi pyöristetään taulukossa yhden desimaalin tarkkuuteen ja alle millisekunnin latenssi kolmen desimaalin tarkkuuteen. Windowsilla latenssi on sovelluksessa aina (siis myös Domain Lookup -näkymässä) kokonaislukuna.
