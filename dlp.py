import os
import hashlib

p = 31050371851708889440695779044384182719244728783
target = 13821904325547285207847180361637528630753679004
order = 11706593258111142827  # ell afterwards

file = open("./no.txt", "r", encoding='utf-8')
no = file.read()
no = no.strip('\n')
file.close()
hash_no = int(hashlib.sha256(no.encode('utf-8')).hexdigest(), 16)
g = pow(hash_no, 2652383248234496409305378666, p)

stdout_redir = './out.txt'
stderr_redir = './err.txt'

os.system(
    f"python ./cado-nfs/cado-nfs.py -t all -dlp -ell {order} target={target},{g} {p} > {stdout_redir} 2> {stderr_redir}")

file = open('./out.txt', "r", encoding='utf-8')
temp = file.read().split(',')
log_h, log_g = int(temp[0]), int(temp[1])
file.close()

result = log_h * pow(log_g, -1, order) % order

test = pow(g, result, p)

if test != target:
    print("something wrong")
else:
    print(result)

file = open('./ret.txt', "w", encoding='utf-8')
file.write(str(g))
file.write('\n')
file.write(str(result))
file.close()
