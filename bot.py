# ==============================
# bot.py
# ==============================

import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes
)

from ai import get_ai_reply
from db import add_user, get_user, increment_count, can_user_chat
from payments import get_payment_message, make_user_premium

# Environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))


# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    add_user(update.effective_user.id)
    await update.message.reply_text(
        "🤖 Welcome to AI Bot!\n\n"
        "🆓 Free: 10 messages/day\n"
        "💎 Premium: Unlimited messages\n\n"
        "Use /premium to upgrade"
    )


# /premium command
async def premium(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        get_payment_message(),
        parse_mode="Markdown"
    )


# Admin command to upgrade user
async def makepremium(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("❌ Unauthorized")
        return

    try:
        user_id = int(context.args[0])
        make_user_premium(user_id)
        await update.message.reply_text("✅ User upgraded to Premium")
    except:
        await update.message.reply_text("❌ Usage: /makepremium USER_ID")


# Chat handler
async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user = get_user(user_id)

    if not can_user_chat(user):
        await update.message.reply_text(
            "❌ Daily limit reached.\nUse /premium to continue."
        )
        return

    reply = get_ai_reply(update.message.text)
    increment_count(user_id)
    await update.message.reply_text(reply)


# Start bot
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("premium", premium))
    app.add_handler(CommandHandler("makepremium", makepremium))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

    print("🤖 Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
