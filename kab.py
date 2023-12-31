import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Замените 'YOUR_BOT_TOKEN' на реальный токен вашего бота
bot = telegram.Bot(token='6297955354:AAGN-1mDkpxFcviDRyZJ6qwuNj596zTCKhU')

# Функция для обработки команды /start
def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_html(
        fr"Привет, {user.mention_html()} какой кабинет ищешь?!",
        reply_markup=telegram.ReplyKeyboardMarkup([['223', '224']]),
    )

# Функция для обработки кастомных команд
def custom_command(update: Update, context: CallbackContext) -> None:
    text = update.message.text.lower()
    if text == '223':
        reply_text = "Второй этаж, крыло справа, кабинет слева"
    elif text == '124':
        reply_text = "Второй этаж, крыло справа, кабинет справа"
    else:
        reply_text = "Извините, я не понимаю эту команду."
    
    update.message.reply_text(reply_text)

# Основная функция для запуска бота
def main():
    # Замените 'YOUR_BOT_TOKEN' на реальный токен вашего бота
    updater = Updater(token='6297955354:AAGN-1mDkpxFcviDRyZJ6qwuNj596zTCKhU', use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, custom_command))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()



from telegram import Update, InputFile
from telegram.ext import Updater, CommandHandler, CallbackContext

# Обработчик команды /send_photo
def send_photo(update: Update, context: CallbackContext):
    # Отправляем фото с подписью
    photo = open('1.png', 'rb')
    caption = 'Это подпись к фото'
    update.message.reply_photo(photo=InputFile(photo), caption=caption)


def main():
    # Замените 'YOUR_BOT_TOKEN' на токен вашего бота
    updater = Updater(token='6297955354:AAGN-1mDkpxFcviDRyZJ6qwuNj596zTCKhU', use_context=True)

    dp = updater.dispatcher

    # Добавляем обработчик для команды /send_photo
    dp.add_handler(CommandHandler('start', send_photo))

    # Запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
