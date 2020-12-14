my_list = ['A']

# only define constants outside of a function in python (won't change)


def build_list(letter_list):
    new_list = letter_list.copy()
    # copy data before you manipluate it
    print("new list", id(new_list)) 
    print("letter list", id(letter_list))
    new_list.append('B')
    print(new_list)


def increase_number(num):
    num += 1  # same as num = num + 1
    print(num)

    
increase_number(0)
build_list(my_list)



# my_list = []
# print("list after first declared", id(my_list), my_list)

# def grow_list(list):
#     list.append(1)

# grow_list(my_list)
# print(id(my_list), my_list)

# def bigger_number(num):
#     print("number inside bigger_number function", id(num), num)
#     num += 1
#     while number < 4:
#         print("number inside while loop", id(number), number)
#         num += 1
#     print("number after while loop", id(number), number)


# def even_bigger_number(num):
#     print("number inside even_bigger_number", id(number), number)
#     number += 5
#     print("number after append inside even_bigger_number", id(number), number)

# bigger_number(number)
# print("number after bigger_number is called", id(number), number)
# even_bigger_number(number)
# print("List after even_bigger is called", id(number), number)
