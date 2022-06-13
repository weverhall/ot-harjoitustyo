# NetLookApp

NetLookApp is a small, cross-platform program that finds domain's availability, IP, FQDN and ping. Domain information gets stored in an SQLite database.

In addition, the app retrieves your public and private IP, MAC address and address types.

## Preparation

- [Verify](https://wiki.python.org/moin/BeginnersGuide/Download) that your Python version is 3.8 or newer
- [Install](https://python-poetry.org/docs/#installation) Poetry
- [Download](https://github.com/weverhall/ot-harjoitustyo/releases/tag/final) and extract the latest GitHub-release

Using the command line, navigate to `ot-harjoitustyo` folder and you're ready to execute Poetry commands.

## Launch

Install dependencies, initialize database and start application:

```bash
poetry install
poetry run invoke build
poetry run invoke start
```

## UI

NetLookApp consists of three views:

![Main View](https://raw.githubusercontent.com/weverhall/ot-harjoitustyo/master/dokumentaatio/kuvat/main.png "Main View")

![Domain Lookup](https://raw.githubusercontent.com/weverhall/ot-harjoitustyo/master/dokumentaatio/kuvat/lookup.png "Domain Lookup")

![Domain History](https://raw.githubusercontent.com/weverhall/ot-harjoitustyo/master/dokumentaatio/kuvat/history.png "Domain History")
