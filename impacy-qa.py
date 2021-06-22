def termCount(search_term, search_text):
    a = len(search_term)
    b = len(search_text)
    frequency = 0

    for i in range(b - a + 1):
        j = 0
        while j < a:
            if (search_text[i + j] != search_term[j]):
                break
            j += 1
 
        if (j == a):
            frequency += 1
            j = 0
    return frequency

if __name__ == '__main__':
    search_text = input("Enter the Text : ")
    search_term = input("Enter the Search term : ")
    answer = input("Do you want to search? Yes or No? : ")

    if answer == 'yes' or answer == 'Yes' or answer == 'y' or answer == 'Y' :
        print("The input" , search_term , "appears" , termCount(search_term, search_text) , "time's in the search content." )
    elif answer == 'no' or answer == 'No' or answer == 'n' or answer == 'N':
        exit    