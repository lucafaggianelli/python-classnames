def class_names(*arguments):
    classes = []

    for arg in arguments:
        if not arg:
            continue

        argType = type(arg)

        if argType in (str,):
            classes.append(arg)
        elif argType in (int, float):
            classes.append(str(arg))
        elif argType in (list, tuple, set):
            if len(arg):
                inner = class_names(*arg)

                if inner:
                    classes.append(inner)
        elif argType == dict:
            for key, value in arg.items():
                if value:
                    classes.append(key)

    return " ".join(classes)
