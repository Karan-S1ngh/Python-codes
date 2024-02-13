# You are given three integers x, y and z representing the dimensions of a cuboid along with an integer n.
# You have to print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of i+j+k is not equal to n. 
# Here, 0 <= i <= x; 0 <= j <= y; 0 <= k <= z


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
l = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]
x = [a for a in l if sum(a)!= n]
print(x)




'''OUTPUT
1
1
1
2
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]


2
2
2
2
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0],
[1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]
'''
