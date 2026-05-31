while(True): 
    try: 
        n = int(input("Height: ")) 
        if(n > 0 and n <= 8): 
            break 
    except ValueError: 
        continue 
    
for i in range(n): 
    for k in range(n-1, i, -1): 
        print(" ", end="") 
    for j in range(i+1): 
        print("#", end="") 
    print()