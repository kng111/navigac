from PIL import Image, ImageDraw, ImageFont
import os

def generate_all_alphabet(font_name, alphabet, color=(0, 0, 255, 255)):
    output_dir_name = f"{font_name.split('.ttf')[0].split('/')[-1]}"
    try:
        os.makedirs(output_dir_name)
    except FileExistsError:
        pass
    fontsize = None
    font = None
    for letter in alphabet:
        img = Image.new('RGBA', (100, 100), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        if not fontsize or font:
            fontsize = 1
            font = ImageFont.truetype(font_name, fontsize)
            while font.getsize(letter)[0] < img.size[0] * 0.9 and font.getsize(letter)[1] < img.size[1] * 0.9:
                fontsize += 1
                font = ImageFont.truetype(font_name, fontsize)
            fontsize -= 1
            font = ImageFont.truetype(font_name, fontsize)

        letter_width, letter_height = font.getsize(letter)
        position = ((img.width - letter_width) // 2, (img.height - letter_height) // 2)
        draw.text(position, letter, fill=color, font=font)
        img.save(f"{output_dir_name}/letter_{letter}.png", "PNG")



# from pyrogram import Client
# from pyrogram.enums import ChatType

# from constants import emoji_alphabet


# def add_emoji_alphabet(font_name, api_id, api_hash, session_name):
#     with Client(session_name, api_id, api_hash) as client:
#         dialogs = client.get_dialogs()
#         stickers_chat_id = None
#         for dialog in dialogs:
#             chat = dialog.chat
#             if chat.type == ChatType.BOT and chat.username == "Stickers":
#                 stickers_chat_id = chat.id
#                 break
#         client.send_message(stickers_chat_id, "/start")
#         client.send_message(stickers_chat_id, "/newemojipack")
#         client.send_message(stickers_chat_id, "Статичные эмодзи")
#         client.send_message(stickers_chat_id, font_name)
#         for letter in emoji_alphabet.keys():
#             client.send_document(stickers_chat_id, f"{font_name}/letter_{letter}.png")
#             client.send_message(stickers_chat_id, emoji_alphabet[letter])
#         client.send_message(stickers_chat_id, "/publish")
#         client.send_message(stickers_chat_id, "/skip")
#         client.send_message(stickers_chat_id, font_name)

# emoji_alphabet = {'А': "😀", 'Б': "😃", 'В': "😄", 'Г': "😁"}