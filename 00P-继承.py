"""
OOP-继承 范例
"""
class People(object):
    def sayHello(self):
        pass
    
class Chinese(People):
    def sayHello(self):
        print('你好')
        
class American(People):
    def sayHello(self):
        print('Hello')
        
if __name__ == '__main__':
    p1 = Chinese()
    p2 = American()
    for i in [p1,p2]:
        i.sayHello()