import sys

def main():
#expect one command line argument, name of file with .py
    check_arg()

    try:
        readfile(sys.argv[1])
    except:
        sys.exit('File Not Found')

def check_arg():
    if len(sys.argv) < 2:
        sys.exit('Too Few Arguments')
    if len(sys.argv) > 2:
        sys.exit('Too Many Arguments')
    if '.py' not in sys.argv[1]:
        sys.exit('Not A Python File')

def readfile(string):
    lines = []
    totallines = 0
    with open(string, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.lstrip(' ').startswith('#') or line.lstrip(' ').startswith('\n') or line == '\n':
                pass
            else:
                totallines += 1

        print(totallines)


#if file does not end in .py or does not exist or there is not exactly 1 command line argument, exit with sys.exit()
#open file
#read total lines inside the file, excluding comments and whitespace
#ouput number of lines


if __name__ == '__main__':
    main()