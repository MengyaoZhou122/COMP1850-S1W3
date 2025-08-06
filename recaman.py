def generate_recaman(n):
    """
    Generate Recaman sequences
    :param n: The sequence length contains the starting a0
    :return: list of Recaman sequences

    """
    if n <= 0:
        return []
    
    sequence = [0]
    seen = {0}
    
    for k in range(1, n):
        prev = sequence[-1]
        candidate = prev - k  
        
        if candidate > 0 and candidate not in seen:
            sequence.append(candidate)
            seen.add(candidate)
        else:
            sequence.append(prev + k)
            seen.add(prev + k)
        return sequence
    if __name__ == "__main__":
        n = int(input().strip())
        result = generate_recaman(n)
        print(" ".join(map(str, result)))