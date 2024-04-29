#(©) AxomBotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ᴏᴡɴᴇʀ : <a href='https://t.me/AlwaysToHelpBot'>ᴀʟᴡᴀʏs ᴛᴏ ʜᴇʟᴘ</a>\n○ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ : <a href='https://t.me/AxomiyaXBuwari'>ᴀxᴏᴍɪʏᴀ ʙᴜᴡᴀʀɪ</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('🍁 ᴅᴀɪʟʏ ɢɪᴠᴇᴀᴡᴀʏ', url='https://t.me/+uKGKdbFE6O0yMDY1')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pas
