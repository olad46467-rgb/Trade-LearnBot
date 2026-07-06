from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@dp.message(Command("start"))
async def start(message: Message):

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📢 Join TradeLearn Hub",
                    url="https://t.me/TradeLearnHub"
                )
            ],
            [
                InlineKeyboardButton(
                    text="✅ Verify",
                    callback_data="verify"
                )
            ]
        ]
    )

    await message.answer(
        "👋 Welcome to TradeLearn Bot!\n\n"
        "Please join our official channel first.",
        reply_markup=keyboard
    )
