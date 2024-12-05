# Automação de Agendamento no Prenotami
Este script automatiza o processo de login e verificação de disponibilidade de agendamentos no site Prenotami, atualizando uma planilha no Google Sheets com as informações obtidas.

## Funcionalidades
* Realiza login no site Prenotami.
* Verifica a disponibilidade de serviços, como "Agendamento Primeiro Passaporte".
* Atualiza uma planilha do Google Sheets com o status de disponibilidade.
* Realiza várias tentativas automáticas em caso de falhas ou indisponibilidade.

## Pré-requisitos

### Python 3.8+

Bibliotecas necessárias (instale com pip):
* seleniumbase
* gspread
* oauth2client
* python-dotenv
  
## Gerenciamento de navegador:

O script utiliza o seleniumbase, que gerencia automaticamente o navegador (Chrome) e o ChromeDriver.
Não é necessário instalar ou configurar manualmente o ChromeDriver.

## Credenciais para Google Sheets:
Arquivo JSON com credenciais de uma conta de serviço do Google Cloud.
Variáveis de ambiente configuradas para acessar credenciais e planilha.

## Configuração

1. Criando o arquivo .env
Crie um arquivo .env na raiz do projeto com as seguintes variáveis:

.env:
GCHAVE=caminho/para/credenciais.json
SPREADSHEET_ID=id-da-planilha
MAIL=email-do-usuario
PASSWORD=senha-do-usuario
GCHAVE: Caminho para o arquivo JSON com as credenciais do Google.
SPREADSHEET_ID: ID da planilha do Google Sheets.
MAIL: E-mail usado para login no site Prenotami.
PASSWORD: Senha usada para login no site Prenotami.

2. Configurando o Google Cloud
Ative as APIs do Google Sheets e Google Drive no Google Cloud Console.
Crie um serviço de conta e baixe o arquivo JSON com as credenciais.
Compartilhe sua planilha do Google Sheets com o e-mail da conta de serviço.

3. Instalando dependências
Instale as bibliotecas necessárias com o seguinte comando:

pip install seleniumbase gspread oauth2client python-dotenv


## Como usar

Certifique-se de que o arquivo .env está configurado corretamente.
Execute o script com:
python login.py


## Estrutura do Script

### Principais Funções

#### realizar_tentativa()
* Faz login no site Prenotami.
* Verifica a disponibilidade de serviços.
* Atualiza uma planilha do Google Sheets com o status obtido.

#### chamar_tentativa()
* Gerencia o número de tentativas automáticas em caso de falhas ou indisponibilidade.
* Repetição de Tentativas
* O script realiza múltiplas tentativas até ser bem-sucedido ou alcançar o limite configurado.

## Notas
* O seleniumbase gerencia automaticamente o navegador (Chrome) e o ChromeDriver.
* Não é necessário instalar ou configurar o ChromeDriver manualmente.
* O script opera no modo headless (sem exibição do navegador).
* Inclua intervalos entre as tentativas para evitar bloqueios por parte do site.
* Certifique-se de que o site Prenotami está acessível no momento da execução.
