from telegram import Update
from telegram.ext import ApplicationBuilder, ChatMemberHandler, ContextTypes

TOKEN = "8065966447:AAEfmJWG_JIGN038gZtftpzVTmg5bGF-wW8"

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = update.chat_member

    if result.new_chat_member.status == "member":
        user = result.new_chat_member.user
        chat = update.effective_chat

        members_count = await context.bot.get_chat_member_count(chat.id)

        name = user.first_name or "شهروند"

        text = f"{name} به شهری امن خوش اومدی!\n" \
               f"حالا ما {members_count} تا شهروندیم که تصمیم گرفتیم آگاهی مون رو بالا ببریم و یه شهر امن بسازیم!"

        await context.bot.send_message(chat.id, text)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(ChatMemberHandler(welcome, ChatMemberHandler.CHAT_MEMBER))

app.run_polling()

