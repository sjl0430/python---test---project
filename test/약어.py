def find_interesting_abbreviation(s, t):
    # S의 접두사와 T의 접미사 찾기
    prefixes = set()
    suffixes = set()
    n, m = len(s), len(t)

    for i in range(1, n + 1):
        prefixes.add(s[:i])

    for j in range(m):
        suffixes.add(t[j:])

    return prefixes, suffixes

def count_valid_pairs(prefixes, suffixes):
    valid_pairs = []

    for prefix in prefixes:
        for suffix in suffixes:
            if prefix and suffix and prefix[-1] == suffix[0]:
                valid_pairs.append((prefix, suffix))
                if len(valid_pairs) >= 2:
                    return valid_pairs
    return valid_pairs

def construct_abbreviation(valid_pairs):
    abbreviations = set()
    for prefix, suffix in valid_pairs:
        abbreviations.add(prefix + suffix[1:])

    if abbreviations:
        return min(abbreviations, key=len)
    return -1

def solve(s, t):
    prefixes, suffixes = find_interesting_abbreviation(s, t)
    valid_pairs = count_valid_pairs(prefixes, suffixes)
    return construct_abbreviation(valid_pairs)

# 사용 예시
print(solve("sarana", "olahraga"))
print(solve("berhiber","wortelhijau"))
print(solve("icpc", "icpc"))
print(solve("icpc", "olahraga"))

# 수정이 필요함