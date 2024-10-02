while True:
    password = input("Введите пароль: ")
    if len(password) >= 8:
        print("Пароль принят.")
        break
    else:
        print("Пароль слишком короткий. Длина пароля должна быть не менее 8 символов. Попробуйте снова.")