L = int(input("Length of sequence: "))  
if L <= 0:
    print("Invalid length")
else:
    sequence = [0]  
    seen = {0}      

    for k in range(1, L):
        prev = sequence[-1]
        next_val = prev - k

        if next_val > 0 and next_val not in seen:
            sequence.append(next_val)
            seen.add(next_val)
        else:
            next_val = prev + k
            sequence.append(next_val)
            seen.add(next_val)

    [print(item) for item in sequence]