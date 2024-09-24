def reverse_str(string):
    final_str = ''
    for i in range(len(string)-1, -1, -1):
        final_str += string[i]
    return final_str

if __name__ == "__main__":
    print(reverse_str(input("Informe a string: ")))
