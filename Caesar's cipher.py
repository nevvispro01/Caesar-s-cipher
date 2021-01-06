import logging

if __name__ == '__main__':
    A = "abcdefghijklmnopqrstuvwxyz"
    B = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    logging.basicConfig(filename="sample.log", level=logging.INFO)
    logging.info("Начало работы")
    text = ''
    new_text = ''
    exit = False
    while exit != True:
        print("Выберите действие:")
        print("1) Зашифровать текст")
        print("2) Расшифровать текст")
        print("3) Выход")
        logging.info("Выберите действие: 1) Зашифровать текст 2) Расшифровать текст 3) Выход")
        value = int(input())
        if value == 1: # Зашифровать тест
            logging.info("Зашифровка текста")
            new_text = ''
            text = str(input("Введите текст который надо зашифровать: "))
            logging.info("Введите текст который надо зашифровать: ")
            p = "Введенный тест: " + text
            logging.info(p)
            text = text.lower() # преобразование всех букв в строчные
            logging.info("Преобразование всех букв в строчные...")
            logging.info("Изменение букв и добавление их к строке с зашифрованном текстом...")
            for i in range(len(text)):
                if A.find(text[i]) != -1: # проверка на английские буквы
                    number = A.find(text[i]) # нахождение цифры, под которой находится данная введенная буква в алфавите в начале программы
                    if number <= 22:
                        new_text = new_text + A[A.find(text[i]) + 3] # Добавление измененной буквы к строке с зашифрованном тексте
                    elif number == 23:
                        new_text = new_text + 'a' # Добавление буквы 'a' к строке с зашифрованном тексте
                    elif number == 24:
                        new_text = new_text + 'b' # Добавление буквы 'b' к строке с зашифрованном тексте
                    elif number == 25:
                        new_text = new_text + 'c' # Добавление буквы 'c' к строке с зашифрованном тексте
                elif B.find(text[i]) != -1: # проверка на русские буквы
                    number = B.find(text[i]) # нахождение цифры, под которой находится данная введенная буква в алфавите в начале программы
                    if number <= 29:
                        new_text = new_text + B[B.find(text[i]) + 3] # Добавление измененной буквы к строке с зашифрованном тексте
                    elif number == 30:
                        new_text = new_text + 'а' # Добавление буквы 'a' к строке с зашифрованном тексте
                    elif number == 31:
                        new_text = new_text + 'б' # Добавление буквы 'б' к строке с зашифрованном тексте
                    elif number == 32:
                        new_text = new_text + 'в' # Добавление буквы 'в' к строке с зашифрованном тексте
                else:
                    new_text = new_text + text[i] # если введен символ, то с ним преобразование не проводятся
            print()
            print("Исходный текст: ", text)
            print("Зашифрованный текст: ", new_text)
            print()
            text = str("Исходный текст: " + text)
            new_text = str("Зашифрованный текст: " + new_text)
            logging.info(text)
            logging.info(new_text)
        elif value == 2: # Расшифровать тест
            logging.info("Расшифровка текста")
            new_text = ''
            text = str(input("Введите текст который надо расшифровать: "))
            logging.info("Введите текст который надо зашифровать: ")
            p = "Введенный тест: " + text
            logging.info(p)
            text = text.lower() # преобразование всех букв в строчные
            logging.info("Преобразование всех букв в строчные...")
            logging.info("Изменение букв и добавление их к строке с зашифрованном текстом...")
            for i in range(len(text)):
                if A.find(text[i]) != -1: # проверка на английские буквы
                    number = A.find(text[i])  # нахождение цифры, под которой находится данная введенная буква в алфавите в начале программы
                    if number >= 3:
                        new_text = new_text + A[A.find(text[i]) - 3] # Добавление измененной буквы к строке с зашифрованном тексте
                    elif number == 0:
                        new_text = new_text + 'x' # Добавление буквы 'x' к строке с зашифрованном тексте
                    elif number == 1:
                        new_text = new_text + 'y' # Добавление буквы 'y' к строке с зашифрованном тексте
                    elif number == 2:
                        new_text = new_text + 'z' # Добавление буквы 'z' к строке с зашифрованном тексте
                elif B.find(text[i]) != -1:
                    number = B.find(text[i])  # нахождение цифры, под которой находится данная введенная буква в алфавите в начале программы
                    if number >= 3:
                        new_text = new_text + B[B.find(text[i]) - 3] # Добавление измененной буквы к строке с зашифрованном тексте
                    elif number == 0:
                        new_text = new_text + 'э' # Добавление буквы 'э' к строке с зашифрованном тексте
                    elif number == 1:
                        new_text = new_text + 'ю' # Добавление буквы 'ю' к строке с зашифрованном тексте
                    elif number == 2:
                        new_text = new_text + 'я' # Добавление буквы 'я' к строке с зашифрованном тексте
                else:
                    new_text = new_text + text[i] # если введен символ, то с ним преобразование не проводятся
            print()
            print("Исходный текст: ", text)
            print("Расшифрованный текст: ", new_text)
            print()
            text = str("Исходный текст: " + text)
            new_text = str("Расшифрованный текст: " + new_text)
            logging.info(text)
            logging.info(new_text)
        elif value == 3:
            exit = True
            print("Выход...")
            logging.info("Выход...")
            logging.info("Process finished with exit code 0")
        else:
            print("Неверный формат ввода, попробуйте еще раз.")
            logging.error("Неверный формат ввода")