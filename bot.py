import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

# ---------- CONFIG ----------
BOT_TOKEN = os.environ.get("BOT_TOKEN")  # Set this in Railway
ADMIN_CONTACT = os.environ.get("ADMIN_CONTACT", "@YourUsername")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

DISCLAIMER = (
    "⚠️ *Disclaimer*\n"
    "This bot provides free sports statistics and educational content only.\n"
    "We do NOT accept bets, hold funds, or operate any gambling service.\n"
    "Gambling involves risk. Must be 18+. Please play responsibly."
)

# ---------- HANDLERS ----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name or "friend"
    text = (
        f"👋 Hello {user}, welcome to *Betting VIP*!\n\n"
        "I share free sports stats, match analysis, and betting education.\n\n"
        f"{DISCLAIMER}\n\n"
        "Use /help to explore commands."
    )
    await update.message.reply_text(text, parse_mode="Markdown")


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "*Available Commands*\n"
        "/start – Welcome & disclaimer\n"
        "/help – This menu\n"
        "/tips – Today's free predictions\n"
        "/stats – Sports statistics\n"
        "/about – About this bot\n"
        "/disclaimer – Legal disclaimer\n"
        "/contact – Contact admin"
    )
    await update.message.reply_text(text, parse_mode="Markdown")


async def tips(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Educational/sample content only. Replace with your own analysis.
    text = (
        "📊 *Today's Free Predictions (Educational)*\n\n"
        "1️⃣ Team A vs Team B — Over 2.5 goals (analysis only)\n"
        "2️⃣ Team C vs Team D — Both teams to score\n"
        "3️⃣ Team E vs Team F — Draw no bet\n\n"
        "These are opinions for learning purposes, not financial advice.\n\n"
        f"{DISCLAIMER}"
    )
    await update.message.reply_text(text, parse_mode="Markdown")


async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "📈 *Sports Statistics*\n\n"
        "• Recent form guides\n"
        "• Head-to-head records\n"
        "• Home/away performance\n"
        "• Goal & scoring trends\n\n"
        "Data is for educational use only."
    )
    await update.message.reply_text(text, parse_mode="Markdown")


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "*About Betting VIP*\n\n"
        "Betting VIP is an educational Telegram bot that shares free sports "
        "statistics and analysis. We do not operate a gambling service and do "
        "not accept or facilitate real-money bets."
    )
    await update.message.reply_text(text, parse_mode="Markdown")


async def disclaimer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(DISCLAIMER, parse_mode="Markdown")


async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"For questions, contact: {ADMIN_CONTACT}"
    )


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Unknown command. Type /help to see the list."
    )


# ---------- MAIN ----------
def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN environment variable is not set.")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("tips", tips))
    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("disclaimer", disclaimer))
    app.add_handler(CommandHandler("contact", contact))

    logger.info("Bot is starting...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
