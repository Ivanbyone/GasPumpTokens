# Parsing GasPump tokens
<img src="https://www.python.org/static/img/python-logo.png" width="50" height="50">
<img src="https://docs.aiogram.dev/en/dev-3.x/_static/logo.png" width="50" height="50">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Docker_logo.png/220px-Docker_logo.png" width="50" height="50">

## Description
This usefull script can help cryptousers to recognize new tokens and buy them earlier then others.
The script use aiohttp library for regular requests (3 seconds) to identify new tokens. If you want to deploy script locally you can change time of regular requests.

## Local development
To deploy locally you should use Docker.
1. Copy git repo.
```
$ git clone https://github.com/Ivanbyone/GasPumpTokens
```
2. Create virtual environment and activate it.
3. Create .env file like as .env.example file, .
4. Create bot in [BotFather](https://web.telegram.org/a/#93372553) and replace chanel link in /find handler.
5. Add token to .env file.
6. Run some Docker commands.
```
$ docker build .
```
And...
```
$ docker run <image name>
```
Congrats, you deploy the project locally!

## License
Please use my code according to [LICENSE](LICENSE)
