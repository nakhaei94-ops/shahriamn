from telegram import Update
from telegram.ext import ApplicationBuilder, ChatMemberHandler, ContextTypes

# توکن ربات رو مستقیم وارد کن
TOKEN = "8065966447:AAEfmJWG_JIGN038gZtftpzVTmg5bGF-wW8"

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cmu = update.chat_member
    if not cmu:
        return

    old_status = cmu.old_chat_member.status
    new_status = cmu.new_chat_member.status

    if new_status in ("member", "administrator") and old_status not in ("member", "administrator"):
        user = cmu.new_chat_member.user
        chat = update.effective_chat
        if not chat:
            return

        chat_obj = await context.bot.get_chat(chat.id)
        member_count = getattr(chat_obj, "member_count", None)

        text = (
            f"{user.first_name} عزیز 🌿\n\n"
            f"به شهری امن خوش آمدی!\n"
            f"حالا ما {member_count or 'چند'} نفر هستیم که تصمیم گرفتیم آگاهی‌مان را بالا ببریم و یک شهر امن بسازیم!"
        )

        await context.bot.send_message(chat_id=chat.id, text=text)

def main():
    if not TOKEN:
        raise RuntimeError("توکن ربات را در متغیر TOKEN قرار بده")

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(ChatMemberHandler(welcome, ChatMemberHandler.CHAT_MEMBER))
    app.run_polling()

if __name__ == "__main__":
    main()