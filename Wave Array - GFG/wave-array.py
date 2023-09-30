from typing import List


class Solution:
    def convertToWave(self, n : int, a : List[int]) -> None:
        arr = [0]*len(a)
        if len(a)%2==0:
            for i in range(1,len(a)+1,2):
                arr[i-1]=a[i]
                arr[i]=a[i-1]
                
        else:
            for i in range(0,len(a)-1,2):
                arr[i+1]=a[i]
                arr[i]=a[i+1]
            arr[-1]=a[-1]
        a.clear()
        a.extend(arr)
       
        return a
       
            
                
                
            
            
        



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        a=IntArray().Input(n)
        
        obj = Solution()
        obj.convertToWave(n, a)
        IntArray().Print(a)

# } Driver Code Ends