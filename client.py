import rpyc
from constCS import *


def main() -> None:
    conn_server_name = rpyc.connect(NAME_SERVER_HOST, NAME_SERVER_PORT)
    print(MAIN_SERVER_NAME)
    server_data = conn_server_name.root.lookup(MAIN_SERVER_NAME)
    print(server_data)
    print(server_data[0])
    conn = rpyc.connect(server_data[0], server_data[1])

    # Inputs
    first_string = input("Input your first string: ")
    second_string = input("Input your second string: ")
    operation = input("Choose one of the following operations -> Concat, Equal, Distance: ")

    # Operations
    if operation == 'Concat':
        response =  conn.root.concat(first_string, second_string)
        print(f"Concatenated strings: {response}")
    elif operation == 'Distance':
        response =  conn.root.levenshtein(first_string, second_string)
        print(f"Levenshtein Distance: {response}")
    elif operation == 'Equal':
        response =  conn.root.equal(first_string, second_string)
        if response:
            print("Strings are equal")
        else:
            print("Strings are not equal")

    else:
        response = "Operation does not exist"


if __name__ == '__main__':
    main()