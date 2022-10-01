import math


def separator(string, limit):
    """
    :param string: the total paragraph or string.
    :param limit: maximum allowed characters in a single line.
    :return: a list of strings. to be more specific a list of lines which will be displayed in the UI.
    """
    
    result = string
    if len(string) < limit:
        result = string
    else:
        print(f'Main String Length = {len(string)}')
        words = string.split()
        new_str = ''
        result_list = []
        flag = False
        i = 0
        while i < len(words):
            new_str_len = len(new_str)
            if len(words[i]) + new_str_len < limit:
                new_str += words[i]
                new_str += ' '
                flag = False
                i += 1
                if i == len(words):
                    result_list.append(new_str.strip())
            else:
                if len(words[i]) >= limit:
                    current_word = words[i]
                    length_diff = limit - new_str_len
                    temp_word = current_word[:length_diff]
                    new_str += temp_word
                    result_list.append(new_str)
                    current_word = current_word[length_diff:]
                    cur_w_len = len(current_word)
                    divs = math.ceil(cur_w_len / limit)
                    init = 0
                    for j in range(1, divs+1):
                        if j == divs:
                            temp_str = current_word[init:]
                            temp_str += ' '
                            result_list.append(temp_str)
                            break
                        else:
                            end_val = j * limit
                            temp_str = current_word[init: end_val]
                            result_list.append(temp_str)
                            init = end_val
                    i += 1

                else:
                    result_list.append(new_str)
                    new_str = ''
        len_of_strings = [len(x) for x in result_list]
        print(result_list)
        print(len_of_strings)



separator('hfjdhfjfkjsdfjsdkfl sdfsdfkjsdfjkdsfhsdkfhksdjhfkjsdfhsdkjfhsdkjfhsdkfhkjsdfjskdfsdkjfhdskjfhkjsdhfkjsdhfkjsdfsdkjfsdkfjshfkjshfkjsdhfkjsdfhk jsdfhkjsdfhkjsdfhkjsdfhksdhfkjsdhfsdkjfsdfhkshfkjsdkhkjghfkjghdfkjghskjghsdkjghksjhgkjkjsdkjfhkjsdfhsdf fhsdkfhksdjfkjsdfhsdkjfhsdkjfhksjdfhkjsdfkjsdfh sdfhjksdhfkjsdhfs jhsdfsd fjksd hfjdskf sd fhsdk fsdh fkjsd hfkjsd fhsd sdhfsdhfkjsdfkjsdhfkjsdhf jfhsdjkfhsdkjfdskfsdk hfjshfsf sdjkhfsdjkf sdfhsd fsdhf sdkfsd', 100)

# separator('fsfsf sfsdfs sdfsdfsdfsdfdf sfsd sdfs sfsdfsdfsdfsdfsdf rr', 100)
