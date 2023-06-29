def count_words():

    text = '''Соображения высшего порядка, а также начало повседневной работы по формированию позиции напрямую зависит от дальнейших направлений развитая системы массового участия. Значимость этих проблем настолько очевидна, что выбранный нами инновационный путь представляет собой интересный эксперимент проверки форм воздействия. Соображения высшего порядка, а также социально-экономическое развитие напрямую зависит от экономической целесообразности принимаемых решений. Задача организации, в особенности же сложившаяся структура организации играет важную роль в формировании новых предложений! Разнообразный и богатый опыт выбранный нами инновационный путь играет важную роль в формировании модели развития. Практический опыт показывает, что выбранный нами инновационный путь представляет собой интересный эксперимент проверки системы масштабного изменения ряда параметров? Таким образом, реализация намеченного плана развития требует от нас анализа модели развития. Значимость этих проблем настолько очевидна, что постоянный количественный рост и сфера нашей активности в значительной степени обуславливает создание экономической целесообразности принимаемых решений. Повседневная практика показывает, что дальнейшее развитие различных форм деятельности играет важную роль в формировании новых предложений? Таким образом, сложившаяся структура организации в значительной степени обуславливает создание ключевых компонентов планируемого обновления? Соображения высшего порядка, а также консультация с профессионалами из IT создаёт предпосылки качественно новых шагов для дальнейших направлений развитая системы массового участия. Таким образом, постоянный количественный рост и сфера нашей активности позволяет выполнить важнейшие задания по разработке...'''

    word_list = text.lower().split()

    list_unsigned_words = [''.join(filter(str.isalpha, a)) for a in word_list]

    while '' in list_unsigned_words:

        list_unsigned_words.remove('')

    ten_word_dictionary = {}

    for word in list_unsigned_words:

        ten_word_dictionary.setdefault(word, list_unsigned_words.count(word))

    num_words = 1

    print()

    while num_words <= 10:

        num_words += 1

        max_key = max(ten_word_dictionary, key=ten_word_dictionary.get)

        print(f"Встречаемые слова - | {max_key:>11} | Количество слов - |{ten_word_dictionary[max_key]}|")

        ten_word_dictionary.pop(max_key)

    print()

count_words()
