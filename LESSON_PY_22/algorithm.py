def distance_2(text, pattern):
   "Calculates the Levenshtein distance between text and pattern."
   text_len, pattern_len = len(text), len(pattern)

   current_column = range(pattern_len+1)
   min_value = pattern_len
   end_pos = 0
   for i in range(1, text_len+1):
      previous_column, current_column = current_column, [0]*(pattern_len+1) # !!!
      for j in range(1,pattern_len+1):
         add, delete, change = previous_column[j]+1, current_column[j-1]+1, previous_column[j-1]
         if pattern[j-1] != text[i-1]:
            change += 1
         current_column[j] = min(add, delete, change)

      if min_value > current_column[pattern_len]: # !!!
         min_value = current_column[pattern_len]
         end_pos = i

   return min_value, end_pos

print (distance_2(u'аргумент', u'рудимент')) #3, 8
print (distance_2(u' в мою пользу', u'рудимент')) #3, 16

#JUMP SEARCH

import math
def JumpSearch (lys, val):
    length = len(lys)
    jump = int(math.sqrt(length))
    left, right = 0, 0
    while left < length and lys[left] <= val:
        right = min(length - 1, left + jump)
        if lys[left] <= val and lys[right] >= val:
            break
        left += jump;
    if left >= length or lys[left] > val:
        return -1
    right = min(length - 1, right)
    i = left
    while i <= right and lys[i] <= val:
        if lys[i] == val:
            return i
        i += 1
    return -1
print(JumpSearch([1,2,3,4,5,6,7,8,9], 5))

#ИНТЕРПОЛЯЦИОННЫЙ ПОИСК

def InterpolationSearch(lys, val):
    low = 0
    high = (len(lys) - 1)
    while low <= high and val >= lys[low] and val <= lys[high]:
        index = low + int(((float(high - low) / ( lys[high] - lys[low])) * ( val - lys[low])))
        if lys[index] == val:
            return index
        if lys[index] < val:
            low = index + 1;
        else:
            high = index - 1;
    return -1
print(InterpolationSearch([1,2,3,4,5,6,7,8], 6))

#ЭКСПОНЕНЦИАЛЬНЫЙ ПОИСК

def ExponentialSearch(lys, val):
    if lys[0] == val:
        return 0
    index = 1
    while index < len(lys) and lys[index] <= val:
        index = index * 2
    return ExponentialSearch( lys[:min(index, len(lys))], val)

print(ExponentialSearch([1,2,3,4,5,6,7,8],3))


