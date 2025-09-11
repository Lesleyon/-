"""
Создать txt-файл, вставить туда любую англоязычную статью из Википедии.
Реализовать одну функцию, которая выполняет следующие операции:
- прочитать файл построчно;
- непустые строки добавить в список;
- удалить из каждой строки все цифры, знаки препинания, скобки, кавычки и т.д. (остаются латинские буквы и пробелы);
- объединить все строки из списка в одну, используя метод join и пробел, как разделитель;
- создать словарь вида {“слово”: количество, “слово”: количество, … } для подсчета количества разных слов,
  где ключом будет уникальное слово, а значением - количество;
- вывести в порядке убывания 10 наиболее популярных слов, используя форматирование
  (вывод примерно следующего вида: “ 1 place --- sun --- 15 times \n....”);
- заменить все эти слова в строке на слово “PYTHON”;
- создать новый txt-файл;
- записать строку в файл, разбивая на строки, при этом на каждой строке записывать не более 100 символов
  при этом не делить слова.
"""

def wiki_function():
    with open("wiki.txt", "r") as txt:
        strings = txt.readlines()
    txt.close()

    for num in range(len(strings)):
        string = strings[num]
        string_new = ""
        for i in range(0, len(string)):
            if string[i].isalpha():
                string_new += string[i]
            elif string[i].isspace():
                string_new += string[i]
        strings[num] = string_new

    string_new = " ".join(strings)
    string_new = string_new.replace("\n", "")
    string_new = string_new.replace("\t", "")

    dictionary = dict()
    temp = ""
    list_string_new = []
    for i in range(len(string_new)):
        if string_new[i] == ' ':
            if temp != "":
                list_string_new.append(temp)
                temp = ""
        if string_new[i] != ' ':
            temp += string_new[i]
    if temp != "":
        list_string_new.append(temp)
    for word in list_string_new:
        word = word.lower()
        if not dictionary.get(word):
            dictionary[word] = 1
        else:
            num = dictionary.get(word)
            dictionary[word] = num + 1

    dictionary_words = []
    dictionary_nums = []
    for key, count in dictionary.items():
        dictionary_nums.append(count)
        dictionary_words.append(key)
    for i in range(len(dictionary_nums)):
        max_value_index = i
        for j in range(i + 1, len(dictionary_nums)):
            if dictionary_nums[max_value_index] < dictionary_nums[j]:
                max_value_index = j
        dictionary_nums[i], dictionary_nums[max_value_index] =\
            dictionary_nums[max_value_index], dictionary_nums[i]
        dictionary_words[i], dictionary_words[max_value_index] =\
            dictionary_words[max_value_index], dictionary_words[i]
    most_popular = []
    for i in range(0, 10):
        print("{0} place --- {1} --- {2} times".format(i, dictionary_words[i], str(dictionary_nums[i])))
        most_popular.append(dictionary_words[i])

    for i in range(len(list_string_new)):
        for popular in most_popular:
            if list_string_new[i].lower() == popular:
                list_string_new[i] = "PYTHON"

    file = open("new_file.txt", "a+")
    count = 0
    for i in range(len(list_string_new)):
        count += len(list_string_new[i])
        if count >= 98:
            file.write("\n")
            file.write(list_string_new[i])
            count = len(list_string_new[i])
        else:
            file.write(" ")
            file.write(list_string_new[i])
    file.close()

# Вызов функции
wiki_function()
