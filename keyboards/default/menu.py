from aiogram.types import ReplyKeyboardMarkup , KeyboardButton
menu = ReplyKeyboardMarkup (
    keyboard = [
        [
            KeyboardButton(text = "2E") ,
        ] ,

        [
            KeyboardButton(text = "4E") ,
            KeyboardButton(text = "3C")
        ],
    ],

    resize_keyboard = True
)

