import os

def read_file(prob_num):
    os.chdir('/home/Documents/PersonalProjects/adventofcode/2021') # Moves the current working directory here
    file = open(f'input_problem%s.txt' % prob_num, 'r')
    return file.readlines()

