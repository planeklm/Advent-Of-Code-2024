def main():
    list1 = []
    list2 = []
    list3 = []
    result = 0
    
    with open("input.txt", 'r') as file:
        for line in file:
            numbers = line.strip().split()
            list1.append(int(numbers[0]))
            list2.append(int(numbers[1]))

    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)


    for i in range(len(sorted_list1)):
        current_item = i 
        value = sorted_list1[current_item] - sorted_list2[current_item]
        list3.append(abs(value))

    for i in range(len(list3)):
        result += list3[i]

    print(result)

main()
