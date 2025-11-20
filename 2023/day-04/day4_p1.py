# input = 'sample.txt'
input = 'input.txt'

with open(input, "r") as f:
    total_pts = 0
    
    for line in f:
        line = line.split('|')
        winning_nums = line[0].split(':')
        winning_nums = winning_nums[1].split()
        winning_nums = set(winning_nums)
        
        nums = line[1].split()
        
        points = 0
        match = 0
        for num in nums:
            if num in winning_nums:
                if match == 0:
                    points += 1
                    match += 1
                else:
                    points += match
                    match *= 2
        
        total_pts += points