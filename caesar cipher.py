def ceasar_string(lang, string, number):

    if lang == 'rus':
        abc_lower = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя'
        abc_upper = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        s_rus = ''
        for i in string:
            if i.isalpha() == True and i == i.lower():
                s_rus = s_rus + (abc_lower[abc_lower.index(i) + number])
            elif i.isalpha() == True and i == i.upper():
                s_rus = s_rus + (abc_upper[abc_upper.index(i) + number])
            elif i.isalpha() == False:
                s_rus = s_rus + i
        return s_rus

    if lang == 'eng':
        abc_lower = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
        abc_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
        s_eng = ''
        for i in string:
            if i.isalpha() == True and i == i.lower():
                s_eng = s_eng + (abc_lower[abc_lower.index(i) + number])
            elif i.isalpha() == True and i == i.upper():
                s_eng = s_eng + (abc_upper[abc_upper.index(i) + number])
            elif i.isalpha() == False:
                s_eng = s_eng + i
        return s_eng


lang = input('Chose language (eng/rus): ')

string = input('Send your string: ')

number = int(input('How many change symbols you need: '))

print(ceasar_string(lang, string, number))