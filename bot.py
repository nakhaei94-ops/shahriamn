from telegram import Update
from telegram.ext import ApplicationBuilder, ChatMemberHandler, ContextTypes

TOKEN = "8065966447:AAEfmJWG_JIGN038gZtftpzVTmg5bGF-wW8"

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = update.chat_member

    # فقط وقتی عضو جدید شد
    if result.new_chat_member.status == "member":
        user = result.new_chat_member.user
        chat = update.effective_chat

        name = user.first_name or "شهروند"

        text = f"{name} به شهری امن خوش اومدی!\n" \
               f"فعلاً ربات پیام خوش‌آمد را تست می‌کند!"

        # پیام تست
        await context.bot.send_message(chat.id, text)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(ChatMemberHandler(welcome, ChatMemberHandler.CHAT_MEMBER))

app.run_polling()
