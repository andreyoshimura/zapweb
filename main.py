import time
import random
import pandas as pd
import pywhatkit as kit
from datetime import datetime

# ==============================
# CONFIGURAÇÕES
# ==============================

EXCEL_FILE = "contatos.xlsx"
MAX_ENVIOS_POR_EXECUCAO = 5
WAIT_TIME = 30  # Tempo para carregar o WhatsApp Web (Firefox)
MIN_DELAY = 300  # 5 minutos (em segundos)
MAX_DELAY = 600  # 10 minutos (em segundos)

MENSAGEM = """Olá, tudo bem?

Estou organizando um grupo no Telegram com conteúdos exclusivos sobre [TEMA].

Você teria interesse em receber o link para participar?
"""

# ==============================
# FUNÇÕES
# ==============================

def carregar_contatos():
    """Carrega a planilha Excel."""
    try:
        df = pd.read_excel(EXCEL_FILE)
        return df
    except Exception as e:
        print(f"Erro ao carregar planilha: {e}")
        exit()


def salvar_planilha(df):
    """Salva imediatamente a planilha após cada envio."""
    try:
        df.to_excel(EXCEL_FILE, index=False, engine="openpyxl")
    except Exception as e:
        print(f"Erro ao salvar planilha: {e}")


def enviar_mensagem(numero, mensagem):
    """
    Envia mensagem via WhatsApp Web.
    Usa pywhatkit para simular teclado/mouse.
    """
    try:
        kit.sendwhatmsg_instantly(
            phone_no=numero,
            message=mensagem,
            wait_time=WAIT_TIME,
            tab_close=True,
            close_time=5
        )
        return True
    except Exception as e:
        print(f"Erro ao enviar para {numero}: {e}")
        return False


# ==============================
# EXECUÇÃO PRINCIPAL
# ==============================

def main():
    df = carregar_contatos()

    if "Numero" not in df.columns or "Status" not in df.columns:
        print("A planilha deve conter as colunas 'Numero' e 'Status'.")
        return

    contatos_pendentes = df[df["Status"] != "Enviado"]

    if contatos_pendentes.empty:
        print("Nenhum contato pendente.")
        return

    envios_realizados = 0

    for index, row in contatos_pendentes.iterrows():

        if envios_realizados >= MAX_ENVIOS_POR_EXECUCAO:
            print("Limite diário atingido.")
            break

        numero = str(row["Numero"]).strip()

        print(f"[{datetime.now()}] Enviando para {numero}...")

        sucesso = enviar_mensagem(numero, MENSAGEM)

        if sucesso:
            df.at[index, "Status"] = "Enviado"
            salvar_planilha(df)
            envios_realizados += 1
            print(f"Mensagem enviada para {numero}")

            if envios_realizados < MAX_ENVIOS_POR_EXECUCAO:
                delay = random.randint(MIN_DELAY, MAX_DELAY)
                print(f"Aguardando {delay // 60} minutos...")
                time.sleep(delay)

        else:
            print(f"Falha ao enviar para {numero}")

    print("Execução finalizada.")


if __name__ == "__main__":
    main()
