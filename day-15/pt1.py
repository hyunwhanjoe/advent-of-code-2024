import sys
from pprint import pprint

'''
if direction:
    if wall next: continue
    elif empty next: move robot
    elif box next:
        if wall next: continue
        elif empty next: move robot & box
        elif box next:
            if wall at end: continue:
            get index of next empty space
            move robot
            move box to index
'''

def draw_map(f_name):
    map = []
    robot_pos = [0,0]
    
    def _read_map(line, i):
        map.append([])
        
        for j, letter in enumerate(line.strip()):
            if letter == '#' or letter == '@' or letter == '.' or letter == 'O':
                map[i].append(letter)
                
                if letter == '@':
                    robot_pos[0] = i
                    robot_pos[1] = j
            else:
                print('invalid letter')
                breakpoint()
        
    def _move_robot(row, col):
        map[robot_pos[0]] [robot_pos[1]] = '.'
        robot_pos[0] = row
        robot_pos[1] = col
        map[row][col] = '@'
        
    def _check_wall(direction, row, col):
        k = 1
        
        if direction == '>':
            while map[row][col+k] == 'O':
                k += 1
                if map[row][col+k] == '#':
                    return True
                    
        elif direction == '<':
            while map[row][col-k] == 'O':
                k += 1
                if map[row][col-k] == '#':
                    return True
        
        elif direction == 'v':
            while map[row+k][col] == 'O':
                k += 1
                if map[row+k][col] == '#':
                    return True
        
        elif direction == '^':
            while map[row-k][col] == 'O':
                k += 1
                if map[row-k][col] == '#':
                    return True
        
        return False
        
    def get_next_index(direction, row, col):
        k = 0
        
        if direction == '<':
            while map[row][col-k] != '.':
                k+= 1
            return k
        
        elif direction == '>':
            while map[row][col+k] != '.':
                k+= 1
            return k
            
        elif direction == '^':
            while map[row-k][col] != '.':
                k+= 1
            return k
        elif direction == 'v':
            while map[row+k][col] != '.':
                k+= 1
            return k
    
    with open(f_name, "r") as f:
        for i, line in enumerate(f):
            if line.startswith('#'):
                _read_map(line, i)
            
            elif line != '\n':
                for direction in line.strip():
                    # print(direction)
                    # pprint(map)
                    # breakpoint()
                    
                    if direction == '<':
                        row = robot_pos[0]
                        col = robot_pos[1] - 1
                        
                        if map[row][col] == '#': 
                            continue
                        elif map[row][col] == '.':
                            _move_robot(row, col)
                        
                        elif map[row][col] == 'O':
                            if map[row][col-1] == '#':
                                continue
                            elif map[row][col-1] == '.':
                                _move_robot(row, col)
                                map[row][col-1] = 'O'
                            elif map[row][col-1] == 'O':
                                if _check_wall(direction, row, col):
                                    continue
                                else:
                                    k = get_next_index(direction, row, col)
                                    _move_robot(row, col)
                                    map[row][col-k] = 'O'
                    
                    elif direction == '>':
                        row = robot_pos[0]
                        col = robot_pos[1] + 1
                        
                        if map[row][col] == '#': 
                            continue
                        elif map[row][col] == '.':
                            _move_robot(row, col)
                        
                        elif map[row][col] == 'O':
                            if map[row][col+1] == '#':
                                continue
                            elif map[row][col+1] == '.':
                                _move_robot(row, col)
                                map[row][col+1] = 'O'
                            
                            elif map[row][col+1] == 'O':
                                if _check_wall(direction, row, col):
                                    continue
                                else:
                                    k = get_next_index(direction, row, col)
                                    _move_robot(row, col)
                                    map[row][col+k] = 'O'
                    
                    elif direction == '^':
                        row = robot_pos[0] - 1
                        col = robot_pos[1]
                        
                        if map[row][col] == '#': 
                            continue
                        elif map[row][col] == '.':
                            _move_robot(row, col)
                        
                        elif map[row][col] == 'O':
                            if map[row-1][col] == '#':
                                continue
                            elif map[row-1][col] == '.':
                                _move_robot(row, col)
                                map[row-1][col] = 'O'
                            elif map[row-1][col] == 'O':
                                if _check_wall(direction, row, col):
                                    continue
                                else:
                                    k = get_next_index(direction, row, col)
                                    _move_robot(row, col)
                                    map[row-k][col] = 'O'
                
                    elif direction == 'v':
                        row = robot_pos[0] + 1
                        col = robot_pos[1]
                        
                        if map[row][col] == '#': # '.'
                            continue
                        elif map[row][col] == '.':
                            _move_robot(row, col)
                        
                        elif map[row][col] == 'O':
                            if map[row+1][col] == '#':
                                continue
                            elif map[row+1][col] == '.':
                                _move_robot(row, col)
                                map[row+1][col] = 'O'
                            elif map[row+1][col] == 'O':
                                if _check_wall(direction, row, col):
                                    continue
                                else:
                                    k = get_next_index(direction, row, col)
                                    _move_robot(row, col)
                                    map[row+k][col] = 'O'

                    
                    else:
                        print('Not a valid direction')
                        break
    
    return map
    
def sum_gps(map):
    sum = 0
    
    for i in range(len(map)):
        for j in range(len(map)):
            if map[i][j] == 'O':
                sum += 100 * i + j
    
    return sum


f_name = sys.argv[1]
map = draw_map(f_name)
sum = sum_gps(map)


if f_name == 'day-15/smaller.txt':
    assert sum == 2028
elif f_name == 'day-15/larger.txt':
    assert sum == 10092
elif f_name == 'day-15/input.txt':
    assert sum == 1_426_855