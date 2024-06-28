def find_list_max_number(num_list : list , k: int):
    num_list_max = []
    for i in range(len(num_list)-(k-1)):
        num_list_max.append(max(num_list[i:i+k]))
    return num_list_max

if __name__ == "__main__":
    print(find_list_max_number([3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1] , k=3))