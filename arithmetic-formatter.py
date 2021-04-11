def arithmetic_arranger(prob_list, solve=False):
    top = ""
    bottom = ""
    dashes = ""
    solns = ""

    if len(prob_list) > 5:
        return "Error: Too many problems."
    
    for prob in prob_list:
        prob_parts = prob.split(" ")
        num_1 = prob_parts[0]
        oper = prob_parts[1]
        num_2 = prob_parts[2]

        if not (oper == "+" or oper == "-"):
            return "Error: Operator must be '+' or '-'."

        if not (num_1.isnumeric() and num_2.isnumeric()):
            return "Error: Numbers must only contain digits."

        if len(num_1) > 4 or len(num_2) > 4:
            return "Error: Numbers cannot be more than four digits."

        longr = num_1 if len(num_1) > len(num_2) else num_2
        sp = len(longr) + 2

        top += num_1.rjust(sp) + "    "
        bottom += oper + num_2.rjust(sp-1) + "    "
        dashes += "-" * sp + "    "

        if oper == "+":
            solns += str(int(num_1) + int(num_2)).rjust(sp) + "    "
        elif oper == "-":
            solns += str(int(num_1) - int(num_2)).rjust(sp) + "    "

    top = top.rstrip()
    bottom = bottom.rstrip()
    dashes = dashes.rstrip()
    
    if solve == True:
        return f"{top}\n{bottom}\n{dashes}\n{solns}"
    else:
        return f"{top}\n{bottom}\n{dashes}"

# print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
# print(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))
# print(arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]))
# print(arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]))
# print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]))
# print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True))