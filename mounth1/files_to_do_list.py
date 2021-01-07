def write_to_file(line):
    new_file = open("text.txt", "a")
    new_file.write(f"{line}\n")
    new_file.close()

def read_from_file():
    file = open("text.txt", "r")
    lines = file.readlines()
    file.close()
    return lines

def main():
    while True:
        print("1) Add a work")
        print("2) Show to do list")
        print("3) Exit")
        option = int(input("Choose a variant: "))

        if option == 1:
            name = input("Work's name: ")
            deadline = input("Deadline: ")
            write_to_file(f"{name} | {deadline}")

        if option == 2:
            lines = read_from_file()
            for i in lines:
                print(i)

        if option == 3:
            print("Exit...")
            break

main()