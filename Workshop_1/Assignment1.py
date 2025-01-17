def square(x):
    """
    This is a demo function
    Where in you just return square of the number
    args:
        x (int)
    returns:
        y (int)
    ex:
        x = 5
        ## then
        y = 25
    """

    y=x*x
    return y


def word_is_palindrome(string):
    """
    This function returns True if the given string is
    a Palindrome
    args:
        string (str)
    returns:
        flag (bool)
    ex:
        string = 'abcba'
        ## then
        flag = True
    """

    x=len(string) 
    for i in (x) :
        if string[i]==string[x-i-1]:
            flag=true
        else :
            flag=false
    
    return flag


def sqrt_of_numbers(num):
    """
    This function returns the magnitude of the square root of the number
    args:
        num (int) Need not be positive
    returns:
        sqroot (float) rounded off upto 2 decimal places.
    ex:
        num = 27
        ## then
        sqroot = 5.20
    """
    if num < 0:
        raise ValueError('Number must be positive')

    else :
        return round(pow(num, 0.5), 2) 
    


def Maximum(arr):
    """
    This function returns first maximum and the second maximum
    number in the array
    args:
        arr (list)
    returns:
        Max1, Max2 (int, int)
    ex:
        arr = [1, 2, 3, 4, 5]
        ## then
        Max1, Max2 = 5, 4
    """

    arr.sort() 
    return arr[-1],arr[-2]


def even_sort(arr):
    """
    This function sorts the array giving higher preference to even numbers
    args:
        arr (list)
    returns:
        sort_arr (list)
    ex:
        arr = [15, 2, 6, 88, 7]
        ## then
        sort_arr = [2, 6, 88 ,7 ,15]
        ## This is any even number is smaller than any odd number
    """

    arr. sort() 
    for i in range(len(arr)) :
        for j in range(len(arr) -1-i) :
            t =arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=t
    return arr
    




def eqn_solver(A, B, C):
    """
    This function solves a two variable system
    i.e.,
        A = [ 1, 2 ]
        B = [ 3, 4 ]
        C = [ 5, 6 ]
        then it means
        1x + 3y = 5
        2x + 4y = 6
        Hence you are required to find x, y for such a linear system
    args:
        A, B, C (list, list, list) representing coefficients in the equation
    returns:
        x, y (float, float)
    """

    y=((A[0]*C[1]-C[1]*A[0]) /(A[0]*B[1]-B[1]*A[0])) 
    x=((B[0]*C[1]-C[1]*B[0]) /(B[0]*A[1]-A[1]*B[0])) 
    return x, y


def swap_case(string):
    """
    This function swaps the case of the string.
    args:
        string (str)
    returns:
        string (str)
    ex:
        string = 'Hello World'
        ## then
        string = 'hELLO wORLD'
    """
    a=""
    l=strlen(string) 
    for i in l:
        if string[i].isupper() :
            a=a+string[i].lower() 
        if string[i].islower:
            a=a+string[i].upper
        else:
            a=a+string[i]
    return a


def is_prime(num):
    """
    This function returns True if the number is prime
    args:
        num (int)
    returns:
        flag (bool)
    """

    flag=True
    if num==1:
        flag=False
    if num>1:
        for i in range(2, num) :
            if (num%i) ==0:
                flag=False
                break
    return flag


def is_leap_year(year):
    """
    This function returns True if the year is leap year
    args:
        year (int)
    returns:
        flag (bool)
    """

    if(year%4) ==0:
        flag=True
     else:
        flag=False
    return flag


def is_perfect_square(num):
    """
    This function returns True if the number is perfect square i.e. it is a square of some integer.
    args:
        num (int)
    returns:
        flag (bool)
    """

    flag=True
    if int(pow(num, 0.5)) -pow(num, 0.5) ==0:
        flag=False
    return flag
    


def is_perfect_number(num):
    """
    This function returns True if the number is perfect number.
    A perfect number is a positive integer that is equal to the sum of its proper positive divisors.
    For example 6 is a perfect number because 1+2+3 = 6
    args:
        num (int)
    returns:
        flag (bool)
    ex:
        num = 6
        ## then
        flag = True

        num = 7
        ## then
        flag = False
    """
    flag=False
    a=[]
    for i in range(1, num) :
        if num%i==0:
            a. append(i)
    if sum(a)==num:
        flag=True
    return flag


