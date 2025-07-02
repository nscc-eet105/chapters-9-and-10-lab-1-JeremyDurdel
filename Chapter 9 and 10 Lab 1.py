#Jeremy Durdel
#Chapter 9 and 10 Lab 1
#07/02/2025

#Main Function, takes information and combines it all
def main():
    print("Name Processor")
    print()
    full_name = get_full_name()
    #Will fix capitalization in the form of a title(first letter upper case, all else lower)
    full_name = full_name.title()

    first_name, last_name = split_name(full_name)
    print(f"{last_name}, {first_name}")


def get_full_name():
    while True:
        name = input("Enter your name: ").strip()
        #This checks for a space or a comma to make sure it's a full name
        if " " in name or "," in name:
            return name
        else:
            print("You must enter your full name.")


def split_name(name):
    if "," in name:
        #Formats based on how the input is formatted
        index = name.split(",")
        first = index[0].strip()
        last = index[1].strip()
    else:
        #Formats based on how the input is formatted
        index = name.split()
        last = index[0]
        first = index[1]
    return last, first


main()