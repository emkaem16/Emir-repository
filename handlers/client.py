from aiogram import types, Dispatcher
from aiogram.types import ParseMode, InlineKeyboardButton,InlineKeyboardMarkup

from config import bot
from keyboards.client_kb import start_markup


async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id,
    f"hello my ret {message.from_user.full_name}",
    reply_markup= start_markup)


async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton(
        "NEXT",
        callback_data='button_call_1'
    )
    markup.add(button_call_1)

    question = 'ты хочешь играть валейболл на плащаь?'
    answers = [
        'yes', 'no', 'sometime', 'often'
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        is_anonymous=False,
        type='question',
        correct_option_id=0,
        explanation=" эу чуком как ты не будешь играть",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    ) 


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])    
    dp.register_message_handler(quiz_1, commands=['quiz'])    
