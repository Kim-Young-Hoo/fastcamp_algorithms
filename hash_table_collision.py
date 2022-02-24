"""
hash function에 의해서 중복 key에 자료가 저장되는 경우 해결법
저장 시 linked list 구조에다가 하고 key값을 따로 같이 저장해둔다
"""


hash_table = list([None for i in range(8)])


def hash_func(key):
    return key % 5

def save_data(data, value):

    index_key = hash(data)
    hash_address = hash_func(index_key)

    if hash_table[hash_address]:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                hash_table[hash_address][index][1] = value
                return
    else:
        hash_table[hash_address].append([index_key, value])



