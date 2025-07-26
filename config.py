BOT_TOKEN = "вставь_свой_токен_сюда"
GROUP_CHAT_ID = -1002593269045

MESSAGES = {
    "start": "👋 Привет, {name}! Вот твоя личная ссылка:
https://t.me/{bot_username}?start={user_id}",
    "write_message": "✍️ Напиши своё анонимное сообщение:",
    "message_sent": "✅ Сообщение отправлено!",
    "new_anonymous": "📩 Новое анонимное сообщение:

{0}",
    "payment_request": "💰 Хотите узнать, кто это? Оплатите 100₽ и нажмите кнопку ниже.",
    "payment_submitted": "⏳ Заявка на оплату отправлена администратору.",
    "payment_not_found": "❌ Платёж не найден.",
    "admin_payment_request": "📥 Пользователь @{username} оплатил в {time}.

Сообщение: {msg_id}",
    "sender_revealed": "👤 Отправитель: @{username}",
    "sender_not_found": "❌ Не удалось найти отправителя.",
    "payment_approved": "✅ Платёж подтвержден.",
    "confirm_payment_deprecated": "🔒 Для подтверждения оплаты нажмите кнопку под сообщением.",
    "message_not_found": "❌ Сообщение не найдено.",
}

BUTTONS = {
    "reveal_sender": "👀 Узнать отправителя (100₽)",
    "payment_done": "💸 Я оплатил(а)",
    "approve_payment": "✅ Одобрить оплату"
}
