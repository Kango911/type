#Kango911
def calculate_letter_case_percentage(chars):
    total_chars = len(chars)
    if total_chars == 0:
        return 0.0, 0.0

    lowercase_count = sum(1 for char in chars if char.islower())
    uppercase_count = sum(1 for char in chars if char.isupper())

    lowercase_percentage = (lowercase_count / total_chars) * 100
    uppercase_percentage = (uppercase_count / total_chars) * 100

    return lowercase_percentage, uppercase_percentage


# Пример использования функции
text = "Hello World! This is a Test."
lowercase_percent, uppercase_percent = calculate_letter_case_percentage(text)
print(f"Процент строчных букв: {lowercase_percent:.2f}%")
print(f"Процент прописных букв: {uppercase_percent:.2f}%")
