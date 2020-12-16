import random

word_list = ['Ласка', 'Хаос', 'Возбуждение', 'Бегемот', 'Проводница', 'Бикини', 'Хейтер', 'Любовник', 'Фантазер',
             'Сердцеед', 'Афродизиак', 'Пехотинец', 'Душа', 'Стриптиз', 'Зашквар', 'Шантаж', 'Невинность', 'Ленивец',
             'Женственность']


def ending(tries):
    if tries == 5:
        return 'ок'
    elif tries in [4, 3, 2]:
        return 'ки'
    elif tries == 1:
        return 'ка'


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
        # голова, торс, обе руки, одна нога
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
        # голова, торс, обе руки
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
        # голова, торс и одна рука
        '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
        # голова и торс
        '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
        # голова
        '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
        # начальное состояние
        '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


def play(word):
    word = word.upper()
    word_lose = word
    tries = 6  # количество попыток
    # print(word)
    print(f'Давайте играть в угадайку слов! У вас есть {tries} попыток')
    print(display_hangman(tries))
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    print(word_completion)

    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    guessed = False  # сигнальная метка

    while not guessed:
        print('Названые буквы >>> ', guessed_letters)
        answer = input('Введите букву или слово: ').upper()
        if not answer.isalpha() or len(answer) > 1 and len(answer) != len(word):
            print('Введите одну букву или слово целиком.')
        elif answer in guessed_letters:
            print('Вы называли эту букву. Попробуйте еще раз.')
        elif answer in guessed_words:
            print('Вы называли это слово. Попробуйте еще раз')
        elif len(answer) == len(word):
            if answer == word_lose:
                print('Поздравляем, вы угадали слово! Вы победили!')
                guessed = True

            else:
                tries -= 1
                print(display_hangman(tries))
                if tries > 0:
                    guessed_words.append(answer)
                    print(f'Вы не угадали слово. У вас осталось {tries} попыт{ending(tries)}. Попробуйте еще.')
                    print(word_completion)
                else:
                    print('You lose!', word_lose, sep='\n')
                    break
        else:
            guessed_letters.append(answer)
            if answer in word:
                print('Вы угадали, такая буква есть')
                count_num = word.count(answer)
                for i in range(count_num):
                    id_word = word.find(answer)
                    word_completion = word_completion[:id_word] + answer + word_completion[id_word + 1:]

                    word = word.replace(word[id_word], '*', 1)
                print(word_completion)
                if '_' not in word_completion:
                    print('Поздравляем, вы угадали слово! Вы победили!')
                    guessed = True
            else:
                tries -= 1
                print(display_hangman(tries))
                if tries > 0:
                    print(f'Такой буквы нет. У вас осталось {tries} попыт{ending(tries)}. Попробуйте еще.')
                    print(word_completion)
                else:
                    print('You lose', word_lose, sep='\n')
                    break


def get_word():
    repeat = True
    while repeat:
        play(*(random.sample(word_list, 1)))
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


