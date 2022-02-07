from math import fabs
import random

chips = {1:'green', 2:'gray', 3:'yellow', 4:'red', 5:'blue', 6:'white', 7:'orange', 8:'pink'}


def code_generator():
    rez_code = [0, 0, 0, 0]
    for i in range(len(rez_code)):
        rez_code[i] = random.choice(list(chips.keys()))
    return rez_code

def code_input():
    flags_error = False
    while not flags_error:
        string_code = input('Entet code :')
        rez_code = string_code.split(' ')
        rez_code = list(map(int, rez_code))
        for i in rez_code:
            if 0 < i < 9 and isinstance(i, int):
                pass
            else:
                print('Input error')
                flags_error = False
                break
            flags_error = True
    return rez_code


def master(input, code):
    red, white = 0, 0
    for i in range(len(input)):
        if input[i] == code[i]:
            red += 1
        elif input[i] in code:
            if input[code.index(input[i])] != code[code.index(input[i])]:            
                white += 1
    return [red, white]



def main():
    print('MASTERMIND')
    code = code_generator()
    attemp = 1
    while attemp < 14:  
        code_string = code_input()
        table = master(code_string, code)
        print(table, end=' ')
        print(f'attemp = {attemp}')
        attemp += 1
        if table[0] == 4:
            print('YOU WIN!')
            break


if __name__ == '__main__':
    main()