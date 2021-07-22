def arithmetic_arranger(problem_list, show_answer = False):

    if (len(problem_list)) > 5:
        return "Error: Too many problems."

    string = ""
    problem_maxlen = []
    first_row = []
    sign = []
    second_row = []

    for maxlen in range(len(problem_list)):
        temp = problem_list[maxlen].split()
        
        if(len(temp[0]) > 4 or len(temp[2]) > 4):
          return "Error: Numbers cannot be more than four digits."

        if(not temp[0].isdigit() or not temp[2].isdigit()):
          return "Error: Numbers must only contain digits."

        if(temp[1] != '+' and temp[1] != '-'):
          return "Error: Operator must be '+' or '-'."

        first_row.append(temp[0])
        sign.append(temp[1])
        second_row.append(temp[2])
        problem_maxlen.append(max(len(temp[0]), len(temp[2])))

    string = string + "  "
    for index in range(len(problem_list)):
        if(index != len(problem_list) - 1):
            string = string + (problem_maxlen[index] - len(first_row[index])) * " " + first_row[index] + "      "
        else:
            string = string +  (problem_maxlen[index] - len(first_row[index])) * " " + first_row[index] + "\n"
      
    for index in range(len(problem_list)):
        if(index != len(problem_list) - 1):
            string = string +  sign[index] + " " + (problem_maxlen[index] - len(second_row[index])) * " " + second_row[index] + "    "
        else:
            string = string +  sign[index] + " " + (problem_maxlen[index] - len(second_row[index])) * " " + second_row[index] + "\n"

    for index in range(len(problem_list)):
        if(index != len(problem_list) - 1):
            string = string +  "--" + problem_maxlen[index] * '-' + "    "
        else:
            if show_answer == False:
                string = string +  "--" + problem_maxlen[index] * '-'
            else:
                string = string +  "--" + problem_maxlen[index] * '-' + "\n"

    if show_answer == True:
        for index in range(len(problem_list) ):
            if(index != len(problem_list) - 1):
                string = string +  (2 + problem_maxlen[index] - len(str(eval(problem_list[index])))) * " " + str(eval(problem_list[index])) + "    "
            else:
                string = string +  (2 + problem_maxlen[index] - len(str(eval(problem_list[index])))) * " " + str(eval(problem_list[index]))

    return string