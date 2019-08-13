# Exercise 6:

x=int(input("Enter a number : "))

def show_stars(rows):
    n=0
    for row in range(rows):
        n += 1
        print(n * "*")

show_stars(x)