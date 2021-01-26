result = [x.split(' ') for x in input().split('|')[::-1]]
flat_list = [item for sublist in result for item in sublist if item != '']
print(' '.join(flat_list))