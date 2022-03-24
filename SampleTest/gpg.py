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
    print('test.py -u <user> -a <action> -f <fullname> -m <message>')


def arg_check(argv):
    try:
        opts, args = getopt.getopt(argv, "hu:a:f:m:",["user=","action=","fullname=","message="])
        global action, age, fullname, message
    except getopt.GetoptError:
        list_help()
        sys.exit(1)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            list_help()
            exit()
        elif opt in ("-a", "--action"):
            action = arg
        elif opt in ("-x", "--xage"):
            age = arg
        elif opt in ("-f", "--fullname"):
            fullname = arg
        elif opt in ("-m", "--message"):
            message = arg


def execute_action(act):
    if act == 'list':
        output('Running ''list'' action')
        pub_keys = gpg.list_keys()
        i = 0
        while i < len(pub_keys):
            output('********************')
            val = pub_keys[i]['uids']
            output('Recipient: ' + str(val))
            val = pub_keys[i]['trust']
            output('Trust Level: ' + val)
            val = pub_keys[i]['length']
            output('Strength: ' + val)
            val = pub_keys[i]['keyid']
            output('KeyID: ' + val)
            val = pub_keys[i]['fingerprint']
            output('Fingerprint: ' + val)
            i = i + 1
    elif act == '':
        print('test')


action = None
age = None
fullname = None
message = None
arg_check(sys.argv[1:])
err = 0

if action is None:
    try:
        output('Param action:' + sys.argv[1])
    except IndexError:
        output('action is undefined')
        err = 1
else:
    output('Defined action: ' + action)

#exit(err)

gpg=gnupg.GPG(verbose=False)
gpg = gnupg.GPG()
gpg.encoding = 'utf-8'


execute_action(action)

sys.exit(0)

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