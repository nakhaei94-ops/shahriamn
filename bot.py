from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8065966447:AAEfmJWG_JIGN038gZtftpzVTmg5bGF-wW8"

# پیام خوش‌آمدگویی برای کاربر جدید
async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.new_chat_members:
        member_count = await context.bot.get_chat_member_count(update.effective_chat.id)
        for member in update.message.new_chat_members:
            text = (
                f"{member.first_name} عزیز 🌿\n\n"
                f"به شهری امن خوش آمدی!\n"
                f"حالا ما {member_count} نفر هستیم که تصمیم گرفتیم آگاهی‌مان را بالا ببریم و یک شهر امن بسازیم!"
            )
            await update.message.reply_text(text)

# ساخت اپلیکیشن
app = ApplicationBuilder().token(TOKEN).build()

# اضافه کردن هندلر خوش‌آمدگویی
app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))

# اجرای ربات
app.run_polling()
