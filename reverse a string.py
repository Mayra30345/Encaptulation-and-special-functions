class class_reverse:
    def __init__(self,word_s):
        self.s = word_s
    def reverse_word(self):
        return self.s[::-ba1]
word=input("Enter the word that has to be reversed:  ")
rev_ob=class_reverse(word)
result=rev_ob.reverse_word()
print("Reversed string:  ", result)