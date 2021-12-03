# RSS Feed Scraper
<br>
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)]()
- - -

## Table of Contents

- [About](#about)
- [Dependencies](#dependencies)
- [Getting Started](#getting_started)
- [TO-DO](#to-do)
<br>

## About <a name="about"></a>
Task scheduled web scraping tool designed to pull RSS data into json format from any specified feed.

## Dependencies <a name="dependencies"></a>
Language:
+ Python (3.10)

Packages/Libraries:
+ [Celery](https://docs.celeryproject.org/en/stable/index.html) ~ Task Scheduler
+ [BeautifulSoup4](https://beautiful-soup-4.readthedocs.io/en/latest/) ~ HTML/XML Parser
+ [Requests](https://docs.python-requests.org/en/latest/) ~ Handles HTTP requests

Message Broker:
+ [RabbitMQ](https://www.rabbitmq.com/) ~ Sends messages for the Celery workers to execute

OPTIONAL:
If you are having issues running the code such as receiving an error along the lines of...
`"Are you missing an xml tree parser?"`
Then if you install the python library:
+ [lxml](https://lxml.de/index.html)
It should correct your issues.

## Getting Started <a name="getting_started"></a>
Essentially, you have to ensure that the RabbitMQ service is always running.
From there you may then just execute Celery commands in the terminal.

RabbitMQ - Starting the service
- - -
Windows: an application that you may run
Linux: (Debian/Ubuntu)
Start:
` $ sudo rabbitmq-server `
Shutdown:
` $ sudo rabbitmqctl shutdown `

Celery
- - -
` $ celery -A tasks worker -B -l INFO `

## TO-DO <a name="to-do"></a>
+ Implement the format for tasks to be retrieved from a list
+ Utilize selenium to scrape data other than RSS feeds
+ *More on the way*

#### [Inspiration](https://codeburst.io/automated-web-scraping-with-python-and-celery-ac02a4a9ce51)