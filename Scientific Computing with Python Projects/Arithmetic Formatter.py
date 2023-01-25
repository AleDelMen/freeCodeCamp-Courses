#This code takes a list of arithmetic problems as input and prints them out in a neatly arranged format. 
#If the show parameter is set to True, it will also print the answer to each problem. 
#Otherwise, it will just print the problems. If there are more than 5 problems, it will return an error message.
def arithmetic_arranger(problems, show = False):
  if len(problems) <= 5 :
    arranged_problems = ""
    aux_first_string= ""
    aux_second_string= ""
    aux_third_string= ""
    aux_fourth_string= ""
    count = 0
    for i in problems:
      aux_list = i.split()
      if aux_list[1] != "+" and aux_list[1] != "-":
            return "Error: Operator must be '+' or '-'."
      if len(aux_list[0]) > 4 or len(aux_list[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
      if aux_list[0].isdigit() != True or aux_list[2].isdigit() != True:
            return "Error: Numbers must only contain digits."
      
      diference = abs(len(aux_list[2]) - len(aux_list[0]))
      if len(aux_list[2]) > len(aux_list[0]):
        aux_list[0] = aux_list[0].rjust(len(aux_list[0]) + diference)
      elif len(aux_list[2]) < len(aux_list[0]):
        aux_list[2] = aux_list[2].rjust(len(aux_list[2]) + diference)

      aux_first_string += "  " + aux_list[0]
      aux_second_string += aux_list[1] + " " + aux_list[2]
      aux_third_string += (len(aux_list[1] + aux_list[2]) + 1)*"-"
      answer = eval(i)
      if answer > 0 and (len(str(answer)) <= len(aux_list[0]) or len(str(answer)) <= len(aux_list[2])):
        ans_str = " " + str(answer)
      else:
        ans_str = str(answer)
      aux_fourth_string += " " + ans_str
      if count != len(problems) - 1:
            aux_first_string += "    "
            aux_second_string += "    "
            aux_third_string += "    "
            aux_fourth_string += "    "
      count += 1

    if show == True:
      arranged_problems = aux_first_string + "\n" + aux_second_string + "\n" + aux_third_string + "\n" + aux_fourth_string
    else:
      arranged_problems = aux_first_string + "\n" + aux_second_string + "\n" + aux_third_string
      
  else:
    arranged_problems = "Error: Too many problems."
  return arranged_problems


print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))

'''
['3801 - 2', '123 + 49']
['3 + 855', '3801 - 2', '45 + 43', '123 + 49']
['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49']
'''
