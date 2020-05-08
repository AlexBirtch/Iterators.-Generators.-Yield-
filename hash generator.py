import hashlib

def HashGenerator(path):
    with open(path, encoding='utf-8') as file:
        for line in file:
            yield hashlib.md5(line.encode('utf-8')).hexdigest()
            yield hashlib.sha512(line.encode('utf-8')).hexdigest()
            yield hashlib.shake_256(line.encode('utf-8')).hexdigest(100)
for hash in HashGenerator('result.txt'):
    print(hash)