# Bot de Negociação de Bitcoin (BTC)

Este projeto é um bot de negociação automática de Bitcoin (BTC) que utiliza a API WebSocket da Bitstamp para monitorar o preço do BTC/USD em tempo real e executar ordens de compra e venda com base em limites de preço predefinidos.

## Funcionalidades

* **Conexão WebSocket:** Conecta-se ao feed de dados em tempo real da Bitstamp via WebSocket.
* **Monitoramento de Preço:** Analisa as mensagens recebidas para extrair o preço atual do BTC.
* **Lógica de Negociação Simples:**
    * Vende BTC se o preço ultrapassar US$ 10.000.
    * Compra BTC se o preço cair abaixo de US$ 8.100.
    * Aguarda novas atualizações de preço caso contrário.
* **Execução de Ordens:** Utiliza a API de negociação da Bitstamp para enviar ordens de compra e venda.
* **Tratamento de Erros:** Inclui blocos `try...except` para lidar com possíveis erros.
* **Segurança:** Utiliza variáveis de ambiente para armazenar credenciais da API.

## Pré-requisitos

* Python 3.6 ou superior
* Bibliotecas Python:
    * `websocket-client`
    * `bitstamp`
* Credenciais da API Bitstamp (USERNAME, KEY, SECRET)

## Instalação

1.  Clone o repositório:

    ```bash
    git clone [https://github.com/dolthub/dolt](https://github.com/dolthub/dolt)
    ```

2.  Instale as dependências:

    ```bash
    pip install websocket-client bitstamp
    ```

3.  Configure as variáveis de ambiente:

    * Defina as variáveis `BITSTAMP_USERNAME`, `BITSTAMP_KEY` e `BITSTAMP_SECRET` com suas credenciais da Bitstamp.

## Uso

1.  Execute o script:

    ```bash
    python nome_do_script.py
    ```

## Observações Importantes

* Este bot utiliza uma estratégia de negociação simples e pode não ser adequado para todos os cenários de mercado.
* A negociação de criptomoedas envolve riscos significativos. Negocie com responsabilidade.
* A quantidade de BTC que sera comprada ou vendida, pode ser alterada na variavel quantidade.
* Recomenda-se adicionar uma estrategia mais robusta, e um sistema de stop-loss, para minimizar os riscos.

## Melhorias Futuras

* Implementar estratégias de negociação mais sofisticadas.
* Adicionar um mecanismo de stop-loss.
* Implementar lógica de reconexão para o WebSocket.
* Adicionar logs para monitorar o comportamento do bot.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir pull requests para adicionar novas funcionalidades ou corrigir bugs.

## Licença

Este projeto é licenciado sob a [Licença MIT](LICENSE).
