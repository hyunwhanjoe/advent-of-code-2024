import sys
from pprint import pprint

robot_pos = [0,0]

def read_map(f_name):
    map = []
    with open(f_name, "r") as f:
        for i, line in enumerate(f):
            if line.startswith('#'):
                map.append([])
                for j, letter in enumerate(line.strip()):
                    if letter == '@':
                        robot_pos[0] = i
                        robot_pos[1] = j
                    
                    map[i].append(letter)
            
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
                    
                    elif direction == '^':
                        row = robot_pos[0] - 1
                        col = robot_pos[1]
                        
                        if map[row][col] == '#': 
                            continue
                        elif map[row][col] == '.':
                            map[robot_pos[0]] [robot_pos[1]] = '.'
                            robot_pos[0] = row
                            robot_pos[1] = col
                            map[row][col] = '@'
                        # elif map[row][col] == 'O':
                    
                    elif direction == '>':
                        row = robot_pos[0]
                        col = robot_pos[1] + 1
                        
                        if map[row][col] == '#': 
                            continue
                        elif map[row][col] == 'O':
                            if map[row][col+1] == '.':
                                map[robot_pos[0]] [robot_pos[1]] = '.'
                                robot_pos[0] = row
                                robot_pos[1] = col
                                map[row][col] = '@'
                                map[row][col+1] = 'O'
                            
                            elif map[row][col+1] == 'O':
                                if map[row][col+2] == '.':
                                    map[robot_pos[0]] [robot_pos[1]] = '.'
                                    robot_pos[0] = row
                                    robot_pos[1] = col
                                    map[row][col] = '@'
                                    map[row][col+2] = 'O'
                        # elif map[row][col] == '.':
                    
                    elif direction == 'v':
                        row = robot_pos[0] - 1
                        col = robot_pos[1]
                        
                        if map[row][col] == '#': # '.'
                            continue
                        elif map[row][col] == 'O':
                            
    
    return map

f_name = sys.argv[1]
map = read_map(f_name)