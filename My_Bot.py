import requests
import vk_api
import time
import json
import sqlite3
import random
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
from enum import Enum


vk_session = vk_api.VkApi(token='token')


vk = vk_session.get_api()
longpol = VkLongPoll(vk_session)
db = sqlite3.connect('base_for_bot.db')
cur = db.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS Fit_Bot(
        nummer INTEGER,
        word TEXT,
        translation TEXT
        )""")
db.commit()
score = 0

def get_but(text, color):
        return{
                "action":{
                        "type": "text",
                        "payload": "{\"button\": \"" + "1" + "\"}",
                        "label": f"{text}"
                },
                "color": f"{color}"
        }

first_keyboard = {
        "one_time" : False,
        "buttons" : [
        [get_but('Меню', 'secondary')]]
 
        }
first_keyboard = json.dumps(first_keyboard, ensure_ascii = False).encode('utf-8')
first_keyboard = str(first_keyboard.decode('utf-8'))


keyboard = {
        "one_time" : False,
        "buttons" : [
        [get_but('1', 'positive'), get_but('2', 'positive'),
        get_but('3', 'positive'), get_but('4', 'positive'),
        get_but('Меню', 'negative')]
        ] 
}
keyboard = json.dumps(keyboard, ensure_ascii = False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))


menukeyboard = {
        "one_time" : False,
        "buttons" : [
        [get_but('О Боте', 'positive')], [get_but('Задание', 'primary')]    # Все цвета для кнопок: Синяя - primary, Белая - secondary, 
                                                                            #Красная - negative, Зелёная - positive
        ]
        }
menukeyboard = json.dumps(menukeyboard, ensure_ascii = False).encode('utf-8')
menukeyboard = str(menukeyboard.decode('utf-8'))





def menu_sender(id, text):
        vk_session.method('messages.send', {'user_id' : id, 'message' : text, 'random_id' : 0, 'keyboard' : menukeyboard})



def sender(id, text):
        vk_session.method('messages.send', {'user_id' : id, 'message' : text, 'random_id' : 0, 'keyboard' : keyboard})

def msg(id, text):
        vk_session.method('messages.send', {'user_id' : id, 'message' : text, 'random_id' : 0})

def to_menu(id, text):
        vk_session.method('messages.send', {'user_id' : id, 'message' : text, 'random_id' : 0, 'keyboard' : first_keyboard})

def menu():
        msg(id, 'Буду ждать тебя тут снова!)')
        menu_sender(id, 'Привет! Меня зовут Fit-Bot 🤖 Я могу помочь тебе лучше подготовиться к экзамену Fit. Вы находитесь в Меню.')

 




def main():
        for event in longpol.listen():
                if event.type == VkEventType.MESSAGE_NEW:
                        if event.to_me:
                                global request
                                request = event.text
                                global id
                                id = event.user_id
                                

                                if request == 'Меню':
                                        menu_sender(id, 'Привет! Меня зовут Fit-Bot 🤖 Я могу помочь тебе лучше подготовиться к экзамену Fit. Вы находитесь в Меню.')

                                elif request == 'О Боте':    
                                        id = event.user_id
                                        to_menu(id, '''
                                        На данный момент этот Бот находится на стадии разработки. Основная задумка заключается в том, чтобы создать помощника для подготовки к экзамену на немецком языке, который называется "Fit A2". Вся лексика взята из учебников по подготовке к этому экзамену. В данной версии Бота показаны основные принципы работы с ним, то есть созданы лишь пробники заданий.           
                                        ''')
                                
                                elif request == 'Задание':

                                        msg(id, 'В этом задании нужно подобрать правильный перевод слова на немецком языке. ')
                                        

                                        def exercise():
                                                


                                                
                                                
                                                                
                                                                
                                                global deutsch_words
                                                deutsch_words = []



                                                                        
                                                                                

                                                def right_first():
                                                        global id
                                                        sender(id, 'Слово на немецком 🇩🇪:')
                                                        number = random.randint(1,170)
                                                        deutsch_words.append(number)
                                                        right_number = number 
                                                        right_word = cur.execute("SELECT word FROM Fit_Bot WHERE nummer = ?", (number, ))
                                                        sender(id, right_word)

                                                        sender(id, 'Выбери правильный перевод 🇷🇺:')

                                                        one = cur.execute("SELECT translation FROM Fit_Bot WHERE nummer = ?", (right_number, ))
                                                        sender(id, one)

                                                        number = random.randint(1,170)
                                                        while number in deutsch_words:
                                                                number = random.randint(1,170)
                                                        deutsch_words.append(number)
                                                        two = cur.execute("SELECT translation FROM Fit_Bot WHERE nummer = ?", (number, ))
                                                        sender(id, two)

                                                        number = random.randint(1,170)
                                                        while number in deutsch_words:
                                                                number = random.randint(1,170)
                                                        deutsch_words.append(number)
                                                        three = cur.execute("SELECT translation FROM Fit_Bot WHERE nummer = ?", (number, ))
                                                        sender(id, three)

                                                        number = random.randint(1,170)
                                                        while number in deutsch_words:
                                                                number = random.randint(1,170)
                                                        deutsch_words.append(number)
                                                        four = cur.execute("SELECT translation FROM Fit_Bot WHERE nummer = ?", (number, ))
                                                        sender(id, four)


                                                        for event in longpol.listen():
                                                                        if event.type == VkEventType.MESSAGE_NEW:
                                                                                if event.to_me:
                                                                                        request = event.text
                                                                                        id = event.user_id

                                                                                        if request == '1':
                                                                                                reaction = random.randint(1, 10)
                                                                                                if reaction == 1:
                                                                                                        sender(id, 'Молодец!')
                                                                                                if reaction == 2:
                                                                                                        sender(id, 'Здорового! 👍🏻')
                                                                                                if reaction == 3:
                                                                                                        sender(id, 'Класс))')
                                                                                                if reaction == 4:
                                                                                                        sender(id, 'Toll!')
                                                                                                if reaction == 5:
                                                                                                        sender(id, 'Super💪🏻')
                                                                                                if reaction == 6:
                                                                                                        sender(id, 'Sehr gut!')
                                                                                                if reaction == 7:
                                                                                                        sender(id, 'У тебя хорошо получается!😎')
                                                                                                if reaction == 8:
                                                                                                        sender(id, 'Richtig)')
                                                                                                if reaction == 9:
                                                                                                        sender(id, 'Продолжай в том же духе 😀')
                                                                                                if reaction == 10:
                                                                                                        sender(id, 'Правильно!')
                                                                                                exercise()
                                                                                        elif request == 'Меню':
                                                                                                 
                                                                                                menu()
                                                                                                
                                                                                                        
                                                                                        else:
                                                                                                sender(id, 'К сожалению это не правильный ответ. Правильный ответ: ')
                                                                                                right_answer = cur.execute("SELECT translation FROM Fit_Bot WHERE nummer = ?", (right_number, ))
                                                                                                sender(id, right_answer)
                                                                                                time.sleep(4)
                                                                                                exercise()
                                                                                        break
                                                   

                                                                
                                                def right_second():
                                                        global id
                                                        sender(id, 'Слово на немецком 🇩🇪:')
                                                        number = random.randint(1,170)
                                                        deutsch_words.append(number)
                                                        right_number = number 
                                                        right_word = cur.execute("SELECT word FROM Fit_Bot WHERE nummer = ?", (number, ))
                                                        sender(id, right_word)

                                                        sender(id, 'Выбери правильный перевод 🇷🇺:')

                                                        number = random.randint(1,170)
                                                        while number in deutsch_words:
                                                                number = random.randint(1,170)
                                                        deutsch_words.append(number)
                                                        one = cur.execute("SELECT translation FROM Fit_Bot WHERE nummer = ?", (number, ))
                                                        sender(id, one)

                                                                        
                                                        two = cur.execute("SELECT translation FROM Fit_Bot WHERE nummer = ?", (right_number, ))
                                                        sender(id, two)

                                                        number = random.randint(1,170)
                                                        while number in deutsch_words:
                                                                number = random.randint(1,170)
                                                        deutsch_words.append(number)
                                                        three = cur.execute("SELECT translation FROM Fit_Bot WHERE nummer = ?", (number, ))
                                                        sender(id, three)

                                                        number = random.randint(1,170)
                                                        while number in deutsch_words:
                                                                number = random.randint(1,170)
                                                        deutsch_words.append(number)
                                                        four = cur.execute("SELECT translation FROM Fit_Bot WHERE nummer = ?", (number, ))
                                                        sender(id, four)

                                                        for event in longpol.listen():
                                                                        if event.type == VkEventType.MESSAGE_NEW:
                                                                                        if event.to_me:
                                                                                                request = event.text
                                                                                                id = event.user_id

                                                                                                if request == '2':
                                                                                                        reaction = random.randint(1, 10)
                                                                                                        if reaction == 1:
                                                                                                                sender(id, 'Молодец!')
                                                                                                        if reaction == 2:
                                                                                                                sender(id, 'Здорового! 👍🏻')
                                                                                                        if reaction == 3:
                                                                                                                sender(id, 'Класс))')
                                                                                                        if reaction == 4:
                                                                                                                sender(id, 'Toll!')
                                                                                                        if reaction == 5:
                                                                                                                sender(id, 'Super💪🏻')
                                                                                                        if reaction == 6:
                                                                                                                sender(id, 'Sehr gut!')
                                                                                                        if reaction == 7:
                                                                                                                sender(id, 'У тебя хорошо получается!😎')
                                                                                                        if reaction == 8:
                                                                                                                sender(id, 'Richtig)')
                                                                                                        if reaction == 9:
                                                                                                                sender(id, 'Продолжай в том же духе 😀')
                                                                                                        if reaction == 10:
                                                                                                                sender(id, 'Правильно!')
                                                                                                        exercise()
                                                                                                elif request == 'Меню':
                                                                                                      
                                                                                                        menu()
                                                                                                        
                                                                                                                
                                                                                                else:
                                                                                                        sender(id, 'К сожалению это не правильный ответ. Правильный ответ: ')
                                                                                                        right_answer = cur.execute("SELECT translation FROM Fit_Bot WHERE nummer = ?", (right_number, ))
                                                                                                        sender(id, right_answer)
                                                                                                        time.sleep(4)
                                                                                                        exercise()
                                                                                                break
                                                             

                                                def right_third():
                                                        global id
                                                        sender(id, 'Слово на немецком 🇩🇪:')
                                                        number = random.randint(1,170)
                                                        deutsch_words.append(number)
                                                        right_number = number 
                                                        right_word = cur.execute("SELECT word FROM Fit_Bot WHERE nummer = ?", (number, ))
                                                        sender(id, right_word)

                                                        sender(id, 'Выбери правильный перевод 🇷🇺:')


                                                        number = random.randint(1,170)
                                                        while number in deutsch_words:
                                                                number = random.randint(1,170)
                                                        deutsch_words.append(number)
                                                        one = cur.execute("SELECT translation FROM Fit_Bot WHERE nummer = ?", (number, ))
                                                        sender(id, one)

                                                        number = random.randint(1,170)
                                                        while number in deutsch_words:
                                                                number = random.randint(1,170)
                                                        deutsch_words.append(number)
                                                        two = cur.execute("SELECT translation FROM Fit_Bot WHERE nummer = ?", (number, ))
                                                        sender(id, two)

                                                        three = cur.execute("SELECT translation FROM Fit_Bot WHERE nummer = ?", (right_number, ))
                                                        sender(id, three)

                                                        number = random.randint(1,170)
                                                        while number in deutsch_words:
                                                                number = random.randint(1,170)
                                                        deutsch_words.append(number)
                                                        four = cur.execute("SELECT translation FROM Fit_Bot WHERE nummer = ?", (number, ))
                                                        sender(id, four)


                                                        for event in longpol.listen():
                                                                        if event.type == VkEventType.MESSAGE_NEW:
                                                                                        if event.to_me:
                                                                                                request = event.text
                                                                                                id = event.user_id

                                                                                                if request == '3':
                                                                                                        reaction = random.randint(1, 10)
                                                                                                        if reaction == 1:
                                                                                                                sender(id, 'Молодец!')
                                                                                                        if reaction == 2:
                                                                                                                sender(id, 'Здорового! 👍🏻')
                                                                                                        if reaction == 3:
                                                                                                                sender(id, 'Класс))')
                                                                                                        if reaction == 4:
                                                                                                                sender(id, 'Toll!')
                                                                                                        if reaction == 5:
                                                                                                                sender(id, 'Super💪🏻')
                                                                                                        if reaction == 6:
                                                                                                                sender(id, 'Sehr gut!')
                                                                                                        if reaction == 7:
                                                                                                                sender(id, 'У тебя хорошо получается!😎')
                                                                                                        if reaction == 8:
                                                                                                                sender(id, 'Richtig)')
                                                                                                        if reaction == 9:
                                                                                                                sender(id, 'Продолжай в том же духе 😀')
                                                                                                        if reaction == 10:
                                                                                                                sender(id, 'Правильно!')
                                                                                                        exercise()
                                                                                                elif request == 'Меню':
                                                                                                       
                                                                                                        menu()
                                                                                                        
                                                                                                                
                                                                                                else:
                                                                                                        sender(id, 'К сожалению это не правильный ответ. Правильный ответ: ')
                                                                                                        right_answer = cur.execute("SELECT translation FROM Fit_Bot WHERE nummer = ?", (right_number, ))
                                                                                                        sender(id, right_answer)
                                                                                                        time.sleep(4)
                                                                                                        exercise()
                                                                                                break
                                                   

                                                def right_fourth():
                                                        global id
                                                        sender(id, 'Слово на немецком 🇩🇪:')
                                                        number = random.randint(1,170)
                                                        deutsch_words.append(number)
                                                        right_number = number 
                                                        right_word = cur.execute("SELECT word FROM Fit_Bot WHERE nummer = ?", (number, ))
                                                        sender(id, right_word)

                                                        sender(id, 'Выбери правильный перевод 🇷🇺:')


                                                        number = random.randint(1,170)
                                                        while number in deutsch_words:
                                                                number = random.randint(1,170)
                                                        deutsch_words.append(number)
                                                        one = cur.execute("SELECT translation FROM Fit_Bot WHERE nummer = ?", (number, ))
                                                        sender(id, one)

                                                        number = random.randint(1,170)
                                                        while number in deutsch_words:
                                                                number = random.randint(1,170)
                                                        deutsch_words.append(number)
                                                        two = cur.execute("SELECT translation FROM Fit_Bot WHERE nummer = ?", (number, ))
                                                        sender(id, two)

                                                        number = random.randint(1,170)
                                                        while number in deutsch_words:
                                                                number = random.randint(1,170)
                                                        deutsch_words.append(number)
                                                        three = cur.execute("SELECT translation FROM Fit_Bot WHERE nummer = ?", (number, ))
                                                        sender(id, three)

                                                                        
                                                        four = cur.execute("SELECT translation FROM Fit_Bot WHERE nummer = ?", (right_number, ))
                                                        sender(id, four)




                                                        for event in longpol.listen():
                                                                        if event.type == VkEventType.MESSAGE_NEW:
                                                                                        if event.to_me:
                                                                                                request = event.text
                                                                                                id = event.user_id

                                                                                                if request == '4':
                                                                                                        reaction = random.randint(1, 10)
                                                                                                        if reaction == 1:
                                                                                                                sender(id, 'Молодец!')
                                                                                                        if reaction == 2:
                                                                                                                sender(id, 'Здорового! 👍🏻')
                                                                                                        if reaction == 3:
                                                                                                                sender(id, 'Класс))')
                                                                                                        if reaction == 4:
                                                                                                                sender(id, 'Toll!')
                                                                                                        if reaction == 5:
                                                                                                                sender(id, 'Super💪🏻')
                                                                                                        if reaction == 6:
                                                                                                                sender(id, 'Sehr gut!')
                                                                                                        if reaction == 7:
                                                                                                                sender(id, 'У тебя хорошо получается!😎')
                                                                                                        if reaction == 8:
                                                                                                                sender(id, 'Richtig)')
                                                                                                        if reaction == 9:
                                                                                                                sender(id, 'Продолжай в том же духе 😀')
                                                                                                        if reaction == 10:
                                                                                                                sender(id, 'Правильно!')
                                                                                                        exercise()
                                                                                                elif request == 'Меню':
                                                                                                        
                                                                                                        menu()
                                                                                                              
                                                                                                else:
                                                                                                        sender(id, 'К сожалению это не правильный ответ. Правильный ответ: ')
                                                                                                        right_answer = cur.execute("SELECT translation FROM Fit_Bot WHERE nummer = ?", (right_number, ))
                                                                                                        sender(id, right_answer)
                                                                                                        time.sleep(4)
                                                                                                        exercise()
                                                                                                break
                                                        


                                                function = random.randint(1,4)

                                                if function == 1:
                                                        right_first()
                                                elif function == 2:
                                                        right_second()
                                                elif function == 3:
                                                        right_third()
                                                elif function == 4:
                                                        right_fourth()





                                        exercise()

                                                                
                                                                
                                                                


                                else:
                                        to_menu(id, 'Для того, чтобы начать со мной говорить напишите или нажмите на кнопку со словом: "Меню"')
                             


                                

while True:
        main()
