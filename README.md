# py_observabilidade

Teste técnico para montagem de um ambiente capaz de prover observabilidade e demonstrar capacidade técnica de criação do mesmo

### Sobre o Ambiente

### Como rodar

1. Clone o repositório e acesse o diretorio do projeto clonado
```shell
$ git clone https://github.com/Jhousyfran/py_observabilidade.git
$ cd py_observabilidade
```

2. Crie a rede observability com o comando
```shell
$ docker network create observability 
```

3. É necessário criar a pasta elasticsearch_data na máquina local manualmente para evitar erro de permissionamento
```shell
$ mkdir elasticsearch_data 
```

4. Agora sim, vamos subir os containers (Após rodar o comando aguarde alguns segundos para que as aplicações estejam disponíveis)
```shell
$ docker-compose up -d 
```
