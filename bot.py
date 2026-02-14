from telegram import Update
from telegram.ext import ApplicationBuilder, ChatMemberHandler, ContextTypes

TOKEN = "8065966447:AAEfmJWG_JIGN038gZtftpzVTmg5bGF-wW8"

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = update.chat_member

    # وضعیت قبلی و جدید عضو
    old_status = result.old_chat_member.status
    new_status = result.new_chat_member.status

    # فقط وقتی که عضو جدید شده یا تازه به گروه اضافه شده
    if new_status in ("member", "administrator") and old_status not in ("member", "administrator"):
        user = result.new_chat_member.user
        chat = update.effective_chat

        # تعداد اعضای گروه
        member_count = await context.bot.get_chat_member_count(chat.id)

        # پیام خوش‌آمد
        text = (
            f"{user.first_name} عزیز 🌿\n\n"
            f"به شهری امن خوش آمدی!\n"
            f"حالا ما {member_count} نفر هستیم که تصمیم گرفتیم آگاهی‌مان را بالا ببریم و یک شهر امن بسازیم!"
        )

        await context.bot.send_message(chat.id, text)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(ChatMemberHandler(welcome, ChatMemberHandler.CHAT_MEMBER))

app.run_polling()
