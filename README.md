# scheduler

A tiny scheduler, using appengine cron. It just calls the configured URL on given schedule.

## Add task

1. Add 'RequestHandler' (task definition) and URL mapping in main.py 
2. Add 'schedule' to call that URL, in cron.yaml

## Deploy application

````bash
    gcloud auth login
    gcloud app deploy
````

## Upload cron jobs

To upload cron jobs, specify the cron.yaml as a parameter to the gcloud command

````bash
gcloud app deploy cron.yaml

````

## Verify cron setup

https://console.cloud.google.com/appengine/taskqueues/cron?tab=CRON