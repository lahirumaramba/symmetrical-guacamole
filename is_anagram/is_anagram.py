
def is_anagram(str1, str2):
    if not str1 or not str2:
        return False

    if len(str1) != len(str2):
        return False

    str1_count = {}
    str2_count = {}

    for c in str1:
        if c in str1_count:
            str1_count[c] += 1
            continue

        str1_count[c] = 1

    for c in str2:
        if c not in str1_count:
            return False

        if c in str2_count:
            str2_count[c] += 1
            continue

        str2_count[c] = 1

    return str1_count == str2_count

"""    for c in str1:
        if str1_count[c] != str2_count[c]:
            return False"""

print(is_anagram("hello", "loohe"))
