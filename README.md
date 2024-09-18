# Parsing GasPump tokens

<img src="https://docs.aiogram.dev/en/dev-3.x/_static/logo.png" width="80" height="80">

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
Congrats, you deploy the project locally, good luck in local development

## License
Please use my code according to [LICENSE](LICENSE)
