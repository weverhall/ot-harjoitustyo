# Testausdokumentti

Sovelluksen automatisoidut yksikkö- ja integraatiotestit on tehty unittestillä. Suorittaessa testejä niille luodaan oma, erillinen tietokantansa, jotta testien suorittaminen ei sekoittaisi ohjelman varsinaista tietokantaa.

## Yksikkö- ja integraatiotestaus

Testiluokka TestLookupService hoitaa sovelluslogiikasta vastaavan NetworkLookup-luokan testauksen. Testiluokkaan on injektoitu sekä HistoryRepository että NetworkLookup luokkien oliot, joiden avulla luodaan yhteys testitietokantaan ja suoritetaan integraatiotestejä.

Testiluokan TestHistoryRepository vastuulla on taas automaatiotestata tietokantaluokka HistoryRepository.

### Testauskattavuus

Käyttöliittymäkerrosta ja sovelluksen käynnistäviä tiedostoja index.py ja build.py lukuunottamatta testauksen haaraumakattavuus on 80%.

![Coverage Report](https://raw.githubusercontent.com/weverhall/ot-harjoitustyo/master/dokumentaatio/kuvat/coverage.png "Coverage Report")

Automaatiotestauksen ulkopuolelle jäivät Windows-spesifit koodiosiot useasta luokasta. Lisäksi oman IP- ja MAC-osoitteen oikeellisuuden testaus automaattisesti osoittautui haastavaksi.

Näiden osalta tehtiin kuitenkin laajahkoa järjestelmätestausta.

## Järjestelmätestaus

Järjestelmätason testejä on suoritettu manuaalisesti sekä Windowsilla että Linuxilla. Virhetilanteita on testattu mm. antamalla vääränlaisia syötteitä ja yrittämällä pingata pingauksen estäneitä tai rajusti lagaavia domaineja. Samalla on seurattu tietokantataulukon toimivuutta kyseisissä tilanteissa.
IP-noutojen oikeellisuudesta on varmistuttu vertaamalla tuloksia muiden IP-hakupalvelujen tuloksiin.
