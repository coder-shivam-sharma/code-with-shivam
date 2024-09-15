import ctypes

class Meralist:
    def __init__(self):
        self.size=1
        self.n=0
        self.A=self._make_array(self.size)  #make a array of size = self.size and store in a variable

    def _make_array(self,capacity):      # this function creates a C types array of size capacity 
        return (capacity*ctypes.py_object)()

    def __len__(self):              # this will give us the size of the meralist
        return self.n

    def append(self,item):        # this will add up the new items in our array
        if self.size == self.n:   # check if arrays is complete filled 
            # resize the array
            self._resize(self.size *2)    # resizing array with the double size 
        #appending 
        self.A[self.n] = item              # assigning  the item value to the index placed inside the array 
        self.n = self.n + 1             # count that particular number which is inserted in the array in the total items of the array 

    def _resize(self,new_capacity):
        B=self._make_array(new_capacity)       # make a array with double size 
        self.size = new_capacity              # now assigning the new array size to a array 
        # COPY over data in new array 
        for i in range(self.n):
            B[i] = self.A[i]       # assigning all the items of A to new array B
        #reassigning the arrays  B to A 
        self.A=B

    def __str__(self):    #this magic function is used to print 
        # formate [1,2,3,4]
        result=""                  # this is the empty string which is used further as a empty container
        for i in range(self.n):            # the for loop will pick one by one item from a raay and store in a string 
            result = result + str(self.A[i]) + ","   # here we use String concatenation concept
        return "[" + result[:-1] +"]"            # this type of arrangement is only for getting desire formate  

    def __getitem__(self,index):                # for access square brackets [] we use magic method name __getitem__
        if index >=0 and index < self.n:         # this will be checked that the index value lies between 0 and total item of the array 
            return self.A[index]               # this will return our item which is placed at that index 
        if index <0 and index>=-(self.__len__()): # this is used for negative index value 
            if self.n > abs(index):
                return self.A[self.n - abs(index)]      
        else:
            return "<...INDEX ERROR...>"        # if index is not lies in that range then we will get a message index error 

    def pop(self):               # pop function used to delete item using index value :   this is only function who show the value which is he deleted  
        if self.n == 0:          # this is the condition to check list is empty or not 
            return "Empty List"
        
        print(self.A[self.n-1])   # this will return us deleted item name 
        self.n = self.n -1

    def clear(self):              # this will remove all the items of the list ; logic : - i) make array size 1 and no of item is 0
        self.n = 0            #assigning no. of item in array is 0
        self.size = 1         # assigning the size of the array is 1 

    def find(self,item):        # this function is used to find any item in a array and return it index value 
        for i in range(self.n):     
            if self.A[i] == item:   # checking the given item exectly match in which item  
                return i            # return the matched item index value 
        return "<.....VALUE ERROR......>"        # if item is not matched then show that message
   
    def insert(self,pos,item):    # this function is used to placed item at their desire placed 
        if self.size == self.n:     # checking the array is complete filled or not
            self._resize(self.n*2)   # if filled then resize the array
        if pos >= 0 and pos <= self.n:    # checking that position lies in the range or not 
            for i in range(self.n,pos,-1):
                self.A[i] =self.A[i-1]        # now at there item will be assigned to the higher index value # in other words we jump items in the forward direction(increasing index value ) till the position does not come.
            self.A[pos] = item    # put that item in that position which you mentioned(assing value at the indexed position)
        else:
            self.A[self.n] = item            # the index is out of range then item placed at the end of the list
        self.n = self.n +1          # adjust the size of array by increase the the size due to new member(item )

    def __delitem__(self,pos):        # this function is used to assign a del keyword
        #delete                         # logic :- 1) find that number then you get its position
        for i in range(pos,self.n -1):  # after getting index number then assign forwarded item to backward till that index number   
            self.A[i] = self.A[i +1]
        self.n = self.n -1        
        
    def extend(self,item):
        if self.size == self.n:     # checking the array is complete filled or not
            self._resize(self.n*2)   # if filled then resize the array
        self.A[self.n] = item            # the index is out of range then item placed at the end of the list
        self.n = self.n +1          # adjust the size of array by increase the the size due to new member(item )

    def remove(self,item):        # this function is used to remove any item 
        a=self.find(item)               # logic :- 1) find that number then you get its position  
        for i in range(a,self.n -1):    # after getting index number then assign forwarded item to backward till that index number 
            self.A[i] = self.A[i +1]    # another words jump the items backward 
        self.n = self.n -1        
