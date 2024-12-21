try:
    # Некоторый код, генерирующий исключение
    raise Exception("Описание ошибки")
    
except Exception as e:
    print("Произошла ошибка:", str(e))
