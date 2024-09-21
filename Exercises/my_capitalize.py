def my_capitalize(param_1):
    if param_1 == "":
        return ""

    param_1 = param_1.lower()
    param_list = list(param_1)

    for i in range(len(param_list)):
        if (
            ord(param_list[i]) >= ord("a")
            and ord(param_list[i]) <= ord("z")
            or ord(param_list[i]) >= ord("A")
            and ord(param_list[i] <= ord("Z"))
        ):
            param_list[i] = param_list[i].upper()
            break

    return "".join(param_list)


in1 = "abc"
in2 = ""
in3 = "AbcE Fgef1"
in4 = "    AbcE     Fgef1   "

print(my_capitalize(in1))
print(my_capitalize(in2))
print(my_capitalize(in3))
print(my_capitalize(in4))
