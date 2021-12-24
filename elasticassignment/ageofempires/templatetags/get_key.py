from django import template

register = template.Library()

@register.filter(name = 'get_key')
def get_key(dic:dict , key:str):
    source = dic.get("_source",None)
    return source.get(key,"")

@register.filter(name = 'get_dict_key_vals_pairs')
def get_dict_key_vals_pairs(dic:dict , key:str):
    source = dic.get("_source",None)
    dict_vals =  source.get(key,"")
    dict_keys = dict_vals.keys()
    ret_arr = []
    for dic_key in dict_keys:
        string = str(dic_key) +": "+ str(dict_vals.get(dic_key, None))
        ret_arr.append(string)
    return ret_arr
