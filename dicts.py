# I am some dictionaries
ages = { 'Kevin' : 59, 'alex': 29, 'bob': 40}
ages
print (ages)

name = "Kevin"
if len(name) >= 6:
     print("name is long")
elif len(name) == 5:
     print("name is 5 characters")
elif len(name) >= 4:
# will stop above becuase its true
    print("name is 4 or more")
else:
    print("name is short")

print("Stop below with ctrl+c")
count = 1
while count <= 4:
    print("looping")
    count += 1

countb = 0
while countb < 10:
     if countb % 2 == 0:
         countb += 1
         continue
     print(f"We're counting odd numbers: {countb}")
     countb += 1

initial = 0
while initial < 100:
    if initial % 2 == 0:
        initial += 1
        continue
    elif initial > 90:
        print("Hey, I hit 90 before reaching 100, I'll stop here")
        break
    else:
        print(f"Let's do a lot of numbers like this: {initial}")
    initial += 1

# comb = 1
# while comb <= 1000:
#    print({comb})
#    comb += 1
#    if comb > 900:
#        print("Wow, I'm tired")
#        break
#    else:
#        print(f"Boom: {comb}")
#    comb += 1
