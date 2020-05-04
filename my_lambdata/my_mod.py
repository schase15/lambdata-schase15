def enlarge(n):
    return int(n) * 100

if __name__ == "__main__":
    # only run the following code
    # when we run this script from the command-line
    # otherwise don't invoke this code (for example when importing from another file)

    x=5
    print(enlarge(x))

    z= input('Please choose a number to enlarge:')
    print(enlarge(int(z)))