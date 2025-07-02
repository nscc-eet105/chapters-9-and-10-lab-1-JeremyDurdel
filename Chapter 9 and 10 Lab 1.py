#Jeremy Durdel
#Chapter 9 and 10 Lab 1
#07/02/2025

def main():
    print("Name Processor")
    print()
    full_name = get_full_name()
    full_name = full_name.title()

    first_name, last_name = split_name(full_name)
    print(f"{last_name}, {first_name}")


def get_full_name():
    while True:
        name = input("Enter your name: ").strip()
        if " " in name or "," in name:
            return name
        else:
            print("You must enter your full name.")


def split_name(name):
    if "," in name:
        index = name.split(",")
        first = index[0].strip()
        last = index[1].strip()
    else:
        index = name.split()
        last = index[0]
        first = index[1]
    return last, first


main()