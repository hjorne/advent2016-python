from hashlib import md5

""" Part 1 """
base = 'ojvtpuvg'
password = ''
index = 0

while len(password) < 8:
    md5_hash = md5(base + str(index)).hexdigest()
    if md5_hash[0:5] == '00000':
        password += md5_hash[5]
    index += 1
print 'Password to the first door is {0}'.format(password)


""" Part 2 """
password = [None] * 8
index = 0
pos = 0

# Loop until all elements in password are not None
while not all(password):
    md5_hash = md5(base + str(index)).hexdigest()
    if md5_hash[0:5] == '00000':
        if md5_hash[5].isdigit():
            pos = int(md5_hash[5])
            # Make sure not to overwrite a previous position in password
            if pos < 8 and not password[pos]:
                password[pos] = md5_hash[6]
    index += 1
print 'Password to the second door is {0}'.format(''.join(password))
