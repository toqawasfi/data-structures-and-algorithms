def left_join(hashmap1, hashmap2):
    result = []
    for key, synonym in hashmap1.items():
        if key in hashmap2:
            result.append([key, synonym, hashmap2[key]])
        else:
            result.append([key, synonym, None])
    return result
# Example hashmaps
hashmap1 = {'happy': 'joyful', 'sad': 'unhappy', 'fun': 'amusing'}
hashmap2 = {'happy': 'sad', 'fun': 'boring'}

result = left_join(hashmap1, hashmap2)
print(result)
