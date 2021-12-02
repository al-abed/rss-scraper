from celery import Celery
from celery.schedules import crontab #Schedules

import requests #Grabs data
from bs4 import BeautifulSoup #Parses XML
import json #Exports to outfile

from datetime import datetime

app = Celery('tasks')

app.conf.timezone = 'UTC'

app.conf.beat_schedule = {
    # executes every 1 minute
    'scraping-task-one-min': {
        'task': 'tasks.rss',
        'schedule': crontab(),
    },
    # # executes every 15 minutes
    # 'scraping-task-fifteen-min': {
    #     'task': 'tasks.rss',
    #     'schedule': crontab(minute='*/15')
    # },
    # # executes daily at midnight
    # 'scraping-task-midnight-daily': {
    #     'task': 'tasks.rss',
    #     'schedule': crontab(minute=0, hour=0)
    # }
}

#saves the scraped data
@app.task
def save(article_list):

    # timestamp and filename
    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')

    filename = 'rss-{}.json'.format(timestamp)

    # creating our articles file with timestamp
    with open(filename, 'w') as outfile:
        json.dump(article_list, outfile)

# scraping function
@app.task
def rss():
    article_list = []

    try:
        print('Started scraping')
        print('{}'.format('-' * 40))

        #Execute request and parse w/ XML
        r = requests.get('https://tools.cdc.gov/api/v2/resources/media/404952.rss')
        soup = BeautifulSoup(r.content, features='xml')

        #Only scrape the items that I want.
        articles = soup.findAll('item')

        # for each "item" I want, parse it into a list
        for a in articles:
            title = a.find('title').text
            description = a.find('description').text
            link = a.find('link').text
            published = a.find('pubDate').text

            # create an "article" object with the data
            # from each "item"
            article = {
                'title': title,
                'description': description,
                'link': link,
                'published': published,
                'created_at': str(datetime.now()),
                'source': 'CDC'
                }

            # append my "article_list" with each "article" object
            article_list.append(article)
        
        print('Successfully finished scraping')
        return save(article_list)
    except Exception as e:
        print('The scraping job failed. See exception:')
        print(e)
