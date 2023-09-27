from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Словарь с соответствиями комната -> файл фотографии
room_photos = {
    '1': 'rooms/1.png',

    '2': 'rooms/2.png',

    '3': 'rooms/3.png',

    '119': 'rooms/119.png',
    '122': 'rooms/122.png',
    '124': 'rooms/124.png',
    '126': 'rooms/126.png',
    '128': 'rooms/128.png',
    '134': 'rooms/134.png',
    '108': 'rooms/108-109.png',
    '109': 'rooms/108-109.png',

    '201': 'rooms/201.png',
    '207': 'rooms/207.png',
    '208': 'rooms/208.png',
    '210': 'rooms/210.png',
    '211': 'rooms/211.png',
    '218': 'rooms/218.png',
    '221': 'rooms/221.png',
    '222': 'rooms/222.png',
    '224': 'rooms/224.png',
    '226': 'rooms/226.png',

    '301': 'rooms/301.png',
    '305': 'rooms/305.png',
    '306': 'rooms/306.png',
    '308': 'rooms/308.png',
    '309': 'rooms/309.png',
    '310': 'rooms/310.png',
    '311': 'rooms/311.png',
    '314': 'rooms/314.png',
    '315': 'rooms/315.png',
    '317': 'rooms/317.png',
    '318': 'rooms/318.png',
    '319': 'rooms/319.png',
    '320': 'rooms/320.png',
    '323': 'rooms/323.png',


}


def help2(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('\n\U0001F47E:\n Вам нужно написать /kab [пробел] номер кабинета\n Пример: /kab 323 \n После вы получите фото и расположение кабинета \n Так же что бы посмотреть этаж нужно написать\n /kab [пробел][номер этажа]\n Пример: /kab 1')

def send_photo(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    command = update.message.text.split()[-1]  # Получаем команду после пробела
    photo_filename = room_photos.get(command)
    if photo_filename:
        photo = open(photo_filename, 'rb')
        context.bot.send_photo(chat_id, photo, caption=f'Фото кабинета {command}')
        photo.close()
    else:
        update.message.reply_text('Кабинет не найден')

def main() -> None:
    # Вместо 'YOUR_BOT_TOKEN' подставьте свой токен
    updater = Updater(token='6297955354:AAGN-1mDkpxFcviDRyZJ6qwuNj596zTCKhU')
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('kab', send_photo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
