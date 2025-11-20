from tqdm import tqdm

# input = 'sample.txt'
input = 'input.txt'

# Took 22 seconds to run, need to optimize
with open(input, "r") as f:
    scratchcards = 0
    cards = []
    
    lines = f.readlines()
    for line in lines:
        line = line.split('|')
        winning_nums = line[0].split(':')
        winning_nums = winning_nums[1].split()
        
        nums = line[1].split()
        
        cards.append([winning_nums, [nums]])
    # breakpoint()
    
    for i, card in enumerate( tqdm(cards)):
        winning_nums = set(card[0])
        for j in range( len(card[1])):
            nums = set( card[1][j])
            n_matches = len(winning_nums & nums)
            
            if n_matches >= 1:
                for k in range(1, n_matches+1):
                    if i+k < len(cards):
                        next_card = cards[i+k]
                        nums = next_card[1][0]
                        next_card[1].append(nums)
        
        # print(len(card[1]))
        scratchcards += len(card[1])
    
    print(f'\nscratchcards: {scratchcards}')
    breakpoint()
