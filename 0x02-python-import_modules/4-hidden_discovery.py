#!/usr/bin/python3.8.x
if __name__ == "__main__":
    import hidden_4.pyc
    module_names = dir(hidden_4.pyc)
    for name in module_names:
        if not name.startswith('__'):
            print(name)
