
    
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime

# Устанавливаем уровень логирования (необязательно)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Определяем расписание звонков
schedule = [
    {"lesson": "1. Урок", "start_time": "09:00", "end_time": "09:45"},
    {"lesson": "2. Урок", "start_time": "09:50", "end_time": "10:35"},
    {"lesson": "3. Урок", "start_time": "10:45", "end_time": "11:30"},
    {"lesson": "4. Урок", "start_time": "11:35", "end_time": "12:20"},
    {"lesson": "5. Урок", "start_time": "13:00", "end_time": "13:45"},
    {"lesson": "6. Урок", "start_time": "13:50", "end_time": "14:35"},
    {"lesson": "7. Урок", "start_time": "14:45", "end_time": "15:30"},
    {"lesson": "8. Урок", "start_time": "15:35", "end_time": "16:20"},
    {"lesson": "9. Урок", "start_time": "16:30", "end_time": "17:15"},
    {"lesson": "10. Урок", "start_time": "17:20", "end_time": "18:05"}
]

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


def start(update: Update, context: CallbackContext):
    schedule_text = """  👾:Вас приветствует навигационнный телеграмм бот Физтеха\n\n Для ознакомления функционала бота советуем воспользоваться\n/zvonki для ознакомления с расписанием и звонками\n\n и /helpkab для навигации по колледжу \n с помощью команд /kab [номер кабинета]"""
    update.message.reply_text(schedule_text)


def helpkab(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("""\n\U0001F47E:\nВам нужно написать /kab [пробел] номер кабинета\n \nПример: /kab 323 \n После вы получите фото и расположение кабинета 
                              \nТак же что бы посмотреть этаж нужно написать\n /kab [пробел][номер этажа]\n Пример: /kab 1""")


def zvonki(update: Update, context: CallbackContext):
    schedule_text = """ 👾:Команды звонков бота:\n 
    /time - Какой сейчас урок,когда он закончится,сколько будет длиться переменна\n 
    /time1 - Расписание звонков (по урокам)\n 
    /time2 - Расписание звонков (по парам)\n
    Удачного пользования 🎈\n"""
    update.message.reply_text(schedule_text)


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




def get_current_lesson():
    current_time = datetime.datetime.now().strftime("%H:%M")
    for lesson in schedule:
        if lesson["start_time"] <= current_time <= lesson["end_time"]:
            return lesson
    return None





def send_schedule1(update: Update, context: CallbackContext):
    # Здесь вы можете добавить код для получения актуального расписания
    # Например, считывание данных из файла или отправка запроса к какому-либо источнику
    schedule_text = """🔔 Расписание звонков:\n
    1. Урок: 09:00 - 09:45\n
    2. Урок: 09:50 - 10:35\n
    3. Урок: 10:45 - 11:30\n
    4. Урок: 11:35 - 12:20\n
    5. Урок: 13:00 - 13:45\n
    6. Урок: 13:50 - 14:35\n
    7. Урок: 14:45 - 15:30\n
    8. Урок: 15:35 - 16:20\n
    9. Урок: 16:30 - 17:15\n
    10. Урок: 17:20 - 18:05\n

    \n (Для поиска кабинета /helpkab)
    """
    
    update.message.reply_text(schedule_text)


def send_schedule2(update: Update, context: CallbackContext):
    # Здесь вы можете добавить код для получения актуального расписания
    # Например, считывание данных из файла или отправка запроса к какому-либо источнику
    schedule_text = """🔔 Расписание звонков:\n
    1. Пара: 09:00 - 10:35\n
    2. Пара: 10:45 - 12:20\n
    3. Пара: 13:00 - 14:35\n
    4. Пара: 14:45 - 16:20\n
    5. Пара: 16:30 - 18:05\n
    \n (Для поиска кабинета /helpkab)
    """
    
    update.message.reply_text(schedule_text)

def time1(update: Update, context: CallbackContext):
    current_lesson = get_current_lesson()
    if current_lesson:
        lesson = current_lesson["lesson"]
        end_time = current_lesson["end_time"]
        next_lesson_index = schedule.index(current_lesson) + 1
        if next_lesson_index < len(schedule):
            next_lesson_start_time = schedule[next_lesson_index]["start_time"]
            time_until_next_lesson = (
                datetime.datetime.strptime(next_lesson_start_time, "%H:%M")
                - datetime.datetime.strptime(end_time, "%H:%M")
            )
            update.message.reply_text(
                f"Вы сейчас на {lesson}\n"
                f"🔔 Урок закончится в {end_time}\n"
                f"Переменна будет длительностью в {str(time_until_next_lesson)[2:]} минут"
            )
        else:
            update.message.reply_text(
                f"Вы сейчас на {lesson}\n"
                f"Урок закончится в {end_time}\n"
                "Это последний урок сегодня.💡"
            )
    else:
        update.message.reply_text("Сейчас нет уроков.💡")

def main():
    # Замените 'YOUR_BOT_TOKEN' на ваш токен, который вы получили от BotFather
    updater = Updater(token='6297955354:AAGN-1mDkpxFcviDRyZJ6qwuNj596zTCKhU', use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))

    dp.add_handler(CommandHandler('zvonki', zvonki))
    dp.add_handler(CommandHandler('helpkab', helpkab))

    dp.add_handler(CommandHandler('time', time1))
    dp.add_handler(CommandHandler('time1',send_schedule1))
    dp.add_handler(CommandHandler('time2',send_schedule2))

    dp.add_handler(CommandHandler('kab', send_photo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
