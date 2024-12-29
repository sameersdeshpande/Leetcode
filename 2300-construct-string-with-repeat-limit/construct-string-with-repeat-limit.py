import heapq

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # Step 1: Count the frequency of each character
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        
        # Step 2: Create a max-heap (by using negative ASCII values)
        max_heap = []
        for char, count in freq.items():
            heapq.heappush(max_heap, (-ord(char), count))  # Push negative to simulate max-heap

        result = []
        prev_char = None
        prev_count = 0

        # Step 3: Greedily construct the result string
        while max_heap:
            # Get the largest character
            char_val, count = heapq.heappop(max_heap)
            char = chr(-char_val)  # Convert back from negative to character

            # Add the current char to the result
            if char == prev_char:
                # If it's the same as the previous one, we can't add more than repeatLimit
                if prev_count < repeatLimit:
                    result.append(char)
                    prev_count += 1
                    # Update the frequency of the character and push it back into the heap if necessary
                    if count - 1 > 0:
                        heapq.heappush(max_heap, (char_val, count - 1))
                else:
                    # Add the next lexicographically smaller character if available
                    if max_heap:
                        next_char_val, next_count = heapq.heappop(max_heap)
                        next_char = chr(-next_char_val)
                        result.append(next_char)
                        prev_char = next_char
                        prev_count = 1
                        # Update the frequency of the next character and push it back into the heap
                        if next_count - 1 > 0:
                            heapq.heappush(max_heap, (next_char_val, next_count - 1))
                        # Push the current character back into the heap for later use
                        heapq.heappush(max_heap, (char_val, count))
            else:
                result.append(char)
                prev_char = char
                prev_count = 1
                # Update the frequency of the character and push it back into the heap if necessary
                if count - 1 > 0:
                    heapq.heappush(max_heap, (char_val, count - 1))

        return ''.join(result)