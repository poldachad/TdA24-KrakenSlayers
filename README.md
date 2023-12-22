# Spuštění

### 1. Zapni si Docker Desktop debílku

### 2. No a potom jen stačí dát do terminálu v tom projektu toto: 

```
docker build . -t tda-flask
docker run -p 8080:80 -v ${PWD}:/app tda-flask
```

Aplikace bude přístupná na `http://127.0.0.1:8080` nebo na `http://localhost:8080`

#### Odevzdání
V rámci GitHub akce se aplikace automaticky odevzdává, jediné co je potřeba udělat je v rámci repozitáře si nastavit svůj vlastní [TEAM\_SECRET](https://tourdeapp.cz/vzdelavaci-materialy/2736-sablony-lokalni-deployment-a-odevzdani#:~:text=3.-,Team%20Secret,-Jd%C4%9Bte%20do%20Settings), který dostanete po registraci do soutěže.
