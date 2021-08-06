dict_a = {}
print(dict_a)

dict_a["name"] = "구름"
print(dict_a)

del dict_a["name"]
print(dict_a)

pets = [
    {"name" : "구름", "age" : 5},
    {"name" : "초코", "age" : 3},
    {"name" : "아지", "age" : 1},
    {"name" : "호랑이", "age" : 1}
]

for pet in pets:
    print("{} : {}".format(pet["name"], pet["age"]))


numbers = [1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,1,2,3]
counter = {}

# 방법 1 : if 문 사용
for number in numbers:
    if number in counter:
        counter[number] += 1
    else:
        counter[number] = 1
print(counter)

# 방법 2 : dict.get() method 사용
counter = {}
for number in numbers:
    counter[number] = counter.get(number, 0) + 1
print(counter)


character = {
    "name" : "기사",
    "level" : 12,
    "items" : {
        "sword" : "검",
        "armor" : "갑옷"
    },
    "skill" : ["베기", "베기2", "베기3"]
}

for key in character:
    value = character[key]
    if type(value) is dict:
        for k in value:
            print("{} : {}".format(k, value[k]))
    elif type(value) is list:
        for v in value:
            print("{} : {}".format(key, v))
    else:
        print("{} : {}".format(key, value))