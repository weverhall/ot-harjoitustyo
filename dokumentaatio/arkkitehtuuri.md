## Pakkauskaavio

Yleiskatsaus sovelluksen kolmitasoisesta kerrosarkkitehtuurista:

![Pakkauskaavio](https://raw.githubusercontent.com/weverhall/ot-harjoitustyo/master/dokumentaatio/kuvat/pakkauskaavio.png "Pakkauskaavio")

## Sovelluslogiikan pääluokka

```
classDiagram
    class NetworkLookup{   
        +domain_lookup(host)
        #domain_ping()
        +find_own_public_ip()
        +find_local_ip()
        +find_mac()
    }
```

## Verkkotunnuksen haku

```mermaid
sequenceDiagram
    actor User
    participant LookupView
    participant NetworkLookup
    participant LookupRepository
    User->>LookupView: type in domain/ip and click enter
    LookupView->>NetworkLookup: domain_lookup("mooc.fi")
    NetworkLookup-->>LookupView: domain data
    NetworkLookup->>LookupRepository: save_history("mooc.fi")
```
