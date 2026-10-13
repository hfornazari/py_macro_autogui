# py_macro_autogui 

py_macro_autogui tem a finalidade de gravar clicks e teclas sendo utilizadas em janelas do desktop e a reprodução desses itens gravados sob supervisão do usuário.

## Visão Geral

Resolve a questão de interações multiplas em janelas do desktop permitindo captura e reprodução.
Foi criado inicialmente para uso pessoal sem pretensão de ser executado em modo de produção!
as principais funcionalidades: 
-captura de clicks/teclas
-armazenamento da captura
-reprodução 

## Arquitetura

Diagrama simples ou descrição dos componentes.


## Pré-requisitos

- windows desktop com mouse e teclado 
- Python 3.12
- tkinter

- Bibliotecas
-   pynput
-   pyautogui
-   tkinter
-   threading
-   time
-   json
-   os

## Configuração

usa os arquivos requirements.txt


## Execução

Como iniciar localmente.
com comando 

.\run.bat que executará no mesmo diretorio o app.py depois de ler requirements e instalar no python local se for necessário instalar libs.

## Testes

F6 - iniciar a captura 
F8 - para captura e grava o arquivo da macro
F9 - executa arquivo de captura
F10 - Interrompe execução
ESC - sai da aplicação


## Estrutura do Projeto

pasta principal onde estão os arquivos
pasta macros/default.json arquivo de captura de instruções de clicks e teclas gravados

## Licença
NOT USE OR RESPONSIBILITIES THE SOFTWARE IS PROVIDADE AS-IS WITH NO GARANTIES OR WARRANTY. USE FOR YOUR OWN RISK
