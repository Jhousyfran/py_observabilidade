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

|APP|ENDEREÇO/PORTA|DEMO (pra facilitar a vida e já sair usando)|
|---|--------------|----|
|kibana| http://localhost:5601| http://146.190.236.50:5601
|app| http://localhost:8280|http://146.190.236.50


#### Algo deu errado e agora??
1. Verifique se todos os containers estão rodando (principalmente elasticsearch). O esperado é algo semelhante ao demonstrado abaixo:
```shell
$ docker ps
CONTAINER ID   IMAGE                                                  COMMAND                  CREATED        STATUS          PORTS                                                 NAMES
3fda8bd7c008   py_observabilidade_nginx                               "/entrypoint.sh"         26 hours ago   Up 24 minutes   0.0.0.0:8280->80/tcp, :::8280->80/tcp                 nginx
4e001bd2193a   py_observabilidade_app                                 "python manage.py ru…"   26 hours ago   Up 24 minutes   0.0.0.0:8000->8000/tcp, :::8000->8000/tcp             appexample
0b6d6614ccdd   postgres                                               "docker-entrypoint.s…"   26 hours ago   Up 24 minutes   5432/tcp                                              py_observabilidade_db_1
61cf58be78bf   docker.elastic.co/beats/metricbeat:7.13.0              "/usr/bin/tini -- /u…"   26 hours ago   Up 23 minutes                                                         metricbeat
074a16a02853   docker.elastic.co/beats/heartbeat:7.13.0               "/usr/bin/tini -- /u…"   26 hours ago   Up 24 minutes                                                         heartbeat
9b1d0016c636   docker.elastic.co/kibana/kibana:7.13.0                 "/bin/tini -- /usr/l…"   26 hours ago   Up 24 minutes   0.0.0.0:5601->5601/tcp, :::5601->5601/tcp             kibana
3337661a0ccb   docker.elastic.co/elasticsearch/elasticsearch:7.13.0   "/bin/tini -- /usr/l…"   26 hours ago   Up 24 minutes   0.0.0.0:9200->9200/tcp, :::9200->9200/tcp, 9300/tcp   elasticsearch
18923e306197   docker.elastic.co/apm/apm-server-oss:7.13.0            "/usr/bin/tini -- /u…"   26 hours ago   Up 24 minutes   0.0.0.0:8200->8200/tcp, :::8200->8200/tcp             apm

```
3. Se o container **elasticsearch** não estiver rodando, é provavel que seja necessário da permissão ao diretório **elasticsearch_data**. Dentro da pasta do projeto clonado faça:
```
$ sudo chmod 775 -R elasticsearch_data
$ docker-compsoe up -d
```

4. O Passo anterior deve ser o suficiente para que o container volte a subir com sucesso! Caso contrario use o comando seguinte para investigar:
```
$ docker logs nome_do_container_desejado
```
