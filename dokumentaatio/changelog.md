# Changelog

## Viikko 3

- Tehty vielä vanhaa, onnetonta, riivattua ja aivan surkeaa reseptisovellusta

## Viikko 4

- Uuden loisteliaan projektin sarastus, eli tietoverkkosovelluksen alku
- Lisätty NetworkLookup-luokka, joka vastaa sovelluslogiikan koodista
  - Verkkotunnusten (engl. domain) saatavuuden haku isäntänimen (engl. hostname) perusteella
    - Varatun verkkotunnuksen IP:n haku
  - Omien IP- ja MAC-osoitteiden nouto
    - IP määritelty joko yksityiseksi tai julkiseksi noudetun osoitteen perusteella
    - MAC määritelty joko LAA- tai UAA-tyyppiseksi
- Lisätty LookupView-luokka, joka vastaa UI-luokan kanssa em. perustoiminnallisuuden käyttöliittymäkomponenteista
- Lisätty TestLookupService-luokka sovelluslogiikan testejä varten
