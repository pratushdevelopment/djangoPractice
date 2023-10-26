try :
   #x = 1/0
   x = open('filename','x')
except FileExistsError as e :
   print(e)

finally :
   print('I Looks like a header')

try :
    x = None
    if x is None :
        raise Exception
    
except Exception as e :
    print('I Love Exception')


try :
    gateway = "Gateway:Opened"
    print(gateway)
    x = 2 + '2'
    print(x)

except Exception as e :
    print(f'The Exception caught is {e}')

finally :
    gateway = "Gateway:Closed"
    print(gateway)