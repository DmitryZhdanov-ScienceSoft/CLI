import fire

class Math(object):
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

def greet(name):
    return f"Hello, {name}!"

if __name__ == '__main__':
    fire.Fire({
        'math': Math,
        'greet': greet
    })
