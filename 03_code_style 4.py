# -*- coding: utf-8 -*-

# блоки кода

x, y = 10, 29

if x < 0:
    print('x меньше нуля')
    z = x ** 2 + y
else:
    print('x больше нуля')
    z = x - y
    print('Результат', z)

# ср. с С++

# if (x < 0) { printf('Меньше нуля\n'); z = x**2 + y; } else { printf('Больше нуля\n');
# z = x - y; } printf('Получается\n', z)

# вложенные блоки кода

name = input('Enter your name >>>')
if name == 'Ola':
    opponent = 'Ola'
    print('Hi, Ola!')
else:
    if name == 'Sofi':
        opponent = 'Sofi'
        print('Hi, Sofi!')
    else:
        if name == 'Katy':
            opponent = 'Katy'
            print('Hi, Katy!')
        else:
            opponent = 'anonymous'
            print('Hi, anonymous!')

# оператор pass

if x < 0:
    if y > 0:
        z = -x + y
    else:
        z = -x - y
else:
    z = x + y

# соглашения о стиле кода
# PEP8 (Python Enhancement Proposal 8) - описан "правильный" стиль программирования в пайтон
# https://www.python.org/dev/peps/pep-0008/

# 4 пробела на каждый уровень отступа

if x < 0:
    if y > 0:
        pass
    else:
        print('направо!')
else:
    print('стой!')

# Максимальная длина строки

my_poem = ['Варкалось, хливкие шорьки пырялись по наве',
           'И хрюкотали зелюки как мюмзики в мове',
           'О бойся Бармаглота, сын! Он так свирлеп и дик',
           'А в глуше рымит исполин - Злопастный Брандашмыг!', ]

# пробелы в операторах

x = 2
y = x * x + 1
is_big = x >= 3000

x = my_poem
print(x[0])
print(x[1])
print(x[2])
print(x[3])
my_list = [2, 3, 4, 5, 6, ]

# reformat кода

p, t = 3, 8

if p == 3:
    print(42)

if p < 0:
    if t > 0:
        print('налево!')
    else:
        print('направо!')
else:
    print('стой!')

# названия переменных

number_pets = 34
if number_pets < 10:
    print('I need more space for my pets!')

my_pets = ['cat', 'dog', 'ostrich']
if 'lion' in my_pet:
    print('Wow!')

my_pets = ['cat', 'dog', 'ostrich']
# но такой стиль используется для названий классов


# рекомендации PEP8

# b (одиночная маленькая буква)
# B (одиночная заглавная буква)
# но лучше использовать только такие однобуквенные имена
#   i j k - для циклов
#   x y z - для координат

# никогда не используйте в названиях переменных одиночные l, I, O  !
a = 34
b = 43
if a > b:
    print('Правильно')
r = 9
if r > 0:
    print('Правильно')

# lowercase (слово в нижнем регистре)
# lower_case_with_underscores (слова из маленьких букв с подчеркиваниями)
# UPPERCASE (заглавные буквы)
# UPPERCASE_WITH_UNDERSCORES (слова из заглавных букв с подчеркиваниями)

# CapitalizedWords (слова с заглавными буквами, или CapWords, или CamelCase).
#   Замечание: когда вы используете аббревиатуры в таком стиле, пишите все буквы аббревиатуры заглавными —
#   HTTPServerError лучше, чем HttpServerError.

# mixedCase (отличается от CapitalizedWords тем, что первое слово начинается с маленькой буквы)
# Capitalized_Words_With_Underscores (слова с заглавными буквами и подчеркиваниями — уродливо!)


# автоматическое переименование в PyCharm и подсказки - вам не нужно набирать длинные названия переменных

my_pets = ['cat', 'dog', 'ostrich']
if 'lion' in my_pets:
    print('Wow!')
# В каждой уважающей себя компании есть style guide (стайл-гайд) - руководство по стилю написания кода.
# Практически все они основываются на PEP8, с небольшими исключениями, принятыми в этой команде.
# Как пример стайл-гайда небольшой компании рекомендую почитать
# https://github.com/best-doctor/guides/blob/master/guides/python_styleguide.md
