# 🤖 Telegram Notifier en Python

Este proyecto te permite enviar mensajes de texto a tu chat personal (o a un grupo) de Telegram utilizando la API de Telegram y Python. 

---

## 🚀 ¿Qué hace?

- Envía mensajes de texto a Telegram con soporte Markdown
- Configuración rápida mediante un archivo `.env`
- Implementado con `requests` y sin frameworks pesados

---

## 🧰 Requisitos

- Python 3.7 o superior
- Un bot de Telegram (ver instrucciones abajo)
- Tu `chat_id` de Telegram
- Las siguientes bibliotecas instaladas:
  - `requests`
  - `python-dotenv`
  - `python-telegram-bot 13.5`

---

## 🛠 Instalación
```
Instala las dependencias:

pip install -r requirements.txt

Crea un archivo .env en el directorio raíz (puedes copiar el de ejemplo)
Rellena .env con tus credenciales

TELEGRAM_TOKEN=123456789:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
TELEGRAM_CHAT_ID=123456789
```

## Cómo crear tu bot de Telegram
1. Crear el bot con BotFather
```
Abre Telegram y busca @BotFather
Escribe /newbot
Ponle un nombre (por ejemplo: Alerta Diario)
Elige un nombre de usuario que termine en bot (por ejemplo: alertadiario_bot)
BotFather te dará un TOKEN, algo así: 123456789:ABC-DEF1234ghIkl-zyx57W2v1u123ew11

```

2. Obtener tu chat ID
```
La forma más rápida es usar @userinfobot:
En Telegram, busca @userinfobot
Haz clic en Iniciar o escribe /start
Te responderá con tu chat ID, como por ejemplo: Your Chat ID: 123456789
```
## Ejemplo de uso e integración

✅ Ejemplo completo de uso

```from telegram_bot import TelegramBot
from dotenv import load_dotenv
from datetime import datetime
import os

# Cargar las variables de entorno
load_dotenv()
EMAIL = os.getenv("EMAIL")
API_KEY = os.getenv("API_KEY")

# Crear una instancia del bot
bot = TelegramBot()
....
....
....
# Generar un mensaje en el apartado de órdenes
msg = f"📆 *Órdenes del día {datetime.now().strftime('%Y-%m-%d')}*\n\n"

if not orders["programBuy"] and not orders["programSell"]:
    msg += "ℹ️ *No se han generado órdenes para hoy.*"
    bot.send_message(msg)
else:
    # Añadir sección de compras
    msg += "🟢 *COMPRAR*\n"
    for order in orders["programBuy"]:
        precio = round(order['price'], 2)
        cantidad = int(round(order['amount'] / precio))
        msg += f"• {cantidad} acciones de {sp.symbols[order['id']]} a ${precio:.2f}\n"
        d.buy_limit(sp.symbols[order['id']], cantidad, precio)

    # Añadir sección de ventas
    msg += "\n🔴 *VENDER*\n"
    for order in orders["programSell"]:
        precio = round(order['price'], 2)
        cantidad = order['amount'] / precio
        msg += f"• {cantidad:.2f} acciones de {sp.symbols[order['id']]} a ${precio:.2f}\n"
        d.sell_limit(sp.symbols[order['id']], cantidad, precio)

    # Enviar el mensaje final a Telegram
    bot.send_message(msg)

```
📌 Resumen:

✅ Instancias TelegramBot()

✅ Construyes tu mensaje en texto

✅ Llamas a bot.send_message(mensaje)
¡Y listo! El mensaje llegará a tu chat de Telegram.

