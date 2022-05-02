# Arkkitehtuurikuvaus

## Sovelluksen rakenne

Yleiskatsaus sovelluksen kolmitasoisesta kerrosarkkitehtuurista:

![Pakkauskaavio](https://raw.githubusercontent.com/weverhall/ot-harjoitustyo/master/dokumentaatio/kuvat/pakkauskaavio.png "Pakkauskaavio")

UI-pakkauksessa on käyttöliittymän, Services-pakkauksessa sovelluslogiikan ja Repositories-pakkauksessa tietokannan koodi.

### Sovelluslogiikka

```mermaid
classDiagram
    class NetworkLookup{   
        +domain_lookup(host)
        #domain_ping(host)
        +find_own_public_ip()
        +find_local_ip()
        +find_mac()
        +fetch_history()
        +clear_history()
    }
```

Hakutoiminto on eriytetty domain_lookup-funktioon ja sen alifunktioon domain_ping. Nimensä mukaisesti, domain_lookup-funktion vastuulla on domainin saatavuuden ja IP- tai FQDN-osoitteen nouto. Myös tietokantaan tallennus tapahtuu automaattisesti tässä funktiossa. Funktio kutsuu domain_pingiä selvittääkseen latenssin, jos domain osoittautui varatuksi.

Funktioista find-alkuiset hoitavat sovelluksen alkunäkymässä olevien verkkosovitinosoitteiden noudon.

Hakuhistoria voidaan noutaa taulukkoon ja poistaa tietokannasta history-metodien avulla, joilla kutsutaan history_repositorystä injektoituja toimintoja.

### Tietokantatoiminnot

```mermaid
classDiagram
    class HistoryRepository{   
        +fetch_all()
        +clear_all()
        +insert(host, address, ping)
    }
```

Pysyväistallennus on HistoryRepository-luokan vastuulla. Sovelluslogiikan NetworkLookup-luokka kutsuu HistoryRepository-luokan insert-metodia aina kun käyttäjä on hakenut varatun domainin. Näin se saadaan tallennetuksi initialize_database-tiedostossa alustettuun history-tietokantaan.

Historia voidaan poistaa käyttöliittymän napilla, joka kutsuu NetworkLookup-luokkaa, joka edelleen kutsuu HistoryRepository-luokan clear_all-metodia.

## Sovelluksen toimintalogiikka

### Domainhaku ja historian tallennus

```mermaid
sequenceDiagram
    actor User
    participant LookupView
    participant NetworkLookup
    participant HistoryRepository
    User->>LookupView: click enter after typing in name or ip
    LookupView->>NetworkLookup: domain_lookup("mooc.fi")
    NetworkLookup-->>LookupView: domain data
    NetworkLookup->>HistoryRepository: insert("mooc.fi", "35.228.16.220", "5")
```

### Historian poisto

```mermaid
sequenceDiagram
    actor User
    participant HistoryView
    participant NetworkLookup
    participant HistoryRepository
    User->>HistoryView: click clear history
    HistoryView->>NetworkLookup: clear_history()
    NetworkLookup->>HistoryRepository: clear_all()
```
