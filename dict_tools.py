import copy

def find_key_in_dict(keys_i_want, dictionary):
    keys_i_want_new = copy.deepcopy(keys_i_want)

    def iterate_through_dict(keys_i_want, dic, output):
        for i in dic:
            if i in keys_i_want:
                output[i] = dic[i]
                keys_i_want.remove(i)
            if type(dic[i]) is dict:
                iterate_through_dict(keys_i_want, dic[i], output)        

    d = dict()
    iterate_through_dict(keys_i_want_new, dictionary, d)            
    return d
