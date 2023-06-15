# Project Ting

Este projeto consiste na implementação de um programa que simula um algoritmo de indexação de documentos semelhante ao utilizado pelo Google. O objetivo do programa é identificar ocorrências de termos em arquivos TXT. Ele é composto por dois módulos principais:

1. Módulo de Gerenciamento de Arquivos: Responsável por permitir o anexo de arquivos de texto no formato TXT.
2. Módulo de Buscas: Responsável por executar funções de busca nos arquivos anexados.

## Habilidades Exercitadas

Durante o desenvolvimento desse projeto, as seguintes habilidades serão exercitadas:

- Manipulação de Pilhas.
- Manipulação de Deque.
- Manipulação de Nós e Listas Ligadas.
- Manipulação de Listas Duplamente Ligadas.

## Linter

Para garantir a qualidade do código, o projeto utiliza o linter Flake8. Ele é responsável por verificar se o código está em conformidade com as boas práticas de desenvolvimento, tornando-o mais legível e fácil de manter. Para executar o linter localmente no projeto, siga as instruções abaixo:

```
python3 -m flake8
```

O Python também oferece um recurso chamado ambiente virtual, que permite que diferentes projetos com diferentes versões de bibliotecas sejam executados em sua máquina sem conflitos. Para utilizar esse recurso, siga as etapas a seguir:

1. Criar o ambiente virtual:
```
$ python3 -m venv .venv
```

2. Ativar o ambiente virtual:
```
$ source .venv/bin/activate
```

3. Instalar as dependências no ambiente virtual:
```
$ python3 -m pip install -r dev-requirements.txt
```

Com o ambiente virtual ativado, as dependências serão instaladas nesse ambiente.

> Lembre-se de ativar o ambiente virtual novamente sempre que voltar a trabalhar no projeto. Para desativá-lo, execute o comando "deactivate".

## Testes

Antes de executar os testes, certifique-se de que o ambiente virtual esteja ativado.

Para executar todos os testes, utilize o seguinte comando:
```
$ python3 -m pytest
```

Caso deseje executar apenas um arquivo de testes específico, utilize o comando a seguir, substituindo "nomedoarquivo" pelo nome do arquivo de teste desejado:
```
$ python3 -m pytest tests/nomedoarquivo.py
```

## Requisitos

A seguir, estão listados os requisitos a serem implementados no projeto:

1. Implementar uma fila para armazenar os arquivos que serão lidos.
2. Implementar uma função `txt_importer` no módulo `file_management` que seja capaz de importar notícias a partir de um arquivo TXT, utilizando "\n" como separador.
3. Implementar a função `process` no módulo `file_process`. Essa função deverá transformar o conteúdo da lista gerada pela função `txt_importer` em um dicionário que será armazenado dentro da fila.
4. Implementar uma função `remove` no módulo `file_process` capaz de remover o primeiro arquivo processado da fila.
5. Implementar uma função `file_metadata` no módulo `file_process` capaz de apresentar informações superficiais de um arquivo processado.
6. Implementar os testes para a classe

 `PriorityQueue` capaz de armazenar arquivos pequenos de forma prioritária.
7. Implementar uma função `exists_word` no módulo `word_search` que verifique a existência de uma palavra em todos os arquivos processados.
8. Implementar uma função `search_by_word` no módulo `word_search` que busque uma palavra em todos os arquivos processados.

## Conclusão

O projeto "Project Ting" consiste em simular um algoritmo de indexação de documentos utilizando arquivos TXT. Ao implementar esse programa, você poderá manipular arquivos, executar buscas e armazenar informações em filas. Certifique-se de seguir as boas práticas de desenvolvimento, como a utilização do linter e a realização de testes para garantir a qualidade do código.
