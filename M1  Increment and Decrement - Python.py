#User function Template for python3

# Function to perform increment and decrement
def do_operation(X, Y):
    # Your code here
    X-=1
    Y+=1
    print (X)
    print (Y)

#{ 
#Driver Code Starts.


# Driver code
def main():
    testcase = int(input())
    
    while(testcase > 0):
        input1 = input().split()
        X = int(input1[0])
        Y = int(input1[1])
        do_operation(X, Y)
        testcase -= 1
        
