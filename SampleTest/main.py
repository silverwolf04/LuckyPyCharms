import getopt
import getpass
import sys

# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def arg_check(argv):
    try:
        opts, args = getopt.getopt(argv, "hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(1)
    for opt, arg in opts:
        print('Option: ' + opt)
        print('Argument: ' + arg)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi(getpass.getuser())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

arg_check(sys.argv[1:])

