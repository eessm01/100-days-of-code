from collections import OrderedDict

favorite_lenguages = OrderedDict()

favorite_lenguages['jen'] = 'python'
favorite_lenguages['sarah'] = 'c'
favorite_lenguages['edward'] = 'ruby'
favorite_lenguages['phil'] = 'python'

for name, lenguage in favorite_lenguages.items():
    print(f'{name}\'s favorite language is {lenguage}.')