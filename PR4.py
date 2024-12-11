def print_char_codes(s):
    if len(s) > 0:
        first_char_code = ord(s[0])  
        last_char_code = ord(s[-1])   
        
        print(f'Код первого символа: {first_char_code}')
        print(f'Код последнего символа: {last_char_code}')
    else:
        print('Строка не должна быть пустой.')


input_string = input("Введите непустую строку: ")
print_char_codes(input_string)
