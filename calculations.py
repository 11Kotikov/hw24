def rational_calc(problem_list):
    while '*' in problem_list or '/' in problem_list:
        for i in range(1, len(problem_list), 2):
            if problem_list[i] == '*':
                result = problem_list.pop(i + 1) * problem_list.pop(i - 1)
                problem_list[i - 1] = result
                break
            elif problem_list[i] == '/':
                result = problem_list.pop(i - 1) / problem_list.pop(i)
                problem_list[i - 1] = result
                break

    while '+' in problem_list or '-' in problem_list:
        for i in range(1, len(problem_list), 2):
            if problem_list[i] == '-':
                result = problem_list.pop(i - 1) - problem_list.pop(i)
                problem_list[i - 1] = result
                break
            elif problem_list[i] == '+':
                result = problem_list.pop(i + 1) + problem_list.pop(i - 1)
                problem_list[i - 1] = result
                break
    # print(result)
    # print (problem_list)
    return problem_list


def get_result(data):
    # lg.write_data(f'Пример подготовленный для решения: {data}')
    while '(' in data:
        first_i = len(data) - data[::-1].index('(') - 1
        second_i = first_i + data[first_i + 1:].index(')') + 1
        data = data[:first_i] + \
            rational_calc(data[first_i + 1:second_i]) + data[second_i + 1:]
    else:
        print('I\'m doing calculations')
        # lg.write_data(f'Результат открытия скобок: {data}')
    data = rational_calc(data)
    return ''.join(map(str, data))
