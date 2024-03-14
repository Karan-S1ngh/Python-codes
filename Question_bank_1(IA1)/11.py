data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
def fun(m):
    v = m [0][0]
    for row in m:
        for element in row:
            print(row)
            print(element)
            if v < element:
                v = element
    return v
print (fun (data [0]))



'''OUTPUT
[1, 2]
1
[1, 2]
2
[3, 4]
3
[3, 4]
4
4
'''
