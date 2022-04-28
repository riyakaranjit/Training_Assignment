def remove_duplicates(input_list: list) -> list:
    """
    Remove all the duplicate element using while loop.
    :param input_list: Given input list
    :return: list: Output with only unique elements
    """
    i = 0
    while i < len(input_list):
        j = i + 1
        while j < len(input_list):
            if input_list[i] == input_list[j]:
                del input_list[j]
            else:
                j += 1
        i += 1
    return input_list


def sandwich_func(sandwich_orders: list) -> list:
    """
    Taking sandwich orders and adding the finished to output list.
    :param sandwich_orders: Various types of sandwich
    :return: list: list of finished sandwich
    """
    finished_sandwiches = []
    i = 0
    while i < len(sandwich_orders):
        print(f'I  made your {sandwich_orders[i]}.')
        finished_sandwiches.append(sandwich_orders[i])
        i += 1
    return finished_sandwiches


def dream_vacation_survey():
    """
    A dream vacation survey.
    :return: str: Summary about of all the surveys
    """
    survey_responses = {}
    active_polling = True
    while active_polling:
        name = input('Enter your name: ')
        dream_destination = input('If you could visit one place in the world, where would you go?: ')
        reason = input('Why would you like to go there?: ')
        continue_survey = input('Would you like to fill another survey? (yes/no)')
        survey_responses[name] = {}
        survey_responses[name]['dream_destination'] = dream_destination
        survey_responses[name]['reason'] = reason
        if continue_survey == 'no':
            active_polling = False
    for name, survey_response in survey_responses.items():
        return (f"{name.title()} would like to go to {survey_response['dream_destination'].title()} "
                f"because it is {survey_response['reason']}.")
    # return survey_responses


def main():
    bird = ['crows', 'pigeon', 'eagles', 'falcon', 'pigeon', 'falcon', 'falcon']
    print(f'After removing all the duplicates form the list {bird}: \n {remove_duplicates(bird)}')

    sandwich_list = input('Enter the name of various sandwiches separated by comma: ').split(',')
    print(f'The list of all the finished sandwiched are: {sandwich_func(sandwich_list)}')

    print(dream_vacation_survey())


if __name__ == '__main__':
    main()
