def distance(strand_a, strand_b):
    ham_dist = 0
    length = max(len(strand_a), len(strand_b))
    for i in range(length):
        try:
            if strand_a[i] != strand_b[i]:
                ham_dist += 1
        except:
            raise ValueError("Invalid lengths. Must be the same.")
    return ham_dist