def get_num_words(text):
    word_list = text.split()
    num_words = len(word_list)
    return num_words


def get_char_count(text):
    dic = {}
    new_text = text.lower()
    for char in new_text:
        if char not in dic:
            dic[char] = 1
        else:
            dic[char] += 1
    return dic


def sort_on(dic):
    return dic["num"]


def sort_dic(dic):
    lod = []
    for k in dic:
        lod.append({"char": k, "num": dic[k]})

    lod.sort(reverse=True, key=sort_on)
    return lod
