s = input()

if len(s)>=10:
    print('+Пароль содержит 10 и более символов')
else:
    print('- Пароль должен содержать, как минимум 10 символов')
          
#if s.isupper() == False:
    #print('+ В пароле есть строчные буквы')
#else:
    #print('- В пароле нет строчных букв!')
    
#if s.islower() == False:
    #print('+ В пароле есть заглавные буквы')
#else:
    #print('- В пароле нет заглавных букв!')
    
if s.isalnum() == False:
    print('+ В пароле есть специальные символы')
else:
    print('- В пароле нет специальных символов!')
    
if s.isdigit() == False:
    print('+ В пароле есть буквы.')
    if s.isupper() == False:
        print('+ В пароле есть строчные буквы')
    else:
        print('- В пароле нет строчных букв!')
    if s.islower() == False:
        print('+ В пароле есть заглавные буквы')
    else:
        print('- В пароле нет заглавных букв!')
else:
    print('- В пароле нет букв!')
    
if s.isalpha() == False:
    print('+ В пароле есть цифры')
else:
    print('- В пароле нет цифр!')
