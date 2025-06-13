def get_num_words(s_words) :
    word_list = s_words.split()
    return len(word_list)

def sort_on(dict):
    return dict["num"]

def sort_dict(my_dict):
    t_list = []
    for x, y in my_dict.items() :
        temp = { "char":x, "num": y}
        t_list.append(temp)
    t_list.sort(reverse=True, key=sort_on)
    return t_list

def get_count_chars(s_words) :
    s_words = s_words.lower()
    c_count = {}
    for c in s_words :
        if c in c_count and c.isalpha():
            c_count[c] += 1
        elif c.isalpha() :
            c_count[c] = 1
    return c_count
