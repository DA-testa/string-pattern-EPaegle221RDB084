# python3

def read_input():
    input_type = input()

    if input_type == "F":
        file_name = "tests/06"
        with open(file_name) as f:
            text = f.readlines()
            T = text[0].strip()
            P = text[1].strip()
    elif  "I" in input_type:
        T = input().strip()
        P = input().strip()
    else:
        print("Invalid input type.")
        return
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (P, T)

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(P, T):
    d = 256
    q = 1000
    M = len(P)
    N = len(T)
    h = 1
    for i in range(M-1):
        h = (h*d) % q
    p = 0
    t = 0
    i = 0
    for i in range(M):
        p = (d*p + ord(P[i]))%q
        t = (d*t + ord(T[i]))%q
    j = 0
    index = []
    for i in range(N-M+1):
        if p == t:
            for j in range (M):
                if T[i+j] != P[j]:
                    break
            else:
                j += 1
            if j == M:
                index.append(i)
        if i<N-M : 
            t = (d*(t-ord(T[i])*h) + ord(T[i+M])) % q
            if t < 0:
                t = t+q
    # this function should find the occurances using Rabin Karp alghoritm 

    # and return an iterable variable
    return index


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

