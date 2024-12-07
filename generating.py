def all_variants(text):
    n = len(text)
    for i in range(1 << n):
        subsequence = []
        for j in range(n):
            if i & (1 << j):
                subsequence.append(text[j])
        yield ''.join(subsequence)

a = all_variants("abc")
for i in a:
    print(i)
