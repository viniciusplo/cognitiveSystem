# Memory and search engine

Esse projeto tem como objetivo servir de modulo de busca semantica e sistema de memoria para agentes. 

## Deploy
Para fazer deploy do sistema voce deve executar os seguintes comandos:

docker network create memory-engine
docker-compose -f docker-compose-qdrant.yml up --build -d
docker-compose up --build -d

## API

Os endpoints podem ser divididos em dois grupos

### vector search db

### graph search db

## qdrant - vector search engine

O gerenciador do Qdrant pode ser acessado em http://localhost:6333/

## Memgraph - graph-based memory engine

O gerenciador do Memgraph pode ser acessado em http://localhost:3000/