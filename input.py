import hashlib
import sys
import os
import subprocess

p = 31050371851708889440695779044384182719244728783
target = 13821904325547285207847180361637528630753679004
order = 11706593258111142827
log_h = 1886633431377697014  # precalculate

if len(sys.argv) != 2:
    print('Not exactly one argv\nProgram Exit')
    exit(-1)  # With Error
else:
    stu_no = str(sys.argv[1])

hash_stu_no = int(hashlib.sha256(stu_no.encode('utf-8')).hexdigest(), 16)
g = pow(hash_stu_no, 2652383248234496409305378666, p)

string = "python ./cado-nfs/cado-nfs.py" + \
    f" -t all -dlp -ell {order} target={g} {p}"

process = subprocess.run(
    string, shell=True, capture_output=True, encoding='utf-8')

log_g = int(process.stdout)

result = log_h * pow(log_g, -1, order) % order

test = pow(g, result, p)

if test != target:
    print("something wrong")
else:
    print(result)

with open('./ret.txt', "w", encoding='utf-8') as f:
    f.write(str(g))
    f.write('\n')
    f.write(str(result))
