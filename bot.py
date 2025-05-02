from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters, JobQueue
from market_data import get_analysis, generate_chart, API_KEY
from signal_handler import send_to_telegram
import logging

TOKEN = "7450144082:AAE01axIqp8yUZ4xX2BxGJTOqGKGfe9KKjw"
AUTHORIZED_USER = "@POWERFULDANI"
AUTHORIZED_USER_ID = 5660835662  # باید با آی‌دی عددی جایگزین بشه

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SYMBOLS = ["EURUSD", "GBPUSD", "USDJPY"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.username != AUTHORIZED_USER.strip("@"):
        await update.message.reply_text("شما اجازه استفاده از این ربات را ندارید.")
        return
    await update.message.reply_text("سلام دانی عزیز! آماده‌ام برای تحلیل. بنویس: تحلیل EURUSD")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.username != AUTHORIZED_USER.strip("@"):
        return
    await update.message.reply_text("بنویس مثلاً: تحلیل EURUSD یا بزار من خودم واست تحلیل بفرستم!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.username != AUTHORIZED_USER.strip("@"):
        return

    text = update.message.text.lower()
    if "تحلیل" in text:
        symbol = text.replace("تحلیل", "").strip().upper()
        result = get_analysis(symbol)
        chart = generate_chart(symbol, API_KEY)
        if chart:
            await update.message.reply_photo(chart, caption=result)
        else:
            await update.message.reply_text(result + "
(نمودار پیدا نشد)")
    else:
        await update.message.reply_text("فرمت درست: تحلیل EURUSD")

async def auto_report(context: ContextTypes.DEFAULT_TYPE):
    for symbol in SYMBOLS:
        result = get_analysis(symbol)
        chart = generate_chart(symbol, API_KEY)
        await context.bot.send_photo(chat_id=AUTHORIZED_USER_ID, photo=chart, caption=result)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.job_queue.run_repeating(auto_report, interval=1800, first=10)
    app.run_polling()

if __name__ == "__main__":
    main()