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
    output('gpg.py --action=list')
    output('gpg.py --action=import --inputfile=publickey')
    output('gpg.py --action=encrypt --recipient=RecipientNameInKeyRing --inputfile=file --outputfile=file')
    output('NOTE: for encrypt --outputfile is optional; will append .pgp to --inputfile name if left blank)')


def arg_check(argv):
    try:
        opts, args = getopt.getopt(argv, "hr:a:i:m:",["recipient=","action=","inputfile=","outputfile="])
        global recipient, action, input_file, output_file
    except getopt.GetoptError:
        list_help()
        sys.exit(1)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            list_help()
            exit()
        elif opt in ("-r", "--recipient"):
            age = arg
        elif opt in ("-a", "--action"):
            action = arg
        elif opt in ("-i", "--inputfile"):
            input_file = arg
        elif opt in ("-o", "--outputfile"):
            output_file = arg


def execute_action(act):
    if act == 'list':
        output('Running ''list'' action')
        try:
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
        except Exception:
            return 1
    elif act == 'import':
        try:
            # import a key and set ultimate trust level
            import_key_file = input_file
            key_data = open(import_key_file).read()
            import_result = gpg.import_keys(key_data)
            output('Importing key with fingerprint:' + str(import_result.fingerprints))
            gpg.trust_keys(import_result.fingerprints, 'TRUST_ULTIMATE')
            my_key = gpg.list_keys()
            output('Fingerprints found in GPG keyring')
            for entry in my_key:
                output('******************')
                for key, value in entry.items():
                    if key == 'fingerprint':
                        output(value)
            return 0
        except Exception:
            output('An error occurred')
            return 1
    elif act == 'encrypt':
        try:
            output('encrypt file')
            # encrypt the file
            if output_file is None:
                o_file = input_file + '.pgp'
            else:
                o_file = output_file
            with open(input_file, 'rb') as f:
                status = gpg.encrypt_file(f, recipients=['PKP_Integrations_Mines1'], output=o_file)

            print(status.ok)
            print(status.stderr)
            return 0
        except Exception:
            output('An error occurred')
            return 1
    else:
        output('Unknown action specified')
        list_help()
        return 1


recipient = None
action = None
input_file = None
output_file = None
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

ret = execute_action(action)

output('Return Code:' + str(ret))
sys.exit(ret)

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