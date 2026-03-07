s=input().lower()
if len(set(s))>=26:
    print("pangram")
else:
    print("not")
