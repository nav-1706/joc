def binary_search(a, x):
    
    start = 0;
    end = len(a)-1;
    flag = False;
    
    while(start <= end and flag == False):
        
        mid = (start+end)//2 # // to get the floor value
        
        if(x == a[mid]):
            flag = True;
            print("Elemet found at idx:", mid);
            return;
        
        elif(x < a[mid]): end = mid-1;
            
        else: start = mid+1;
    
    print("Element is not present in the array")
    

a = [1,2,5,7,8,14,16,17,20];
binary_search(a, 17);