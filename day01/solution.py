#!/usr/local/bin/python3

import sys

num_list = []

def read_file(inputfile):
    f = open(inputfile,"r")
    for x in f:
        num_list.append(int(x))
    f.close()

def find_goal_sum1(goal):
    ans = 0
    for big in num_list:
        for small in num_list[:0:-1]:
            if big + small == goal:
                print(big,small)
                ans = big * small
                break
        else:
            continue
        break
    print(ans)
    return ans

def find_goal_sum2(goal):
    ans = 0
    for big in num_list:
        for small in num_list[:0:-1]:
            for mid in num_list[-2:0:-1]:
                if big + small + mid == goal:
                    print(big,small,mid)
                    ans = big * small * mid
                    break
            else:
                continue
            break
        else:
            continue
        break
    print(ans)
    return ans

def main():
    # Command line input
    if len(sys.argv) > 2:
        sum_goal = sys.argv[2]
        input_file = sys.argv[1]
    elif len(sys.argv) > 1:
        sum_goal = 2020
        input_file = sys.argv[1]
    else:
        sum_goal = 2020
        input_file = 'inputtest.txt'

    print(input_file,sum_goal)
    read_file(input_file)
    num_list.sort(reverse=True)
    print(num_list)

    #Solve Part 1
    print("Part 1")
    answer1 = find_goal_sum1(sum_goal)
    print("Answer 1:",answer1)

    #Solve Part 2
    print("Part 2")
    answer2 = find_goal_sum2(sum_goal)
    print("Answer 2:",answer2)

if __name__ == '__main__':
    main()
