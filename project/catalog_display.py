def display(id_number):
    with open(id_number+".txt", 'r') as file:
        print file.read()