def resize_array(a):
    """
    This function resizes a 1D array to 2D array of size 2x3
    args:
        a (np.array) of size 1x6
    returns:
        b (np.array) of size 2x3
    ex:
        a = np.array([1, 2, 3, 4, 5, 6])
        ## then
        b = np.array([[1, 2, 3], [4, 5, 6]])
    """

    # Code Here
    import numpy as np
    B=np.array(a) 
    
    return B. reshape(2, 3) 


def reverse_step_array(a):
    """
    This function returns the reversed array with step size of 3.
    args:
        a (np.array)
    returns:
        b (np.array)
    ex:
        a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
        ## then
        b = np.array([9, 6, 3])
    """

    # Code Here
    return a[::-3]


def reverse_words(string):
    """
    This function reverses the words in the string.
    args:
        string (str)
    returns:
        string (str)
    ex:
        string = 'Hello Again World'
        ## then
        string = 'World Again Hello'
    """

    # Code Here
    a=[]
    s=""
    a=string.split('') 
    for i in range (len(a)) :
        s=s+""+a[-1]
        a. pop(-1) 
    return s. strip() 


def count_characters(string):
    """
    This function counts the frequency of characters(ignore spaces as characters) in the input string.
    args:
        string (str)
    returns:
        dict (dict)
    ex:
        string = 'Hello World'
        ## then
        dict = {'H': 1, 'e': 1, 'l': 3, 'o': 2, 'W': 1, 'r': 1, 'd': 1}
    """

    # Code Here
    all_freq={}
    for i in string:
        if i in all_freq:
            all_freq[i]+=1
        else :
            all_freq[i]=1
    if ''in all_freq  .keys():
        del all_freq['']
        
    return all_freq


def remove_special_characters(string):
    """
    This function removes the special characters from the input string. Special characters are those which are not letters or numbers.
    args:
        string (str)
    returns:
        string (str)
    ex:
        str = 'Hello, World! 123$ th15 1s 4 t35t str1ng'
        ## then
        str = 'Hello World 123 th15 1s 4 t35t str1ng'
    """

    # Code Here
    sample=[]
    for i in range(len(string):
                   if string[i].isupper() or string[i].islower() or string[i].isdigit() or string[i]=='':
                           sample. append(string[i]) 
                   ns="".join(sample) 
                   
                   
    return ns


def sort_tuple_of_tuples(input_tuple):
    """
    This function sorts the input tuple of tuples by the second item.
    args:
        input_tuple (tuple)
    returns:
        input_tuple (tuple)
    ex:
        input_tuple: (('a', 55), ('z', 1), ('f', 37), ('w', 19))
        ## then
        input_tuple: (('z', 1), ('w', 19), ('f', 37), ('a', 55))
    """

    # Code Here
    l=[]
    for i in range(len(input_tuple) :
                   l. append(input_tuple[i]) 
    for i in range(len(input_tuple)-1):
                   for j in range(0, len(input_tuple) -i-1):
                           if l[j][1]>l[j+1][1]:
                                    t=l[j]
                                    l[j]=l[j+1]
                                    l[j+1]=t
                   
                   
                   
    return tuple(1) 


def alpha_numeric_words(string):
    """
    This function finds words with both alphabets and numbers from an input string.
    args:
        string (str)
    returns:
        string (str)
    ex:
        string: "Hey there33 how11 are you1"
        ## then
        string: "there33 how11 you1"
    """

    # Code Here
    res=[]
    temp=string.split() 
    for idx in temp:
        if any(chr.isalpha() for chr in idx) and any(chr.isdigit() for chr in idx) :
            res. append(idx) 
            
    return ''. join(res) 


def count_them_all(string):
    """
    This function counts all letters, digits, and special symbols from an input string.
    args:
        string (str)
    returns:
        dict (dict)
    ex:
        string: "IdDk3837#$fsd%%"
        ## then
        dict: {'Characters': 7, 'Numbers': 4, 'Symbols': 4}
    """

    # Code Here
    d=0
    s=0
    c=0
    for i in range (len(string)) :
        if string[i].isdigit() :
            d=d+1
        elif string[i].isupper() or string[i].islower() :
            c=c+1
        elif string [i]! ='':
            s=s+1
      r={ 'characters':c , 'numbers':d, 'symbols':s}
            
    return r


def hash_supremacy(string):
    """
    This function replaces each special symbol with '#' in the input string.
    args:
        string (str)
    returns:
        string (str)
    ex:
        string: "&He was a^%$ great @guy"
        ## then
        string: "#He was a### great #guy"
    """
    a=""
    for i in range(len(string)) :
        if string[i].isdigit() or string[i].isupper() or string[i].islower() :
            a=a+string[i]
        else:
            a=a+"#"
    return a
