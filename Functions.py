#FUNCTIONS

def get_sum(num):
    sum = 0
    for i in range(num+1):
        print(i)
        sum += i
    return sum

def get_list(num):
    arr = []
    for i in range(1,num+1):
        arr.append(i)
    return arr


def greet(place):
    print('Vanakkam daa mapla '+place+ ' la irunthu!')

sum = get_sum(5)
print(sum)

greet("Mathalamparai")

arr = get_list(10)

print(arr)



