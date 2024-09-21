def capitalize(param_1):
    if param_1 == "":
        return ""

    return " ".join([word.capitalize() for word in param_1.split()])


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
