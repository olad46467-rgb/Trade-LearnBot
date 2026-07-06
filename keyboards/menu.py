from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

join_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📢 Join Channel",
                url="https://t.me/TradeLearn Hub"
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
