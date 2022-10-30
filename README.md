# Tour de App - Flask boiler plate

Šablona pro vývoj aplikace pro Tour de App společně s vytvořením a nahráním výstupu

## Lokální spuštění

### Python
#### Prerekvizity
- Python 3
- pipenv (`pip install --user pipenv` pro Windows, https://pypi.org/project/pipenv/#installation pro Linux dle distribuce) 
#### Spuštění
```
pipenv install
flask --app app/app.py init-db
flask --app app/app.py run
```     

### Docker 
#### Prerekvizity
- Docker
- (Windows) aktivovaný wsl2 

#### Spuštění
```
docker-build . -t tda-flask
docker run -p 8080:80 -v ${PWD}:/app tda-flask
```
## Odevzdání
V rámci GitHub akce se aplikace automaticky odevzdává, jediné co je potřeba udělat je v rámci repozitáře si nastavit svůj vlastní TEAM\_SECRET, který dostanete po registraci do soutěže