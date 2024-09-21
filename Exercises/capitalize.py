def capitalize(param_1):
    if param_1 == "":
        return ""

    param_1 = param_1.lower()
    param_list = param_1.split(" ")

    for i in range(len(param_list)):
        word_list = list(param_list[i])
        for j in range(len(word_list)):
            if (
                ord(word_list[j]) >= ord("a")
                and ord(word_list[j]) <= ord("z")
                or ord(word_list[j]) >= ord("A")
                and ord(word_list[j]) <= ord("Z")
            ):
                word_list[j] = word_list[j].upper()
                break
            else:
                break
        param_list[i] = "".join(word_list)

    return " ".join(param_list)


in1 = "a FiRSt LiTTlE TESt"
in2 = "__second Test A Little Bit   Moar Complex"
in3 = "   But... This iS not THAT COMPLEX"
in4 = "     Okay, this is the last 1239809147801 but not    the least    t"
in5 = ""

print(capitalize(in1))
print(capitalize(in2))
print(capitalize(in3))
print(capitalize(in4))
print(capitalize(in5))
