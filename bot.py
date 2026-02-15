from telegram import Update, ChatPermissions
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8065966447:AAEfmJWG_JIGN038gZtftpzVTmg5bGF-wW8"


async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message.new_chat_members:

        # گرفتن تعداد اعضای گروه
        member_count = await context.bot.get_chat_member_count(update.effective_chat.id)

        for member in update.message.new_chat_members:

            text = (
                f"{member.first_name} عزیز 🌿\n\n"
                f"به شهری امن خوش اومدی!\n"
                f"حالا ما {member_count} تا شهروندیم که تصمیم گرفتیم آگاهی‌مون رو بالا ببریم و یه شهر امن بسازیم!"
            )

            await update.message.reply_text(text)

            # محدود کردن ارسال پیام
            permissions = ChatPermissions(can_send_messages=False)

            await context.bot.restrict_chat_member(
                chat_id=update.effective_chat.id,
                user_id=member.id,
                permissions=permissions
            )


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))

app.run_polling()
