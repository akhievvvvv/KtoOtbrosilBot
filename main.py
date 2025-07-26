import logging
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

from config import BOT_TOKEN, GROUP_CHAT_ID, MESSAGES, BUTTONS
from database import mark_paid, is_paid  # из предыдущего примера

logging.basicConfig(level=logging.INFO)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = MESSAGES["start"].format(
        name=user.first_name or "Пользователь",
        bot_username=context.bot.username,
        user_id=user.id,
    )
    await update.message.reply_text(text)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    text = update.message.text

    # Отправляем анонимное сообщение в группу с ID GROUP_CHAT_ID
    await context.bot.send_message(chat_id=GROUP_CHAT_ID, text=MESSAGES["new_anonymous"].format(text))

    keyboard = [
        [InlineKeyboardButton(BUTTONS["reveal_sender"], callback_data=f"reveal_{user_id}")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(MESSAGES["message_sent"], reply_markup=reply_markup)


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data.startswith("reveal_"):
        user_id = int(data.split("_")[1])
        if is_paid(user_id):
            # Предположим, что ты здесь покажешь ник отправителя, заглушка:
            username = "username"  # надо заменить реальной логикой
            await query.edit_message_text(MESSAGES["sender_revealed"].format(username=username))
        else:
            await query.edit_message_text(MESSAGES["payment_request"])

    elif data == "payment_done":
        # Отправить админам уведомление, что пользователь оплатил
        # Здесь нужно добавить логику уведомления админов
        await query.edit_message_text(MESSAGES["payment_submitted"])


async def confirm_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    mark_paid(user_id)
    await update.message.reply_text(MESSAGES["payment_approved"])


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("confirm_payment", confirm_payment))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()


if __name__ == '__main__':
    main()
