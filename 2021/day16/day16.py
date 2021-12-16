with open("input.txt", "r") as file:
    codigo=file.read()

hex_to_bin = {"0": "0000","1": "0001","2": "0010","3": "0011","4": "0100","5": "0101","6": "0110","7": "0111","8": "1000","9": "1001","A": "1010","B": "1011","C": "1100","D": "1101","E": "1110","F": "1111"}

n_codigo = ""
for c in codigo:
    n_codigo += hex_to_bin[c]
codigo = n_codigo

total_version = 0
def converte_codigo(codigo):
    global total_version
    pkg_version = int(codigo[:3],2)
    total_version += pkg_version
    pkg_type = int(codigo[3:6],2)

    if pkg_type == 4:
        value = ""
        for i in range(6,len(codigo),5):
            value += codigo[i+1:i+5]
            if codigo[i] == "0":
                break
        value = int(value,2)
        return (5 + i, value)

    else:
        value = 0
        if pkg_type == 1:
            value = 1
        elif pkg_type == 2:
            value = float("inf")
        elif pkg_type in (5,6,7):
            value = -1
        length_type = int(codigo[6])

        if length_type == 0:
            total_lenght = int(codigo[7:22],2)

            lenght = 0
            while lenght<total_lenght:
                out = converte_codigo(codigo[22+lenght:])
                lenght+=out[0]
                if pkg_type == 0:
                    value += out[1]
                elif pkg_type == 1:
                    value *= out[1]
                elif pkg_type == 2:
                    value = min(value,out[1])
                elif pkg_type == 3:
                    value = max(value,out[1])
                else:
                    if value == -1:
                        primeiro = out[1]
                        value = 0
                    else:
                        if pkg_type == 5:
                            value = int(primeiro>out[1])
                        if pkg_type == 6:
                            value = int(primeiro<out[1])
                        if pkg_type == 7:
                            value = int(primeiro==out[1])
            return (22 + total_lenght, value)

        else:
            subpackets = int(codigo[7:18],2)
            lenght = 0
            for _ in range(subpackets):
                out = converte_codigo(codigo[18+lenght:])
                lenght+=out[0]
                if pkg_type == 0:
                    value += out[1]
                elif pkg_type == 1:
                    value *= out[1]
                elif pkg_type == 2:
                    value = min(value,out[1])
                elif pkg_type == 3:
                    value = max(value,out[1])
                else:
                    if value == -1:
                        primeiro = out[1]
                        value = 0
                    else:
                        if pkg_type == 5:
                            value = int(primeiro>out[1])
                        if pkg_type == 6:
                            value = int(primeiro<out[1])
                        if pkg_type == 7:
                            value = int(primeiro==out[1])

            return (18 + lenght, value)
valor_final = converte_codigo(codigo)[1]
print()
print("VERSÃO TOTAL -",total_version)
print("VALOR FINAL -",valor_final)