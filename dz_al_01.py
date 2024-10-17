#Преобразовываем строку в символ: удаляем все пробелы, знаки препинания и приводим все символы к одному регистру (например, к сохранению).
# Это необходимо, чтобы сравнивать строки без учета регистра и ненужных символов. Для этого применяем библиотеку re
#Получаем обратную версию строки.
#Сравниваем оригинальную форму и ее обратную версию
#Если они равны, строка будет палиндромом, выдаем True. Если нет — False.


import re

def is_palindrome(string):   
    cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', string).lower()
  
    reversed_string = cleaned_string[::-1]
   
    if cleaned_string == reversed_string:
        return True  
    else:
        return False  

print(is_palindrome("A man, a plan, a canal, Panama"))  # True
print(is_palindrome("Hello, World!"))  # False
