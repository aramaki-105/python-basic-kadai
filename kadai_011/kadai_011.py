array = ["水","金","地","火","木","土","天","海","冥"]


for index in array:
    print(index)

index = 0
len_array = len(array)

while index < len_array:
    planet = array[index]
    index = index + 1
    print(planet)