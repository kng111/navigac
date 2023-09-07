
    
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

def get_current_lesson():
    current_time = datetime.datetime.now().strftime("%H:%M")
    for lesson in schedule:
        if lesson["start_time"] <= current_time <= lesson["end_time"]:
            return lesson
    return None

def start(update: Update, context: CallbackContext):
    schedule_text = """ 👾:Вас приветствует телеграмм бот навигатор\n
      Для ознакомления функционала бота советуем воспользоваться /help\n
      """
    update.message.reply_text(schedule_text)

def help(update: Update, context: CallbackContext):
    schedule_text = """ 👾:Общие команды бота:\n 
    /time - Какой сейчас урок,когда он закончится,сколько будет длиться переменна\n 
    /time1 - Расписание звонков (по урокам)\n 
    /time2 - Расписание звонков (по парам)\n
    Удачного пользования 🎈\n"""
    update.message.reply_text(schedule_text)

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
    5. Пара: 16:30 - 18:05
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
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('time', time1))
    dp.add_handler(CommandHandler('time1',send_schedule1))
    dp.add_handler(CommandHandler('time2',send_schedule2))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
