# Функция для проверки слова на условия задачи
def is_symmetric_word(word):
    vowels = "аеёиоуыэюя"
    consonants = "бвгджзйклмнпрстфхцчшщ"

    # Проверяем чередование гласных и согласных
    alternating = (word[0] in vowels)
    for i in range(1, len(word)):
        if (i % 2 == 0 and word[i] not in vowels) or (i % 2 != 0 and word[i] not in consonants):
            alternating = False
            break

    # Проверяем симметричность относительно центра
    symmetric = (word == word[::-1])

    return alternating and symmetric


# Основная функция для фильтрации слов в строке
def filter_symmetric_words(line):
    result = []

    # Разделяем строку на слова по пробелам
    words = line.split()

    # Проверяем каждое слово
    for word in words:
        if is_symmetric_word(word):
            result.append(word)

    # Соединяем подходящие слова в новую строку
    return ' '.join(result)


# Пример использования функции
text = "аргентина манит. казак лес. баян ода. кот где? топот. репер. око поко. радар."
filtered_text = filter_symmetric_words(text)
print("Отфильтрованные слова:")
print(filtered_text)
