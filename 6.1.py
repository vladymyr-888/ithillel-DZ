import string
let = 's-U'
start,end = let.split('-')
letters2 = string.ascii_letters
start1 = letters2.index(start)
end1 = letters2.index(end)
result = letters2[letters2.index(start):letters2.index(end) +1]
print(result)