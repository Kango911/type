def count_abc_occurrences(chars):
    count = 0
    n = len(chars)

    # Проходим по массиву символов до предпоследнего символа
    for i in range(n - 2):
        # Проверяем текущий символ и следующие два
        if chars[i] == 'a' and chars[i + 1] == 'b' and chars[i + 2] == 'c':
            count += 1

    return count


# Пример использования функции
characters = ['a', 'b', 'c', 'a', 'b', 'c', 'x', 'y', 'z', 'a', 'b', 'c']
result = count_abc_occurrences(characters)
print(f"Количество вхождений 'abc' в массив символов: {result}")
