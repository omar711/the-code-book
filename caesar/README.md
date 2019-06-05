

Usage examples:

Encrypt some text:

```
cat test.txt | python caesar.py 3 > text-cipher.txt
```

Decrypt:

```
cat text-cipher.txt | python caesar.py -3
```

Message statistics:

```
cat text-cipher.txt | python message_statistics.py
```

Brute force (try all 26 possibilities):

```
cat text-cipher.txt | python caesar_brute.py
```