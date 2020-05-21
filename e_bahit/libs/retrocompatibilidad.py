from sys import version_info as version

def echo(data):
    if version.major == 2: 
        exec("print \"{}\"".format(data))
    else: 
        exec ("print(\"{}\")".format(data))


def get(label):
    if version.major == 2:
        exec("data = raw_input(\"{}\")".format(label))
    else:
        exec("data = input(\"{}\")".format(label))
    return locals()['data']