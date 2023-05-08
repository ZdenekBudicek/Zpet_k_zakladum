user_name = input("Zadejte své uživatelské jméno: ")
password = input("Zadejte své heslo: ")

print(f"{user_name}, vaše heslo je {'*' * len(password)} a délka vašeho hesla je {len(password)}")
