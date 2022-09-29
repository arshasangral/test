lst = ['qwertyuiop','asdfghjkl','zxcvbnm']
words = ["Hello","Alaska","Dad","Peace"]
lst2 = []

for word in words:
  flag = True  
  for i in lst:
    if word[0].lower() in i:
        for letter in range(1,len(word)):
            if word[letter] not in i:
                flag = False
                break
        if flag == True:
            lst2.append(word)

print(lst2)   
  
