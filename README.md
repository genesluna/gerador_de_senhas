![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

# Gerador de Senha

Código fonte para para criação de testes unitários para o Projeto Integrador V-A do curso de Análise e Desenvolvimento de Sistemas EAD do CESMAC.

O aluno deve criar testes unitários que assegurem que o gerador de senhas:

- Deve gerar uma senha com tamanho correto.

- Deve gerar uma senha que inclui caracteres especiais se o critério for solicitado.

- Deve gerar uma senha que inclui letras maiúsculas se o critério for solicitado.

- Deve gerar uma senha que inclui letras minúsculas se o critério for solicitado.

- Deve gerar uma senha que inclui números se o critério for solicitado.

- Deve lidar corretamente com a ausência de escolha de critérios pelo usuário.

- Deve assegurar que o comprimento da senha é suficiente para incluir pelo menos um caractere de cada critério selecionado.

## Vídeo com explicação rápida do código

[![Vídeo com explicação rápida do código](https://img.youtube.com/vi/3YpYhR3wQJI/maxresdefault.jpg)](https://www.youtube.com/watch?v=3YpYhR3wQJI)

## Utilizando o código

Para iniciar a criação dos testes, é necessário clonar o projeto do GitHub:

```shell
git clone https://github.com/genesluna/gerador_de_senhas.git
```

## Rodando o código

```shell
python main.py --tamanho 12 --especiais --maiusculas --minusculas --numeros
```