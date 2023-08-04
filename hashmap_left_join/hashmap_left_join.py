def left_join(hashmap1, hashmap2):
    result = []
    for key, value in hashmap1.items():
        if key in hashmap2:
            result.append([key, value, hashmap2[key]])
        else:
            result.append([key, value, None])
    return result