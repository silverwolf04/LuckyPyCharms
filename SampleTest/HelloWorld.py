import getopt, sys, os

file = os.environ.get('file')


def output(param):
    if file is None:
        print(param)
    else:
        with open(file, 'w') as f:
            print(param, file=f)


def list_help():
    print('test.py -u <user> -a <age> -f <fullname> -m <message>')


def arg_check(argv):
    try:
        opts, args = getopt.getopt(argv, "hu:a:f:m:",["user=","age=","fullname=","message="])
        global user, age, fullname, message
    except getopt.GetoptError:
        list_help()
        sys.exit(1)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            list_help()
            exit()
        elif opt in ("-u", "--user"):
            user = arg
        elif opt in ("-a", "--age"):
            age = arg
        elif opt in ("-f", "--fullname"):
            fullname = arg
        elif opt in ("-m", "--message"):
            message = arg


user = None
age = None
fullname = None
message = None
arg_check(sys.argv[1:])
err = 0

if user is None:
    try:
        output(sys.argv[2])
    except IndexError:
        print('user is undefined')
        err = 1
else:
    output(user)

if age is None:
    try:
        output(sys.argv[3])
    except IndexError:
        print('age is undefined')
        err = 1
else:
    output(age)

if fullname is None:
    try:
        output(sys.argv[4])
    except IndexError:
        print('fullname is undefined')
        err = 1
else:
    output(fullname)

if message is None:
    try:
        output(sys.argv[5])
    except IndexError:
        print('message is undefined')
        err = 1
else:
    output(message)

sys.exit(err)
