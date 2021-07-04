import re

def arithmetic_arranger(problems, bool = False):
    if len(problems)> 5:
        return "Error: Too many problems."
        
    for item in problems:
        element = item.split(" ")
        if element[1] not in ["+","-"]:
            return "Error: Operator must be '+' or '-'."
            
        if not element[0].isdigit() or not element[2].isdigit():
            return "Error: Numbers must only contain digits."
            
        if len(element[0]) > 4 or len(element[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        

    big_arr = []
    arranged_problems = ""

    for item in problems:
        numbers = []
        length = 0
        k = re.findall("[0-9]*",item)
        for i in re.findall("[+-]",item):
            operator = i
        for element in k:
            if element.isdigit():
                numbers.append(element)
            if len(element) > length:
                length = len(element)                

        if operator == "+":
            ans = int(numbers[0])+int(numbers[1])
        if operator == "-":
            ans = int(numbers[0])-int(numbers[1])     
        
        mod_len = length + 2
        array = []
        if len(numbers[0]) > len(numbers[1]):
            mod_len1 = length
            row1 = numbers[0].rjust(mod_len)
            row2 = operator+" "+numbers[1].rjust(mod_len1)
        else:
            row1 = numbers[0].rjust(mod_len)
            row2 = (operator+" "+numbers[1]).rjust(mod_len)
        line = "-"*mod_len
        row3 = str(ans).rjust(mod_len)
        array.append(row1)
        array.append(row2)
        array.append(line)

        value = 3
        if bool:
            array.append(row3)
            value = 4

        
        big_arr.append(array)

    for j in range(value):
        for i in range(len(big_arr)):
            if i < len(big_arr)-1:
                arranged_problems = arranged_problems+big_arr[i][j]+"    "
            else:
                arranged_problems = arranged_problems+big_arr[i][j]
        if j < value-1:
            arranged_problems = arranged_problems+"\n"

    return arranged_problems
        
print(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))

# print("   32         1      45      123\n- 698    - 3801    + 43    +  49\n-----    ------    ----    -----\n -666     -3800      88      172")