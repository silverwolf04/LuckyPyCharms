import getopt, getpass, sys, os

# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def list_help():
    print('test.py -i <inputfile> -o <outputfile> -e <extracmd>')
    print('Options can also be passed as environment variables using the variable names in the <> above')


def arg_check(argv):
    try:
        opts, args = getopt.getopt(argv, "hi:o:e:",["ifile=","ofile=","excmd="])
        # global variable scope - https://www.w3schools.com/python/python_variables_global.asp
        global inputfile, outputfile, extracmd
    except getopt.GetoptError:
        print('Format the arguments as follows:')
        list_help()
        sys.exit(1)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            list_help()
            exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-e", "--extracmd"):
            extracmd = arg


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi(getpass.getuser())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Environment variables
# https://www.nylas.com/blog/making-use-of-environment-variables-in-python/
inputfile = os.getenv('inputfile')
outputfile = os.getenv('outputfile')
extracmd = os.getenv('extracmd')
arg_check(sys.argv[1:])

# Check if variable is None aka 'null'
# https://pytutorial.com/check-if-variable-is-not-null-in-python
print("Input file is " + str(inputfile).replace('None',''))
print("Output file is " + str(outputfile).replace('None',''))
print("Extra command is " + str(extracmd).replace('None',''))
