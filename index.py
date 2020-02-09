import telebot
import random
from datetime import datetime

bot = telebot.TeleBot('985346176:AAE3S1OEv5yeY2V3dVSNSZmeLLxk9QNusyQ')
bus = (["9","46","50","53","60","73",'33'])
bus_code = [
    ["11072","11441","11568","11101","11095"],   #9 
    ["13018","13153"],   #46
    ["13072", "13079", "13038","13059","13066","13073"],  #50
    ["16014"],     #53
    ["11070", "11012",  "11219", "11071","11013","11028","11266","13113","13161"],  # 60
    ["11464","11496", "11408", "11396","11376","11372"],  #73
    ["136"]    #33
     ]
bus_num = (
     ["447BF01","097YL01","042BM01","275BT01","982AS01"],   #9
     ["141AT01","667AX01"],   #46
     ["780AL01", "Z954CA","Z435CA","Z540CA","Z684AU","Z922DA","723CA01","Z859CC"], #50
     ["839BM01"],    #53
     ["887AS01", "031AT01",  "048BA01", "896AS01","012AT01","102BO01","586BA01"],    #60
     ["272BO01","278BO01", "687BM01","587BM01","140BL01","855BL01"],  #73
     ["308BO01"]    #33
)
listbot = 't.me/listbusbot'

@bot.message_handler(commands=['start'])
def start_message(message):
          bot.send_message(message.chat.id, f'Отказ от ответственности: Здраствуйте, вы используете данную программу исключительно на свой страх и риск.\n\nСПИСОК ДОСТУПНЫХ АВТОБУСОВ ПРОВЕРЯЙТЕ В БОТЕ {listbot}')
          bot.delete_message(chat_id, message_id)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
     chatid = message.chat.id
     resp = message.text
     response = resp[2:5]
     randomFirst = random.randrange(299,999)
     randomSecond = random.randrange(1111,9999)
     curTime = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
     check = dict(zip([j for i in bus_code for j in i],[j for i in bus_num for j in i]))
     if message.text in check:
          bot.send_message(chatid, f"БИЛЕТ: 0{randomFirst}:38:{randomSecond}\nСУММА: 90 ТГ.\nДАТА: {curTime}\nТРАСНПОРТ: {resp} ({check[resp]})\nТЕЛ: 77762097977\nТРАНЗАКЦИЯ: 33853{randomSecond}\nТОО АСТАНА LRT\nhttps://smsbus.kz/cd.jsp?id=0{randomFirst}38{randomSecond}")
     else :
          bot.send_message(chatid,f"БИЛЕТ: 0{randomFirst}:38:{randomSecond}\nСУММА: 90 ТГ.\nДАТА: {curTime}\nТРАСНПОРТ: {resp} A{response} \nТЕЛ: 77762097977\nТРАНЗАКЦИЯ: 33853{randomSecond}\nТОО АСТАНА LRT\nhttps://smsbus.kz/cd.jsp?id=0{randomFirst}38{randomSecond}")


if __name__ == '__main__':
     bot.infinity_polling()
