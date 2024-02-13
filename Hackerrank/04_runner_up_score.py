# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
# You are given n scores. Store them in a list and find the score of the runner-up.


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
l = sorted(set(arr))
# set doesnt has any repetitive elements
print(l[len(l)-2])




'''OUTPUT
5
2 3 6 6 5
5
'''
