import sys
from pprint import pprint

def main(f_name):
    map = []
    robot_pos = [0,0]
    
    def _move_robot(row, col):
        map[robot_pos[0]] [robot_pos[1]] = '.'
        robot_pos[0] = row
        robot_pos[1] = col
        map[row][col] = '@'
        
    def _read_map(line, i):
        map.append([])
        for j, letter in enumerate(line.strip()):
            map[i].append(letter)
            
            if letter == '@':
                robot_pos[0] = i
                robot_pos[1] = j
    
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
                            else:
                                print('Not valid piece')
                                break
                    
                    elif direction == '>':
                        row = robot_pos[0]
                        col = robot_pos[1] + 1
                        
                        if map[row][col] == '#': 
                            continue
                        elif map[row][col] == '.':
                            _move_robot()
                        
                        elif map[row][col] == 'O':
                            if map[row][col+1] == '#':
                                continue
                            elif map[row][col+1] == '.':
                                _move_robot(row, col)
                                map[row][col+1] = 'O'
                            # elif map[row][col+1] == 'O':
                            else:
                                print('Not valid piece')
                                break
                                
                    
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
                            else:
                                print('Not valid piece')
                                break
                
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
                            # elif map[row+1][col] == 'O':
                            else:
                                print('Not valid piece')
                                break
                    
                    else:
                        print('Not a valid direction')
                        break

f_name = sys.argv[1]
main(f_name)