# Python Slack Bot


```bash
sudo docker build -t slackbot .
```

Put slack token to the file conf/conf.yaml and run:

```bash
sudo docker run -d -v "$PWD"/conf:/usr/src/app/conf slackbot
```

Also you can use pass slack token via Environment varalbe, using env file for docker container:

```bash
sudo docker run -d --env-file ./env.list slackbot
```
