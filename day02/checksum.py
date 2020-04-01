# definujeme funkce
def find_max(input):
    max = 0
   
    for x in input:
        if max < x:
            max = x
    return max


def find_min(input):
    min = input[1]
   
    for x in input:
        if min > x:
            min = x
    return min


##########################################################################################################################################
# tady nám běží program


maximum = find_max([4, 7, 1, 5])
minimum = find_min([4, 7, 1, 5])
print(maximum)
print(minimum)

