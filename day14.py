import re
from hashlib import md5


def get_md5(index):
    """ Takes care of md5 hash caching for speedups """
    if index > len(md5s) - 1:
        for i in range(len(md5s), index + 1):
            md5_hash = md5(salt + str(i)).hexdigest()
            # Uncomment for part 2
            # for j in range(2016):
            #     md5_hash = md5(md5_hash).hexdigest()
            md5s.append(md5_hash)
    return md5s[index]


salt = 'yjdafjpo'
index = 0
count = 0
md5s = []

while count < 64:
    md5_hash = get_md5(index)
    # Looks for anything of the form xxx
    m = re.search(r'(.)\1{2}', md5_hash)
    if m:
        c = m.group()[0]
        for i in range(1, 1001):
            md5_hash = get_md5(index + i)
            # Looks for the same x as above exactly 5 times (xxxxx)
            m = re.search(c + r'{5}', md5_hash)
            if m:
                count += 1
                print count, index
                break
    index += 1
print index - 1
