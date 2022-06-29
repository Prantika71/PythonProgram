#global scope

#outer value
p= "Ami"

def hudai():

    global p

    # inner value
    #eta global er under a inner value outer value k overlap kore fele.
    p= 90
    print(p)
hudai()

print(p)

# global keyword use na krle error.. globaly handle hbe na