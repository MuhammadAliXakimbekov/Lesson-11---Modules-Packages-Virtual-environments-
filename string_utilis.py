def reverse_string(s):
        s[::-1]
    

def count_vowels(s):
        vowels = 'aeiouAEIOU'
        count = 0
        for i in s:
                if i in vowels:
                    count += 1
        return count
print(count_vowels('MuhammadAli'))

