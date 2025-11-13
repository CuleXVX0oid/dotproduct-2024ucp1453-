def dot_product(vector_a, vector_b):
    # Check if the vectors are the same length
    if len(vector_a) != len(vector_b):
        raise ValueError("Vectors must be the same length")
    
    # Compute the dot product
    result = sum(a * b for a, b in zip(vector_a, vector_b))
    
    return result

# Example usage:
vector_a = [1, 2, 3]
vector_b = [4, -5, 6]

result = dot_product(vector_a, vector_b)
print("Dot Product:", result)

