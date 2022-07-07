vmware_string = 'Vm1w3a5re'

def string_sort(vmware_string):
    final_char = []
    num = []
    char = []
    google_string = list("".join(vmware_string))

    for i in vmware_string:

        if i.isalpha():
            char.append(i)
        else:
            num.append(i)

    final_char = "".join(char + num)
    print(final_char)

string_sort(vmware_string)

#Output: Vmware135

