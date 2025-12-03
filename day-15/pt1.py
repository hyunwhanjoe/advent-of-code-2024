import sys
from pprint import pprint

def main(f_name):
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
        
        elif direction == 'v':
            while map[row+k][col] == 'O':
                k += 1
                if map[row+k][col] == '#':
                    return True
        
        return False
    
    with open(f_name, "r") as f:
        for i, line in enumerate(f):
            if line.startswith('#'):
                _read_map(line, i)
            
            elif line != '\n':
                for direction in line.strip():
                    print(direction)
                    pprint(map)
                    breakpoint()
                    
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
                            # elif map[row][col-1] == 'O':
                    
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
                                    k = 0
                                    while map[row][col+k] != '.':
                                        k+= 1
                                    
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
                            # elif map[row-1][col] == 'O':
                
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
                                    k = 0
                                    while map[row+k][col] != '.':
                                        k+= 1
                                    
                                    _move_robot(row, col)
                                    map[row+k][col] = 'O'

                    
                    else:
                        print('Not a valid direction')
                        break

f_name = sys.argv[1]
main(f_name)