# LAB 9
# Ruvi Jaimes

# Reads an ordered list of numbers from two files 
# and prints each list of numbers, merges
# the two list, orders the new list, and stores 
# the list in a sequential pickle file. 

# catches valueError and typeError

 
import pickle 
def read_lines(file):
    list1 = []
    for line in file:
        try:
            list1 += [int(line)]  
        except(ValueError,TypeError): #go to the next line
            print ("ERROR: There were other values found in the file.")     
    return list1
def merge (file1, file2):
    new_list = []
    i=j=0
    while i < len(file1) and j <len(file2):
        if file1[i]<= file2[j]:
            new_list.append(file1[i])
            i += 1
        else:
            new_list.append(file2[j])
            j +=1
    if i < len(file1):
        new_list.extend(file1[i:])
    elif j < len(file2):
        new_list.extend(file2[j:])
                                
    return new_list           
    
def main():
    file1 = open("data1.txt","r") 
    file2 = open("data2.txt","r")
    file1_list = read_lines(file1)
    print("List one has these values: ", file1_list)
    file2_list = read_lines(file2)
    print("List two has these values: ", file2_list)
    final_list = merge(file1_list, file2_list)
    print("This is your list: ", final_list)
    print("Pickling list...")
    f = open("result.pkl","wb")
    pickle.dump(final_list,f)
    f.close()
   
   
main()
# f=open("result.pkl","rb")
# b= pickle.load(f)
# f.close()
# print(b)
