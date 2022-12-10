# завдання 1 // № 6
# Напишіть програму, яка зчитує від користувача магнітуду та виводить відповідний
# опис. Нижче наведена таблиця містить діапазони магнітуд землетрусів за шкалою
# Ріхтера та опис відповідного землетрусу:
# Магнітуда
# Опис
# <2.0
# Мікро (micro)
# 2.0-3.0
# Дуже слабкий (very minor)
# 3.0-4.0
# Слабкий (minor)
# 4.0-5.0
# Легкий (light)
# 5.0-6.0
# Помірний (moderate)
# 6.0-7.0
# Сильний (strong)
# 7.0-8.0
# Дуже сильний (major)
# 8.0-10.0
# Великий (great)
# >=10.0
# Рідкісно великий (meteoric)

magnitude = 0

def magnituDe():


    try:
        magnitude = int(input('введіть магнітуду : '))
        if magnitude < 0 :
            print('землетрусу нема')
        elif magnitude < 2:
            print('Мікро (micro)')
        elif magnitude < 3:
            print('Дуже слабкий (very minor)')
        elif magnitude < 4:
            print('Слабкий (minor)')
        elif magnitude < 5:
            print('Легкий (light)')
        elif magnitude < 6:
            print('Помірний (moderate)')
        elif magnitude < 7:
            print('Сильний (strong)')
        elif magnitude < 8:
            print('Дуже сильний (major)')
        elif magnitude < 10:
            print('Великий (great)')
        elif magnitude >= 10:
            print('Рідкісно великий (meteoric)')
    except:
        print('введіть число!!!!!!!!!')
        magnituDe()

magnituDe()