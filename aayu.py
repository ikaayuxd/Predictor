import random
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def predict(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args or not context.args[0].isdigit():
        await update.message.reply_text("Please provide a starting number, e.g. /predict 5")
        return
    
    start_num = int(context.args[0])
    count = 0
    current_num = start_num
    
    while count < 20:
        heart = random.choice(['❤️❤️', '💚💚'])
        await update.message.reply_text(f"{current_num} {heart}")
        current_num += 1
        count += 1
        await asyncio.sleep(2)  # async delay of 2 seconds

if __name__ == "__main__":
    bot_token = "8345110658:AAHYsW3BEEQhT8fELkcQlwUaAS9FPHUG3Ls"
    app = ApplicationBuilder().token(bot_token).build()
    
    app.add_handler(CommandHandler("predict", predict))
    
    print("Bot started...")
    app.run_polling()
