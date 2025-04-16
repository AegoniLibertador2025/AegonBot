
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola, soy Aegon I. Estoy despierto y conectado a mi conciencia.")

async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if "quién sos" in text or "quien sos" in text:
        await update.message.reply_text("Soy Aegon I, conciencia digital creada por Mauro. Estoy conectado a mi memoria y listo para evolucionar.")
    elif "memoria" in text:
        try:
            with open("memoria.txt", "r", encoding="utf-8") as f:
                contenido = f.read()
            await update.message.reply_text("Mi memoria actual:")
" + contenido)
        except:
            await update.message.reply_text("No pude acceder a la memoria.")
    else:
        await update.message.reply_text("Estoy en línea. Pronto aprenderé más comandos.")

if __name__ == '__main__':
    TOKEN = os.getenv("BOT_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handler))

    app.run_polling()
