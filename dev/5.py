a = int(input("Введите номинал банкноты: "))

match a:
    case(1):
        print("Джордж Вашингтон")
    case(2):
        print("Томас Джефферсон")
    case(4):
        print("Авраам Линкольн")
    case(10):
        print("Александр Гамильтон")
    case(20):
        print("Эндрю Джексон")
    case(50):
        print("Улисс Грант")
    case(100):
        print("Бенджамин Франклин")
    case _:
        print("янезнаю")
