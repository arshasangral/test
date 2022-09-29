lst = ['qwertyuiop','asdfghjkl','zxcvbnm']
words = ["Hello","Alaska","Dad","Peace"]
lst1 = []

for word in words:
  flag = True  
  for i in lst:
    if word[0].lower() in i:
        for letter in range(1,len(word)):
            if word[letter] not in i:
                flag = False
                break
        if flag == True:
            lst1.append(word)

print(lst1)   
  
