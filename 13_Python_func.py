import json


def some_func(*args, **kwargs):
    dict_args = {}
    half = len(args) // len(kwargs)
    for i, key in enumerate(kwargs.values()):
        dict.update({key: list(args[i * half: (i + 1) * half])})
    return dict_args


def load_dict(some_dict, json_path):
    outfile = open(json_path, 'w', encoding='utf-8')
    json.dump(some_dict, outfile)
    outfile.close()


def main():
    poz_arg = list(range(21))
    dict_args = some_func(*poz_arg, ford='ford', kia='kia', lada='lada',
                          nissan='nissan', reno='reno')
    load_dict(dict_args, "output.json")
    return dict_args

if __name__ == '__main__':
    main()
