def example():
    shopping = {'Target': ['socks', 'soap','detergent','sponges']}
    shopping['Safeway']=['butter','cake','cookies','milk']
    for key in shopping:
        shopping[key].sort()
    return shopping


def show_all_lists(cart):
    for key, value in cart.items():
        print key, value

def show_the_list(cart,key):
    if key not in cart:
        print "List does not exist"
    elif len(cart[key]) == 0:
        print "List is empty."
    else:
        for item in cart[key]:
            print item

def new_list(cart, key, items):
    if key in cart:
        print "Error: that list already exists"
        return cart
    items = list(set(items))
    items.sort()
    for i in range(len(items)):
        items[i]=items[i].strip()
    cart[key]=items
    return cart

def new_item(cart, key, item):
    cart[key].append(item)
    cart[key].sort()
    return cart

def remove_item(cart, key, item):
    cart[key].remove(item)
    return cart


def remove_list(cart, key):
    del cart[key]
    return cart

def add_multiple_items(cart, key, comma_string):
    items = comma_string.split(",")
    for item in items:
        item = item.strip()
        new_item(cart, key, item)
    return cart

def save_into(cart, file_name):
    with open(file_name, 'w') as outfile:
        outfile.write(str(cart))

def main():
    #shopping=example() Used this before having a file
    shopping = {}
    try:
        cart_file = open("cart.txt", 'r')
        format_type = raw_input('''Enter 1 if the contents are a dictionary,
2 if the format is List: item, item, item ''')
        if format_type == '1':
            shopping = eval(cart_file.read())
        elif format_type == '2':
            for line in cart_file:
                line = line.strip()
                if line != '':
                    parts = line.split(":")
                    key = parts[0].strip()
                    value = parts[1].split(",")
                    for i in range(len(value)):
                        value[i] = value[i].strip()
                    shopping[key] = value
        else:
            print "Okay, starting with empty cart."
        cart_file.close()
    except IOError:  #This try/except makes the code not fail on that specific error.
        print "No file named cart.txt, beginning with empty cart."
    
        
    menu = '''0 - Main Menu
1 - Show all lists.
2 - Show a specific list.
3 - Add a new shopping list.
4 - Add an item to a shopping list.
5 - Remove an item from a shopping list.
6 - Remove a list by nickname.
7 - Add multiple items to a shopping list.
8 - Export all your shopping lists to the standard file.
9 - Export all your shopping lists to a different file.
10 - Exit when you are done.''' 
    print menu
    while(True):
        call = raw_input("Enter a number 0 through 10: ").strip()
        if call == '0':
            print menu
        if call == '1':
            show_all_lists(shopping)
        elif call == '2':
            key = raw_input("Which list would you like?").strip()
            show_the_list(shopping,key)
        elif call == '3':
            key = raw_input("What would you like to name the list? ").strip()
            items = raw_input("Add items to the list (separate with commas): ").split(",")
            shopping = new_list(shopping, key, items)
        elif call == '4':
            key = raw_input("Which list would you like?").strip()
            item = raw_input("Name of item: ").strip()
            shopping = new_item(shopping, key, item)
        elif call == '5':
            key = raw_input("Which list would you like to remove an item from?").strip()
            item = raw_input("Name of item: ").strip()
            shopping = remove_item(shopping, key, item)
        elif call == '6':
            key = raw_input("Which list would you like to remove?")
            shopping = remove_list(shopping, key)
        elif call == '7':
            key = raw_input("Which list would you like?").strip()
            comma_string = raw_input("List items, separated by commas:").strip()
            shopping = add_multiple_items(shopping, key, comma_string)
        elif call == '8':
            file_name = "cart.txt"
            save_into(shopping, file_name)
        elif call == '9':
            file_name = raw_input("Name the file: ").strip()
            save_into(shopping, file_name)
        elif call == '10':
            break
        else:
            print menu





if __name__ == '__main__':
    main()
