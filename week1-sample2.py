import random

def orderIceCream(flavors, toppings, sizes):
    f = int(random.randint(0,len(flavors)-1))
    t = int(random.randint(0,len(toppings)-1))
    s = int(random.randint(0,len(sizes)-1))
    return f, t, s

icecream = {
	"flavors": ["vanilla", "chocolate", "strawberry"],
	"toppings": ["sprinkles", "hot fudge", "peanuts"],
	"sizes": ["small", "medium", "large"]
}

print(type(icecream))
print(icecream.keys())
print(icecream["flavors"])

for flavor in icecream["flavors"]:
    print(flavor)

for key in icecream:
    print( key)
    for item in icecream[key]:
        print(item, " ", end = '')
    print("\n")

icecream["flavors"].append("cookie dough")
print(icecream["flavors"])

optionsList = []
for key in icecream:
    for item in icecream[key]:
        optionsList.append(item)
print(optionsList)

order = orderIceCream(icecream["flavors"], icecream["toppings"], icecream["sizes"])
print("I would like a", icecream["flavors"][order[0]], icecream["toppings"][order[1]], icecream["sizes"][order[2]])

