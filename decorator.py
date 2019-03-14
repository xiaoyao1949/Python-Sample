"""
函数-装饰器 范例
"""
def makebold(fn):
    def wrapped():
        return '<b>' +fn() +'</b>'
    return wrapped

def makeitalic(fn):
    def wrapped():
        return '<i>' + fn() + '</i>'
    return wrapped

@makebold
@makeitalic
def hello():
    return 'hello world'

print(hello())
