from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
from dotenv import load_dotenv
import os
#import undetected_chromedriver as uc
#from undetected_chromedriver import ChromeOptions
from seleniumbase import Driver


load_dotenv()

gchave = os.getenv('GCHAVE')
spreadsheet_id = os.getenv('SPREADSHEET_ID')
adress = os.getenv('MAIL')
password = os.getenv('PASSWORD')

# Configuração do Selenium para rodar em modo headless
driver = Driver(uc=True, headless=True)

# Configuração do Selenium
#service = Service("chromedriver/chromedriver.exe")  # Substitua pelo caminho do ChromeDriver


def realizar_tentativa():
    # Configuração do escopo e autenticação
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(gchave, scope)
    client = gspread.authorize(creds)

    # Acessar a planilha pelo ID
    spreadsheet = client.open_by_key(spreadsheet_id)

    # Acessar a primeira aba da planilha
    worksheet = spreadsheet.sheet1
    
    try:
        # Abrir o site
        driver.get("https://prenotami.esteri.it/Services")  # Substitua pela URL do site

        # Aguardar o carregamento da página
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "login-form"))
        )

        # Localizar e preencher o campo de e-mail
        email_field = driver.find_element(By.ID, "login-email")
        email_field.clear()
        email_field.send_keys(adress)  # Substitua pelo e-mail desejado

        # Localizar e preencher o campo de senha
        password_field = driver.find_element(By.ID, "login-password")
        password_field.clear()
        password_field.send_keys(password)  # Substitua pela senha desejada

        # Submeter o formulário
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()

        # Validar sucesso do login com base em um elemento presente na página pós-login
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "dataTableServices_wrapper"))
        )
        print("Login realizado com sucesso!")

        # Aguardar até que a tabela seja carregada
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "dataTableServices"))
        )

        # Encontrar todas as linhas da tabela
        rows = driver.find_elements(By.CSS_SELECTOR, "#dataTableServices tbody tr")

        for row in rows:
            # Verificar se a linha contém o texto "Agendamento Primeiro Passaporte"
            if "Agendamento Primeiro Passaporte" in row.text:
                # Localizar o botão "Reservar" dentro dessa linha e clicar
                reservar_button = row.find_element(By.CSS_SELECTOR, "button.button.primary")
                reservar_button.click()
                print("Botão 'Reservar' clicado com sucesso!")

                # Após clicar, verificar o HTML da página para o texto
                WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.TAG_NAME, "body"))  # Certifica-se que a página atualizou
                )
                page_source = driver.page_source

                if "Unavailable" in page_source:
                    print("HTML 'Unavailable' detectado. Tentando novamente...")
                    return False  # Indica que o processo deve ser repetido

                if "Sorry, all appointments for this service are currently booked" in page_source:
                    print("Não há vagas")
                    # Escrever em uma célula
                    worksheet.update_cell(1, 2, "Nao ha vagas")
                    print("Atualização realizada com sucesso!")
                else:
                    print("Ha vagas")
                    # Escrever em uma célula
                    worksheet.update_cell(1, 2, ">>> ATENCAO! Há vagas <<<")
                    worksheet.update_cell(1, 3, "Liberou alguma vez")
                    print("Atualização realizada com sucesso!")
                return True  # Sucesso, pode sair do loop

        print("Linha com 'Agendamento Primeiro Passaporte' não encontrada.")
        return False  # Repetir se não encontrar a linha

    except Exception as e:
        print(f"Erro durante a execução: {e}")
        return False  # Repetir em caso de erro

# Repetir até que o processo seja bem-sucedido com um máximo de 5 tentativas
def chamar_tentativa():
    i = 0
    while not realizar_tentativa() and i < 5:
        print("Reiniciando tentativa...")
        time.sleep(30)  # Aguarda alguns segundos antes de tentar novamente
        i += 1
    return i < 5

# Acionar a chamada de tentativa 5 vezes
for i in range(0, 4, 1):
    print(f"Tentativa {i+1}")
    if chamar_tentativa():
        print("Tentativa bem-sucedida. Encerrando o script.")
        break  # Sai do loop principal ao encontrar uma tentativa bem-sucedida
    time.sleep(300)

# Fechar o navegador no final
driver.quit()


