from urllib.request import urlopen
for line in urlopen('https://www.baidu.com'):
    line = line.decode('utf-8')  # Decoding the binary data to text.
    print(line)
