# Python_scripts
Variety of scripts made in Python that may solve problems that require a huge time of work

## About

Sometimes we need to automate some process or iterate things, python will help us.

### Json hashes --> hashcat format

When you have an array of Hashes and users, if we want to decrypt the code we should convert it to Hashcat format.

```
f = open('hash.txt','r')
o = open('formatted_hashes.txt','w')
l = f.read().strip().split(',')
for i in l:
  o.write(i.split(':')[1][2:-1] + '\n') 
f.close()
o.close()

```

### Tiny PTY shell

How to load a pty shell, useful to reverse conexions.

```
python -c 'import pty; pty.spawn("/bin/sh")'
```
