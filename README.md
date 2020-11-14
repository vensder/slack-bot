# Python Slack Bot

Build container locally:

```bash
docker build -t slackbot .
```

Pass slack token via Environment varialbe, using env file for docker container:

```bash
cat env.list
SLACK_TOKEN=xoxb-100000000001-1111111111111-INSERTTOKENHERE

docker run -d --env-file ./env.list slackbot
```

Use docker hub image:

```bash
docker run -d --env-file ./env.list --add-host example.com:10.0.0.1 vensder/slack-bot 
```
