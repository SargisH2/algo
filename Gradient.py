#Gradient deccent
def f(x):#function(x), 2x^2+3x-1
    return 2*x**2 + 3*x - 1

def d(x): #derivative(x), 4x+3
    return 4*x + 3

def g(n, l=0.1, x0=0):#gradient(count, lambda, first x)
    for _ in range(int(n)):
        x0= x0 - l*d(x0)
    return x0

steps=int(input("Steps: "))
print(f"In this example (lambda=0.1, x0=0, steps={steps})\nXmin is {g(steps)},\nFmin is {f(g(steps))}")