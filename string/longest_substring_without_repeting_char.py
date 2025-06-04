def lengthOfLongestSubstring(s: str) -> int:
    dictionary = {}
    previous_longest_string =0
    longest_string = 0

    for _, char in enumerate(s):
        if char not in dictionary:
            previous_longest_string+=1
            dictionary[char] = 1
        else:
            if(previous_longest_string > longest_string):
                longest_string = previous_longest_string

            dictionary = {}
            dictionary[char] = 1
            previous_longest_string = 1
        
    return longest_string
        
print(lengthOfLongestSubstring("pwwkew"))  # Output: 3