str1 = list("AACC")

def shouldSwap(string, start, curr):
    for i in range(start, curr):
        if string[i] == string[curr]:
            return False
    return True

def permute(string, left, right):
    if left == right:
        print(''.join(string))
        return

    count = set()
    for i in range(left, right+1):
        #if not shouldSwap(string, left, i):
            #continue
        if string[i] in count:
            continue

        string[left], string[i] = string[i], string[left]
        permute(string, left+1, right)
        string[left], string[i] = string[i], string[left]

        count.add(string[i])

permute(str1, 0, len(str1)-1)

#Time O(N*N!)
