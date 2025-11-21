from tqdm import tqdm

# input = 'sample.txt'
input = 'input.txt'

# Took 3 seconds to run
with open(input, "r") as f:
    scratchcards = 0
    cards = []
    
    lines = f.readlines()
    for line in lines:
        line = line.split('|')
        winning_nums = line[0].split(':')
        winning_nums = winning_nums[1].split()
        
        nums = line[1].split()
        
        cards.append( [winning_nums, nums, 1])
    
    for i, card in enumerate( tqdm(cards)):
        winning_nums = set(card[0])
        nums = set(card[1])
        n_matches = len(winning_nums & nums)
        
        for j in range(card[2]): # n_copies
            if n_matches > 0:
                for k in range(1, n_matches+1):
                    if i+k < len(cards):
                        # n_copies
                        cards[i+k][2] += 1
        
        # print(card[2])
        scratchcards += card[2]
    
    print(f'\nscratchcards: {scratchcards}')
