list = [10,15,7,255,13,103,100015]
var = 0
maxNum = 0
for i in list:
    var = i
    if maxNum < var:
        maxNum = var

print(maxNum)