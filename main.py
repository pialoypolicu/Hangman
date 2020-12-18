import random

question = ['Какое колесо не крутится при правом развороте?', 'Каких камней в море нет?',

            '''Когда национальным гвардейцам США, служащим в Техасе, начали выдавать новую маскировочную форму,
некоторые из них пригрозили подать в отставку, если этот маскарад не прекратится. Внимание, вопрос! Что послужило 
образцом для этих костюмов?''',

            '''Существует анекдот про московских рэкетиров, которые пошли на дело, но по пути наткнулись на небольшое 
символическое "препятствие". На вопрос рэкетиров: "На кого работаешь" встреченное животное дало вполне логичный ответ. 
Какой?''']

# word_list = ['Ласка', 'Хаос', 'Возбуждение', 'Бегемот', 'Проводница', 'Бикини', 'Хейтер', 'Любовник', 'Фантазер',
#           'Сердцеед', 'Афродизиак', 'Пехотинец', 'Душа', 'Стриптиз', 'Зашквар', 'Шантаж', 'Невинность', 'Ленивец',
#          'Женственность']

word_list = ['Запасное', 'Сухих', 'Кактус', 'Мур']


def ending(tr):
    if tr in [7, 6, 5]:
        return 'ок'
    elif tr in [4, 3, 2]:
        return 'ки'
    elif tr == 1:
        return 'ка'


def display_hangman(num):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
                   -------X
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
        # голова, торс, обе руки, одна нога
        '''
                   -------X
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
        # голова, торс, обе руки
        '''
                   -------X
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
        # голова, торс и одна рука
        '''
                   -------X
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
        # голова и торс
        '''
                   -------X
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
        # голова
        '''
                   -------X
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
        # начальное состояние
        '''
                   -------X
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                ''',
        '''
                   -------X
                   |      
                   |      
                   |    
                   |      
                   |     
                   -
                ''',
        '''
                   -------
                   |      
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[num]


def play(qst, lvl):
    word = word_list[qst].upper()  # Загаданное слово
    word_lose = word
    if lvl == 'легкий':     # уровень сложности, кол-во попыток
        tries = 8  # количество попыток
    elif lvl == 'средний':
        tries = 7
    elif lvl == 'сложный':
        tries = 6
    elif lvl == 'я кратос':
        tries = 5
        print(f'''Считаешь себя круче Кратоса, давай посмотрим, насколько крепки твои яйца! Тебе даю {tries} попыток!'
Вопроса загадки не жди, проверь свою интуацию!''')
    # print(word)
    if lvl in ['легкий', 'средний', 'сложный']:
        print(f'''Отгадайте загадку. У вас есть {tries} попыток
{question[qst]}''')
    print(display_hangman(tries))
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    if lvl == 'легкий':
        word_completion = word[0] + word_completion[1:len(word)-1] + word[-1]
        word = '*' + word[1:len(word)-1] + '*'
    print(word_completion)

    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    guessed = False  # сигнальная метка

    while not guessed:
        print('\nНазваные буквы >>>', guessed_letters)
        flag = True
        while flag:  # Проверяем что ввели.
            answer = input('Введите букву или слово русского алфавита: ').upper()
            if len(answer) == 1:
                if ord(answer) < 1040 or ord(answer) > 1103:
                    print('Требуется ввести букву русского алфавита или слово совпадающим количеством букв ответа.')
                    continue
                elif len(answer) == 1 and 1040 <= ord(answer) <= 1103:
                    if answer in guessed_letters:
                        print('Вы называли эту букву. Попробуйте еще раз.')
                    else:
                        flag = False
            elif len(answer) == len(word):
                if answer in guessed_words:
                    print('Вы называли это слово. Попробуйте еще раз')
                elif answer == word_lose:
                    if word_lose == 'МУР':
                        print(word_lose, '- Московский уголовный розыск\nПоздравляем, вы угадали слово! Вы победили!')
                        flag = False
                    else:
                        print('\nПоздравляем, вы угадали слово! Вы победили!')
                        flag = False
                else:
                    for c in answer:
                        if ord(c) < 1040 or ord(c) > 1103:
                            print('Требуется ввести букву русского алфавита или слово совпадающим количеством букв '
                                  'ответа.')
                            break
                    else:
                        flag = False
            elif len(answer) > 1 and len(answer) != len(word):
                print('Требуется ввести букву русского алфавита или слово совпадающим количеством букв ответа.')

        if len(answer) == 1:
            guessed_letters.append(answer)
            if answer in word:
                print('Вы угадали, такая буква есть')
                count_num = word.count(answer)
                for i in range(count_num):
                    id_word = word.find(answer)
                    word_completion = word_completion[:id_word] + answer + word_completion[id_word + 1:]
                    word = word.replace(word[id_word], '*', 1)
                print(word_completion, end='')
                if '_' not in word_completion:
                    if word_completion == 'МУР':
                        print(' - Московский уголовный розыск\nПоздравляем, вы угадали слово! Вы победили!')
                        guessed = True
                    else:
                        print('\nПоздравляем, вы угадали слово! Вы победили!')
                        guessed = True
            else:
                tries -= 1
                print(display_hangman(tries))
                if tries > 0:
                    print(f'Такой буквы нет. У вас осталось {tries} попыт{ending(tries)}. Попробуйте еще.')
                    print(word_completion)
                else:
                    print('Вы проиграли!\nЗагаданное слово:', word_lose)
                    break

        elif len(answer) == len(word):
            if answer == word_lose:
                guessed = True
            else:
                tries -= 1
                print(display_hangman(tries))
                if tries > 0:
                    guessed_words.append(answer)
                    print(f'Вы не угадали слово. У вас осталось {tries} попыт{ending(tries)}. Попробуйте еще.')
                    print(word_completion)
                else:
                    print('Вы проиграли!\nЗагаданное слово:', word_lose)
                    break


def get_word():
    repeat = True
    while repeat:
        level = input('''>>> Выберете уровень сложности.
>>> Легкий - Задан вопрос к загадке. Отображается 1-ая и последняя буква. Дается 8 попыток.
>>> Средний - Задан вопрос к загадке. Дается 7 попыток.
>>> Сложный - Задан вопрос к загадке. Дается 6 попыток.
>>> Я Кратос - Вопрос скрыт. Дается 5 попыток.
>>> ''').lower()
        while level not in ['легкий', 'средний', 'сложный', 'я кратос']:
            level = input('''>>> Выберете уровень сложности.
>>> Легкий - Задан вопрос к загадке. Отображается 1-ая и последняя буква. Дается 8 попыток.
>>> Средний - Задан вопрос к загадке. Дается 7 попыток.
>>> Сложный - Задан вопрос к загадке. Дается 6 попыток.
>>> Я Кратос - Вопрос скрыт. Дается 5 попыток.
>>> ''').lower()
        play(*(random.randrange(len(question)), level))
        rpt = input('''Желаете сыграть еще? 
        >>> Играть ещË раз - да
        >>> Пока - нет
        >>> ''').lower()
        while rpt not in ['да', 'нет']:
            rpt = input('''Желаете сыграть еще?
            >>> Играть ещË раз - да            
            >>> Пока - нет                     
            >>> ''').lower()
        if rpt in 'да':
            continue
        else:
            repeat = False


get_word()
