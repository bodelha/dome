# Dome - Estufa de desidratação inteligente


Este repositório contém o projeto **Dome**, desenvolvido para o **Projeto Interdisciplinar** do 4º semestre do curso de **Desenvolvimento de Software Multiplataforma** da **FATEC Franca**. "Dome" (estufa em italiano) tem como objetivo monitorar e controlar as condições de uma estufa de desidratação.

O projeto integra as disciplinas:

- Laboratório de Desenvolvimento Web
- Programação para Dispositivos Móveis I
- Internet das Coisas e Aplicações
- Estatística Aplicada

## Descrição do Projeto

A ideia central do projeto é monitorar variáveis como:

- **Temperatura** dentro e fora da estufa
- **Umidade** dentro e fora da estufa
- **Luminosidade**

Inicialmente, o projeto foca apenas no monitoramento desses dados. No entanto, uma evolução do projeto poderá incluir a criação de regras automatizadas, como:

- Ligar uma fonte de calor artificial quando a temperatura interna estiver abaixo de um certo limite.
- Acionar uma ventoinha para trocar o ar interno pelo externo baseado nas leituras de temperatura e umidade.

A estrutura do projeto é dividida em diferentes partes:

- **API**: Backend desenvolvido em Flask, responsável por gerenciar as interações entre o sistema e as diferentes aplicações (web e mobile). Utilizamos **marshmallow** para validação e serialização de dados.
- **App**: Aplicação web desenvolvida em React, que consome a API para visualização e interação dos dados.
- **Mobile**: Aplicativo mobile desenvolvido em React Native, que também consome a API para funcionalidades similares à versão web.
- **IoT Devices Simulator**: Simulação de dispositivos IoT utilizando o Wokwi, substituindo sensores e Arduino físicos.

### Simulação de Dispositivos IoT

A simulação é feita com o Wokwi, que permite a criação de um ambiente virtual para simular os dispositivos e sensores conectados à aplicação.

## Tecnologias Utilizadas

- **Backend (API)**: Flask com marshmallow para validação
- **Frontend (Web App)**: React
- **Mobile**: React Native
- **Simulador IoT**: Wokwi

## Instalação e Execução

### Clonando o repositório

```bash
git clone https://github.com/bodelha/dome.git
cd dome
git submodule init
git submodule update
```

### Rodando a aplicação

Com a extensão do [Wokwi](https://marketplace.visualstudio.com/items?itemName=Wokwi.wokwi-vscode) instalada e configurada com licença ativa, bem como o platformio funcionado:

1. Renomeie o arquivo `ESP32/src/config.example.h` para o diretório `ESP32/src/config.h`
2. Digite `cd ESP32` e tecle Enter
3. Digite `paltformio run` ou `pio run` e aperte Enter
4. Aperte F1 e Selecione a opção `Wokwi: Start Simulator` ou abra o `diagram.json`
5. Ajuste o `.env.sample`, no mínimo renomeando para `.env`,
6. Em outro terminal, no root do projeto, execute `docker compose up -d`

Esse comando vai subir:

- banco de dados relacional postgresql para persistência dos dados
- "banco" chave-valor memcache para cacheamento
- backend feito em Python exposto na porta 5000
- frontend construído com React diponível na porta 3000
- um broker mosquitto, em que o ESP32 publica mensagens
- um serviço "gateway" que consome as mensagens do MQTT e converte para o formato da API, fazendo requests POST e persistindo os dados.

Para minimizar as depêndencias com o wokwi e potenciais problemas de rede, uma série de dados é gerada durante o build da aplicação caso `ENV=development` no `.env`. Pela natureza do script e o fato de serem gerados dados para cada um minuto dos últimos 3 meses, a aplicação não fica estável e disponível instantaneamente.


### Desenvolvedores

- Isabela Oliveira - bodelha
- Kauê José - Kaue404
- Samuel Santos - Metronox
- Marcos Vinicius - MVHespanholo

## Referências

* [Secador Solar Embrapa](https://ainfo.cnptia.embrapa.br/digital/bitstream/doc/1145471/1/EmbrapaFlorestas-2022-ComunicadoTecnico479-1.pdf) acesso em 20/10/24