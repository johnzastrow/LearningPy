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
