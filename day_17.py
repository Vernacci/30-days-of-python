# *args / **kwargs
def greet(*name):
    for n in name:
        print(f'Hello {name}')


greet('vito', 'emanuel', 'bosta', 'frezin', 'mirongas')
