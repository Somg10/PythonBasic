# Function to print given string 'x' times
def print_fun(string, x):
    # Your code here
    print(string*x)

#{ 
#Driver Code Starts.

# Driver Code
def main():
    testcases = int(input())
    
    # Loop for testcases
    while(testcases > 0):
        string = input()
        x = int(input())
        print_fun(string, x)
        testcases -= 1

if __name__ == '__main__':
    main()
    
#} Driver Code Ends
