# opens up the text file menu.txt and 
# makes a dictionary of the items on the menu
# with values price and calories 
# The file has a letter and then the 
# A – Add item
# D – Delete item
# U – Update item
# P – Print the menu in descending order of price
# E – End of menu
# After the command character is a list of tab, 
# ‘\t’, separated: name of the menu item, 
# price of the item, the number of calories in the item
def main():
    menu = open("menu.txt","r")
    
    command = " "
    menu_dict={}
    while command!= "E":
        command = menu.read(1)
       
        if command == "A" or command == "U":
            items = menu.readline().split("\t")
            menu_dict[items[0]] = {"price": items[1],
                                   "calories":items[2]}
        elif command == "P":
            sort(menu_dict)
        elif command == "D":
            items = menu.readline().split("\t")
            del menu_dict[items[0]]
            #update 
        
def sort(menu_dict):
    list1 = sorted(menu_dict.items(), key=lambda x: x[1]['price'], reverse=True)
    print("Menu")
    for item in list1:
        print(item)
        
main()
