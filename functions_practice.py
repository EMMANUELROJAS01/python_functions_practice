def hello():
    print('hello, user')


def pack(a,b,c):
        return [a, b, c]

 
def eat_lunch(my_lunch):
 if len(my_lunch) == 0: print('my lunchbox is empty') 
 for food_index in range(len(my_lunch)):
    if food_index == 0:
        print(f'first I ate{my_lunch[food_index]}')
        if food_index < (len(my_lunch) -1):
                print(f'then I ate{my_lunch[food_index]}')
                        

hello()
print(pack('a', 'b', 'c'))
print(pack(1,2,3))


eat_lunch([])
eat_lunch(['rice'])
eat_lunch(['beef','chicken','rice','beans'])