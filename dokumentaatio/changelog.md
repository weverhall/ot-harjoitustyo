# Changelog

## Viikko 3

- Tehty vielä vanhaa, onnetonta ja mahdollisesti riivattua reseptisovellusta

## Viikko 4

- Uuden projektin sarastus, eli tietoverkkosovelluksen alku
- Lisätty NetworkLookup-luokka, joka vastaa sovelluslogiikan koodista
  - Verkkotunnusten saatavuuden haku domain-nimen perusteella
    - Varatun verkkotunnuksen IP:n haku
  - Omien IP- ja MAC-osoitteiden nouto
    - IP määritelty joko yksityiseksi tai julkiseksi noudetun osoitteen perusteella
    - MAC määritelty joko LAA- tai UAA-tyyppiseksi
- Lisätty LookupView-luokka, joka vastaa UI-luokan kanssa em. perustoiminnallisuuden käyttöliittymäkomponenteista
- Lisätty TestLookupService-luokka sovelluslogiikan testejä varten

## Viikko 5

- Oikeasti hakee myös julkisen IP-osoitteen
  - Oletusarvoisesti näyttää sekä julkisen että yksityisen/paikallisen IP:n erikseen
  - IP:t määritelty joko IPv4- tai IPv6-tyyppisiksi
- Verkkotunnusten saatavuuden haku nyt myös IP:n perustella
  - Varatun IP:n tapauksessa noutaa FQDN:n
- Pingaa varattua domainia ja ilmoittaa latenssin

## Viikko 6

- Käyttöliittymää siistitty ja laajennettu
  - Nyt yhteensä kolme eri näkymää: MainView, LookupView ja HistoryView, joita hallinnoi UI-luokan koodi
- Lisätty hakuhistorian tallennus
  - Tietokannat alustetaan initialize_database-tiedostossa
  - Muu SQL-koodi löytyy HistoryRepository-luokasta, ja sen metodeja kutsutaan sovelluslogiikan NetworkLookup-luokasta

## Viikko 7

- Lisätty TestHistoryRepository-luokka tietokannan testeille
- Lisätty tarpeelliset tiedostot ja tiedostopolut testitietokantaa varten