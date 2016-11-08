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
    else:
        print cart[key]

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





def main():
    shopping=example()
    menu = '''0 - Main Menu
1 - Show all lists.
2 - Show a specific list.
3 - Add a new shopping list.
4 - Add an item to a shopping list.
5 - Remove an item from a shopping list.
6 - Remove a list by nickname.
7 - Add multiple items to a shopping list.
8 - Exit when you are done.''' 
    print menu
    while(True):
        call = raw_input("Enter a number 0 through 8: ").strip()
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
            break
        else:
            print menu





if __name__ == '__main__':
    main()