"""
Write a program that takes a string, will perform a transformation and return it.
For each of the letters of the parameter string switch it by the next one in alphabetical order.

'z' becomes 'a' and 'Z' becomes 'A'. Case remains unaffected.
"""


def rotone(param_1):
    if param_1 == "":
        return ""

    param_list = list(param_1)
    for i in range(len(param_list)):
        if param_list[i] >= "a" or param_list[i] <= "z":
            param_list[i] = (int(param_list[i]) + 1 - 97 + 26) % 26 + 97

    return "".join(param_list)


in1 = "abc"
in2 = "AkjhZ zLKIJz , 23y "
in3 = ""

print(rotone(in1))
