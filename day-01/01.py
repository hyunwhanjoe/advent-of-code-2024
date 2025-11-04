with open("input.txt", "r") as f:
    left = []
    right = []
    
    for line in f:
        ids = line.strip().split('   ')
        left.append( int(ids[0]))
        right.append( int(ids[1]))
    
    left.sort()
    right.sort()
    
    sum = 0
    for i in range( len(left)):
        diff = left[i] - right[i]
        sum += abs(diff)
        
    print(sum)