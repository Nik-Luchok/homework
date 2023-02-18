"""

Find how many unique numbers are in a given list

"""


def main():
    numbers = [3, 6, 7, 12, 234, 4, 2, 67, 3, 2, 1, 4, 3, 2, 234]
    print("Given list:", numbers)

    print("Unique numbers in a list:", len(unique(numbers)))


# define unique function
def unique(list1):
    # initialize unique_list
    unique_list = []

    # iterate over items in a list that we are checkinng
    for item in list1:
        # if item is not yet present in unique_list, we append unique list
        if item not in unique_list:
            unique_list.append(item)
    
    # return unique list
    return unique_list


if __name__ == "__main__":
    main()
