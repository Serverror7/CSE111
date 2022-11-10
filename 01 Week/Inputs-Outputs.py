name = input("What is your name? ")
age = int(input("What is your age? "))
if age >= 18:
    if age == 18:
        print(f"Hello {name}! You and I are ths same age!")
    else:
        dif = age - 18
        if dif >= 70:
            print(f"Hello {name}! {age}? That's a lot older than me!")
        else:
            print(f"Hello {name}! {age}? That's {dif} years older than me.")
else:
    dif = 18 - age
    if age <= 0:
        print(f"Hello {name}! {age} years old! How are you even able to type?")
        if age < 0:
            birth = input("Are you even born yet? \n")
            print(f"{birth}! Whatever you say, I guess.")
    else:
        print(f"Hello {name}! Wow, you're {age} years old! You're {dif} years younger than I am.")