# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True



def find_anagram(word, anagram):
    if len(word) != len(anagram):
        return False
    elif sorted (word) != sorted(anagram):
        return False
    else:
        return True   

print(find_anagram("wells", "swell"))        
print(find_anagram("silent", "listen"))
print(find_anagram("hello", "madam")) 
print(find_anagram("rail safety", "fairy tales"))