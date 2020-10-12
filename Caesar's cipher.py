if __name__ == '__main__':
    A = "abcdefghijklmnopqrstuvwxyz"
    B = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    text = ''
    new_text = ''
    exit = False
    while exit != True:
        print("Выберите действие:")
        print("1) Зашифровать текст")
        print("2) Расшифровать текст")
        print("3) Выход")
        value = int(input())
        if value == 1:
            new_text = ''
            text = str(input("Введите текст который надо зашифровать: "))
            text = text.lower()
            for i in range(len(text)):
                number = A.find(text[i])
                if A.find(text[i]) != -1:
                    if A.find(text[i]) <= 22:
                        number = A[A.find(text[i]) + 3]
                        new_text = new_text + A[A.find(text[i]) + 3]
                    elif A.find(text[i]) == 23:
                        new_text = new_text + 'a'
                    elif A.find(text[i]) == 24:
                        new_text = new_text + 'b'
                    elif A.find(text[i]) == 25:
                        new_text = new_text + 'c'
                elif B.find(text[i]) != -1:
                    number = B.find(text[i])
                    if A.find(text[i]) <= 29:
                        number = B[B.find(text[i]) + 3]
                        new_text = new_text + B[B.find(text[i]) + 3]
                    elif A.find(text[i]) == 30:
                        new_text = new_text + 'а'
                    elif A.find(text[i]) == 31:
                        new_text = new_text + 'б'
                    elif A.find(text[i]) == 32:
                        new_text = new_text + 'в'
                else:
                    new_text = new_text + text[i]
            print()
            print("Исходный текст: ", text)
            print("Зашифрованный текст: ", new_text)
            print()
        elif value == 2:
            new_text = ''
            text = str(input("Введите текст который надо расшифровать: "))
            text = text.lower()
            for i in range(len(text)):
                if A.find(text[i]) != -1:
                    if A.find(text[i]) >= 3:
                        new_text = new_text + A[A.find(text[i]) - 3]
                    elif A.find(text[i]) == 0:
                        new_text = new_text + 'x'
                    elif A.find(text[i]) == 1:
                        new_text = new_text + 'y'
                    elif A.find(text[i]) == 2:
                        new_text = new_text + 'z'
                elif B.find(text[i]) != -1:
                    if B.find(text[i]) >= 3:
                        new_text = new_text + B[B.find(text[i]) - 3]
                    elif B.find(text[i]) == 0:
                        new_text = new_text + 'э'
                    elif B.find(text[i]) == 1:
                        new_text = new_text + 'ю'
                    elif B.find(text[i]) == 2:
                        new_text = new_text + 'я'
                else:
                    new_text = new_text + text[i]
            print()
            print("Исходный текст: ", text)
            print("Расшифрованный текст: ", new_text)
            print()
        elif value == 3:
            exit = True
            print("Выход...")