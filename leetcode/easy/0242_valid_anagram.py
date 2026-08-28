def is_anagram_mine(s, t):
    def count_letters_mine(text):
        count=[0]*26
        for ch in text:
            index = ord(ch)-ord('a')
            count[index]+=1
        return count
    if count_letters_mine(s) == count_letters_mine(t):
        return True
    return False
#法一，我自己想的，26位英文字母限制，可以直接建立0~25的数组

def is_anagram_dict(s, t):
    def count_letters_dict(text):
        count = {}
        for ch in text:
            if ch in count:
                count[ch]+=1
            else:
                count[ch]=1
        return count
    if count_letters_dict(s) == count_letters_dict(t):
        return True
    return False
#法二，dict做法，学习dict

s = "anagram"
t = "nagaram"

print(is_anagram_dict(s, t))