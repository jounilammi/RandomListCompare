import random
import time


def compareAndPrint(number, top):
    while True:

        list1 = [None] * number
        list2 = [None] * number

        
        for i in range(len(list1)):
            list1[i] = random.randint(0,top)
        
        
        print("List made first:         "," ".join(map(str,list1)))
        k = 0
        i = 0
        start_time = time.time()
        while(True):
            
            while(list2[k] != list1[k]):
                list2[k] = random.randint(0,top)
                i += 1
                print("Second list is currently  {}                  ".format(" ".join(map(str,list2))), end = '\r')
            k += 1
            if(list2 == list1):
                print("")
                print("")
                print("Second list is currently  {}                  ".format(" ".join(map(str,list2))), end = '\r')
                break
        end_time = time.time()
        total_time = round(end_time - start_time, 6)
        break
    print("Randomly generating the second list to match the first list took {} seconds and {} steps".format(total_time,i))
    print("")
   
   
    

    
    
    
def onlyCompare(number, top):
    while True:
        list1 = [None] * number
        list2 = [None] * number

        
        for i in range(len(list1)):
            list1[i] = random.randint(0,top)
        k = 0
        i = 0
        start_time = time.time()
        while(True):
            while(list2[k] != list1[k]):
                list2[k] = random.randint(0,top)
                i +=1
            k += 1
            if(list2 == list1):
                break
        end_time = time.time()
        total_time = round(end_time - start_time, 6)        
        break
    print("First list:  "," ".join(map(str,list1)))
    print("Second list: "," ".join(map(str,list2)))    
    print("Randomly generating the second list to match the first list took {} seconds and {} steps".format(total_time,i))
    print("")
    print("")
   
    
if __name__ == "__main__":
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("")
    print("")
    print("This program will generate two lists of fixed length, fill the first one with random integers from 0 to n,")
    print("and generate the other list, index by index, by trial and error, until the lists match. It will start measuring")
    print("time after the first list has been generated and stop after the lists match.")
    print("")
    while True:
        try:
            print("Leave empty and press enter to quit the program, or enter integers to continue.")
            number = input("List lengths as int: ")
            if number == "":
                exit()
            else:
                number = int(number)
               
                top = int(input("Fill the list with integers from 0 to: "))
        except ValueError:
            print("Your input was neither empty or an integer")
            continue
            
        else:
            print("Do you want the program to print the lists on each try? This makes the operation much slower.")
            print("Note that if the list is longer than your screen is wide, the printing will start to fill the console.")
            while True:
                printing = input("Your choice (y/n):")
                print("")
                printing.lower().strip()
                if printing == "y":
                    compareAndPrint(number, top)
                    break
                elif printing == "n":
                    onlyCompare(number, top)
                    break
                else:
                    print("Choose either 'y' or 'n'")
                    continue
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    