import json

def flatten_json(y):
    out = {}
    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a.replace("-","_").replace(".","_").replace("/","_") + '.')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '.')
                i += 1
        else:
            try:
                x = json.loads(x, strict=False)
                x = flatten(x)
            except: pass

            out[name[:-1]] = x
    flatten(y)
    return out
