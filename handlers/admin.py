from re import A
from aiogram import types, Dispatcher
from config import bot, ADMIN

async def ban(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id not in ADMIN:
            await message.answer("you are not my boss")
        if not message.reply_to_message:
            await message.answer("commands have to reply to message")   
        else:
            await message.bot.kick_chat_member(message.chat.id, 
            user_id=message.reply_to_message.from_user.id)
            await message.answer(f" user {message.reply_to_message.from_user.full_name} "
            f"was ban with {message.from_user.full_name} ")     
    else:
        await message.answer(" its work only in group")


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=['ban'], commands_prefix="!/")        