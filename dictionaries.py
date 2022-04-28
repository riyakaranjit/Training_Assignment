def list_to_dict(list1: list, list2: list) -> dict:
    student_record = {Students[i]: (Marks[i]) for i in range(len(Students))}
    lowest_value = min(student_record.values())
    print(lowest_value)
    new_student_records = {k: v for k, v in student_record.items() if v != lowest_value}
    return new_student_records


def dictionary_to_list(input_dict: dict) -> str:
    key_list = list(input_dict.keys())
    value_list = list(input_dict.values())
    return f'\n Key List {key_list}, Value List:{value_list}'


def accessing_dictionary(input_dict: dict) -> str:
    """
    :param input_dict: Given nested dictionary
    :return: Accessing each key and values in the dictionary
    """
    usernames_list = []
    name_list = []
    age_list = []
    poison_list = []
    for username, user_info in input_dict.items():
        usernames_list.append(username)

        name_list.append(user_info.get('name'))
        age_list.append(user_info.get('age'))
        poison_list.append(user_info.get('poison'))

    return '\n Username:{} \n Name: {} \n Age: {} \n Poison:{}'.format(usernames_list, name_list, age_list, poison_list)


def milk_carton_func(expiry_date, vol, price, brand):
    milk_carton = {}
    milk_carton['Expiration date'] = expiry_date
    milk_carton['Volume'] = vol
    milk_carton['Cost'] = price
    milk_carton['Brand name'] = brand
    return milk_carton


def main():
    Students = ['jack', 'jill', 'david', 'silva', 'ronaldo']
    Marks = [55, 56, 57, 66, 76]
    Euro = {'France': 5, 'Germany': 2, 'Portugal': 3, 'Hungary': 6}
    users = {'g91': {'name': 'Aron', 'age': 55, 'poison': 'Old monk'},
             'twir56': {'name': 'Visakha', 'age': 26, 'poison': 'coca cola'},
             'jsdl8': {'name': 'Saudi', 'age': 12, 'poison': 'hinwa'}}

    print("List to dictionary without the lowest value: ", list_to_dict(Students, Marks))

    print('Dictionary to list: ', dictionary_to_list(Euro))

    print('Accessing all the values in dictionary: ', accessing_dictionary(users))

    expiration_date = tuple(map(int, input('Enter the expiration day month and year of milk: ').split()))
    volume = float(input("Enter the volume of the milk: "))
    cost = int(input("Enter the cost of the milk.: "))
    brand_name = input("Enter the brand name of the milk: ")
    milk_cartoon = milk_carton_func(expiration_date, volume, cost, brand_name)
    print(milk_cartoon)
    print(f'The cost of six cartons of milk based on the cost of the milk_carton is: Rs. {6 * milk_cartoon["Cost"]}')


if __name__ == "__main__":
    main()
