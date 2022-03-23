import gnupg, getopt, sys, os

# OpenPGP => GnuPG => PGP
# All the same thing, just licensed differently and maintained by different groups

file = os.environ.get('file')


def output(param):
    if file is None:
        print(param)
    else:
        with open(file, 'a') as f:
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
        elif opt in ("-a", "--action"):
            user = arg
        elif opt in ("-x", "--xage"):
            age = arg
        elif opt in ("-f", "--fullname"):
            fullname = arg
        elif opt in ("-m", "--message"):
            message = arg


action = None
age = None
fullname = None
message = None
arg_check(sys.argv[1:])
err = 0

if action is None:
    try:
        output('Action:' + sys.argv[1])
    except IndexError:
        print('action is undefined')
        err = 1
else:
    output('User: ' + user)

exit(err)

gpg=gnupg.GPG(verbose=False)
gpg = gnupg.GPG()
gpg.encoding = 'utf-8'
gpg.list_keys()

"""
# create a signature key

gpg.encoding = 'utf-8'
input_data = gpg.gen_key_input(
    name_email = 'dcover@mines.edu',
    passphrase = 'test123',
    key_type = 'RSA',
    key_length = 4096
)

key = gpg.gen_key(input_data)
print(key)
"""

"""
# import a key and set ultimate trust level
import_key_file = "C:/pvm-gitccit/workday/9Workday/GPG/MinesWorkday_0x32F8E37C_SECRET.asc"
# import_key_file = "C:/pvm-gitccit/workday/9Workday/GPG/MinesWorkday_0x32F8E37C_public.asc"
# import_key_file = 'c:/users/dcover/downloads/misc/pgp_public_mines1.pub'
key_data = open(import_key_file).read()
import_result = gpg.import_keys(key_data)
gpg.trust_keys(import_result.fingerprints, 'TRUST_ULTIMATE')
mykeys = gpg.list_keys()
print(mykeys)
"""

"""
# encrypt the file
path = 'c:/users/dcover/downloads/misc/'
enc_file = "test"
with open(path + test, 'rb') as f:
    status = gpg.encrypt_file(f, recipients = ['PKP_Integrations_Mines1'], output = path + test + '.pgp')

print(status.ok)
print(status.stderr)
"""

# decrypt the file
path = "c:/users/dcover/downloads/misc/"
infile = 'TEST_Workday_Employee_202203161504.csv.pgp'
outfile = infile.rsplit(".", 1)[0]

print('infile: ' + path + infile)
print('outfile: ' + path + outfile)

with open(path + infile, 'rb') as f:
    status = gpg.decrypt_file(f, output = path + outfile)

print(status.ok)
print(status.stderr)