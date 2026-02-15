import asyncio

from telegram import Update, ChatPermissions
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    ChatMemberHandler,
    filters,
    ContextTypes,
)

TOKEN = "8065966447:AAEfmJWG_JIGN038gZtftpzVTmg5bGF-wW8"


async def delete_after_delay(message, delay=60):
    await asyncio.sleep(delay)
    try:
        await message.delete()
    except:
        pass


async def welcome_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.new_chat_members:
        member_count = await context.bot.get_chat_member_count(update.effective_chat.id)

        for member in update.message.new_chat_members:
            text = (
                f" درود {member.first_name} عزیز 🌿\n\n"
                f"به شهری امن خوش اومدی!\n"
                f"حالا ما {member_count} تا شهروندیم که تصمیم گرفتیم آگاهی‌مون رو بالا ببریم و یه شهر امن بسازیم!"
            )

            sent_message = await update.message.reply_text(text)

            # حذف بعد از 60 ثانیه
            asyncio.create_task(delete_after_delay(sent_message, 60))

            permissions = ChatPermissions(can_send_messages=False)
            await context.bot.restrict_chat_member(
                chat_id=update.effective_chat.id,
                user_id=member.id,
                permissions=permissions,
            )


async def welcome_chat_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = update.chat_member
    if result is None:
        return

    old_status = result.old_chat_member.status
    new_status = result.new_chat_member.status

    if old_status in ("left", "kicked") and new_status == "member":
        member = result.new_chat_member.user
        chat_id = result.chat.id

        member_count = await context.bot.get_chat_member_count(chat_id)

        text = (
            f" درود {member.first_name} عزیز 🌿\n\n"
            f"به شهری امن خوش اومدی!\n"
            f"حالا ما {member_count} تا شهروندیم که تصمیم گرفتیم آگاهی‌مون رو بالا ببریم و یه شهر امن بسازیم!"
        )

        sent_message = await context.bot.send_message(chat_id=chat_id, text=text)

        # حذف بعد از 60 ثانیه
        asyncio.create_task(delete_after_delay(sent_message, 60))

        permissions = ChatPermissions(can_send_messages=False)
        await context.bot.restrict_chat_member(
            chat_id=chat_id,
            user_id=member.id,
            permissions=permissions,
        )


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome_message))

app.add_handler(ChatMemberHandler(welcome_chat_member, ChatMemberHandler.CHAT_MEMBER))

app.run_polling(allowed_updates=["message", "chat_member"])
