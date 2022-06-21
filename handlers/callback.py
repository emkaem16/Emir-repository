from aiogram import Dispatcher, types
from aiogram.types import ParseMode, InlineKeyboardButton,InlineKeyboardMarkup

from config import bot, dp 






@dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton(
        "NEXT",
        callback_data='button_call_2',
    )
    markup.add(button_call_2)

    question = 'can you drive a car?'
    answers = [
        'yes', 'no', 'sometime', 'often'
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        is_anonymous=False,
        type='question',
        correct_option_id=0,
        explanation=" эу чуком как ты не будешь играть",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup,
    )

@dp.callback_query_handler(lambda call: call.data == "button_call_2")
async def quiz_3(call: types.CallbackQuery):


    question = 'choose one?'
    answers = [
        'yes', 'no', 'sometime', 'often'
    ]

    photo = open('media/problem1.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)


    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        is_anonymous=False,
        type='question',
        correct_option_id=0,
        explanation=" эу чуком как ты не будешь играть",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        
    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == "button_call_1")
    dp.register_callback_query_handler(quiz_3, lambda call: call.data == "button_call_2")