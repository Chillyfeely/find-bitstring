from heapq import heappush, heappop
import time

def find_bit_string(probabilities, target_string):
    """
    Find the most probable bit string given a list of probabilities for each bit
    and a target string to match.
    
    Args:
    probabilities: List of probabilities for each bit being 1
    target_string: Target string to match
    
    Returns:
    bit_string: Most probable bit string that matches the target string
    tries: Number of tries needed to find the target string
    """
    n = len(probabilities)  # Get the length of the bit string
    max_heap = [(-1.0, "")]  # Initialize max-heap with empty string and probability 1
    tries = 0  # Initialize counter for tries
    
    while max_heap:
        tries += 1  # Increment tries counter
        # Pop the most probable string
        neg_prob, bit_string = heappop(max_heap)
        prob = -neg_prob  # Convert back to positive probability
        
        if len(bit_string) == n:
            # If we've reached the target length
            if bit_string == target_string:
                return bit_string, tries
            continue
        
        # Calculate probabilities for the next bit being 1 or 0
        next_pos = len(bit_string)
        p1 = prob * probabilities[next_pos]
        p0 = prob * (1 - probabilities[next_pos])
        
        # Add new candidates to the heap
        heappush(max_heap, (-p1, bit_string + "1"))
        heappush(max_heap, (-p0, bit_string + "0"))
    
    return None, tries  # If not found, return tries

# Example usage
# 64-bit binary string
target_string = "11101001100111010110011001011011"

# Probabilities for each bi
probabilities = [0.9,0.5,0.7,0.4,0.9,0.9,0.5,0.7,0.4,0.9,0.4,0.5,0.9,0.5,0.7,0.4,0.9,0.4,0.5,0.6,0.3,0.6,0.7,0.4,0.9,0.4,0.5,0.6,0.3,0.6,0.7,0.4]
start_time = time.time()
result, tries = find_bit_string(probabilities, target_string)
end_time = time.time() 
print("Found string:", result)
print("Number of tries:", tries)
print("Runtime of the function is", end_time - start_time, "seconds")
