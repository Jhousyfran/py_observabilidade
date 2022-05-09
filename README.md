# py_observabilidade

![tela](https://www.ufsm.br/app/uploads/sites/791/2021/06/ELK-1.png)

Teste técnico para montagem de um ambiente capaz de prover observabilidade e demonstrar capacidade técnica de criação do mesmo

### Sobre o Ambiente

#### Sobre a aplicação
* App python usando Django
* nginx

#### Sobre o ambiente de observabilidate
* **elasticsearch** - para indexação de dados e mecanismo de busca
* **kibana** - para visualização de dados, metricas, logs e etc (em forma de dashboards e etc)
* **metricbeat** - para coleta de métricas (cpu, memória e etc)
* **heartbeat** - para informações de dispinibilidade (uptime)
* **filebeat** - para coleta de logs
* **apm-server** - para monitoramento de desempenho de aplicativos em tempo real (solicitações HTTP internas e externas, consultas de banco de dados, chamadas para caches e etc)

### Como rodar

1. Clone o repositório e acesse o diretorio do projeto clonado
```shell
$ git clone https://github.com/Jhousyfran/py_observabilidade.git
$ cd py_observabilidade
```

2. Crie a rede **observability** com o comando
```shell
$ docker network create observability 
```

3. É necessário criar a pasta **elasticsearch_data** na máquina local manualmente para evitar erro de permissionamento
```shell
$ mkdir elasticsearch_data 
```

4. Agora sim, vamos subir os containers (Após rodar o comando aguarde alguns segundos para que as aplicações estejam disponíveis)
```shell
$ docker-compose up -d 
```

5. Para as aplicações

|APP|ENDEREÇO/PORTA|
|---|--------------|
|kibana| http://localhost:5601|
|app| http://localhost:8280|
