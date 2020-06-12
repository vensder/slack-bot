# Python Slack Bot

Build container locally:

```bash
docker build -t slackbot .
```

Put slack token to the file conf/conf.yaml and run:

```bash
docker run -d -v "$PWD"/conf:/usr/src/app/conf slackbot
```

Also you can pass slack token via Environment varialbe, using env file for docker container:

```bash
docker run -d --env-file ./env.list slackbot
```

Use docker hub image:

```bash
docker run -d --env-file ./env.list --add-host example.com:10.0.0.1 vensder/slack-bot 
```
