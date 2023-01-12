"""Make a chain of function decorators. """
def decor1(func):
        def wrap():
               print("************")
               func()
               print("************")
        return wrap
def decor2(func):
        def wrap():
               print("@@@@@@@@@@@@")
               func()
               print("@@@@@@@@@@@@")
        return wrap
     
@decor1
        
@decor2
def sayhellogfg():
         print("Hello")
def saygfg():
         print("Infobell")
         
sayhellogfg()
saygfg()