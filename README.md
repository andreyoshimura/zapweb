# WhatsApp Web Automation - Telegram Invite

Script de automação para envio controlado de convites para grupo do Telegram via WhatsApp Web.

## ⚠️ Aviso

Uso por sua conta e risco. Automação pode violar os Termos de Serviço do WhatsApp.

---

## 📌 Funcionalidades

- Envio máximo de 5 mensagens por execução
- Intervalo aleatório entre 5 e 10 minutos
- Atualização automática da planilha após cada envio
- Estratégia de filtro de interesse (não envia link direto)
- Compatível com Firefox
- Resiliência contra mudanças no WhatsApp Web (simulação de teclado/mouse via pywhatkit)

---

## 📂 Estrutura do Projeto

├── main.py
├── contatos.xlsx
├── requirements.txt
└── README.md


---

## 📊 Estrutura da Planilha

Arquivo: `contatos.xlsx`

| Numero        | Status   |
|--------------|----------|
| 5511999999999 |         |
| 5511888888888 | Enviado |

- Numero: deve conter DDI + DDD + número
- Status: será atualizado automaticamente para "Enviado"

---

## 🚀 Instalação

1. Criar ambiente virtual:
