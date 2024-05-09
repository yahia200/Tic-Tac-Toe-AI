def most_frequent(list):
    return max(set(list), key = list.count)


prio=[2,2,3,3,4,5]

print(most_frequent(prio))