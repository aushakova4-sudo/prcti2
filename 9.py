print('Собака короткошерстной породы?')
answer1 = input().lower()
if answer1 == 'да':
    print ('рост собаки менее 50 см?')
    answer2 = input().lower()
    if answer2 == 'да':
        print ('У собаки короткий хвост? ')
        answer3 = input().lower()
        if answer3 == 'да':
            print ('английский бульдог')
        else:
            print('У собаки длинные уши?')
            answer4 = input().lower()
            if answer4 == 'да':
                print('гончая')
            else:
                print('У собаки короткое тело?')
                answer5 = input().lower()
                if answer5 == 'да':
                    print('мопс')
                else:
                    print('чихуахуа')
    else:
        print('собака весит более 50 кг?')
        answer6 = input().lower()
        if answer6 =='да':
            print ('датский дог')
        else:
            print('фоксхаунд')
else:
    print('Рост собаки менее 50 см?')
    answer7 = input().lower()
    if answer7 == 'да':
        print('у собаки доброжелательный характер?')
        answer8 = input().lower()
        if answer8 == 'да':
            print('кокер-спаниэль')
        else:
            print('ирландский сеттер')

    else:
        print('у собаки рост менее 70 см?')
        answer9 = input().lower()
        if answer9 == 'да':
            print('у собаки длинные уши?')
            answer10 = input().lower()
            if answer10 == 'да':
                print('большой вандейский грифон')
            else:
                print('колли')
        else:
            print('окрас рыжий с белыми отметинами?')
            answer11 = input().lower()
            if answer11 == 'да':
                print('сенбернар')
            else:
                print('белоснежный окрас?')
                answer12 = input().lower()
                if answer12 == 'да':
                    print('ирландский волкодав')
                else:
                    print('ньюфаундленд')
