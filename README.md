# Python Slack Bot

This Slack bot has two plugins. One of them helps to check the SSL certificate expiring for any accessible domain. Just send the message in the channel where the bot is invited like that:

`@botname !ssl date google.com`

Another plugin helps you to use IP calculator to check the IP addresses range, and so on. Just send the message to the bot like this:

`@botname !ipcalc 10.0.0.0/24`

Build image locally:

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
