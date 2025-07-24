from telegram import TelegramBot

bot = TelegramBot()

# Enviar mensaje de texto
bot.send_message("👋 Hola desde *Python* usando TelegramBot!", markdown=True)


