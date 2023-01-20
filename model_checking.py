import termcolor


def modelCheck():
    binary_matrix = []

    KB_sum = [2, 4]
    "Statement: (P ^ ~Q) -> R"

    termcolor.cprint("???", "blue")

    ind = 0
    for p in range(2):
        for q in range(2):
            for r in range(2):
                v = implies((p and not q), r == 1)
                binary_matrix.append((ind, p, q, r, v))
                ind += 1

    for i in binary_matrix:
        print(i)


def entails():
    pass



def implies(cond1: bool, cond2: bool):
    if not cond1:
        return 1

    if cond2:
        return 1

    return 0
