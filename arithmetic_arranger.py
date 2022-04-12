def arithmetic_arranger(problems, ansQuestion = False):
  num1 = num2 = operator = ""
  line1 = line2 = line3 = line4 = ""
  top = bottom = 0
  problem_space = "    "

  if len(problems) > 5:
    return "Error: Too many problems."

  for questions in problems:
    quest_num = questions.split()
    num1 = quest_num[0]
    operator = quest_num[1]
    num2 = quest_num[2]

    if len(num1) >= 5 or len(num2) >= 5:
      return "Error: Numbers cannot be more than four digits."

    for i in num1:
      if not i.isdigit():
        return "Error: Numbers must only contain digits."
    for i in num2:
      if not i.isdigit():
        return "Error: Numbers must only contain digits."
      
    top = int(num1)
    bottom = int(num2)
    length = max(len(num1), len(num2))
    exceptions = error_handling(num1, num2, operator)

    if exceptions != "":
      return exceptions

    
    if questions != problems[-1]:
      line1 += num1.rjust(length + 2) + problem_space
      line2 += operator + " " + num2.rjust(length) + problem_space
      line3 += "-" * (length + 2) + problem_space
      if ansQuestion == True:
        if operator == "+":
          line4 += str((top + bottom)).rjust(length +2) + problem_space
        if operator == "-":
          line4 += str((top - bottom)).rjust(length +2) + problem_space
    else:
      line1 += num1.rjust(length +2) 
      line2 += operator + " " + num2.rjust(length) 
      line3 += "-" * (length +2)
      if ansQuestion == True:
        if operator == "+":
          line4 += str(top + bottom).rjust(length + 2)
        if operator == "-":
          line4 += str(top - bottom).rjust(length + 2 )

  if ansQuestion:
    return line1 + "\n" + line2 + "\n" + line3 + "\n" + line4
  return line1 + "\n" + line2 + "\n" + line3
          

    
def error_handling(number1, number2, operator): 
    
  #if operator is not + or -
  try:
    if operator != '+' and operator != '-':
        raise Exception
  except:
      return "Error: Operator must be '+' or '-'."
  #returns empty string if all criteria is met
  return ""  


