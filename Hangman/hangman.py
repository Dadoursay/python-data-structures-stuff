import random

words = ["apple", "banana", "cherry", "date", "elderberry",
    "fig", "grape", "honeydew", "kiwi", "lemon",
    "mango", "nectarine", "orange", "papaya", "quince",
    "raspberry", "strawberry", "tangerine", "ugli", "vanilla",
    "watermelon", "watermelon", "yam", "zucchini", "apricot",
    "blackberry", "cantaloupe", "dragonfruit", "grapefruit", "lime"]

#word = words[random.randint(0, len(words)-1)]

word = list(random.choice(words))

count = 0
count1 = 0

progress = ["_"] * len(word)



while count < 6:
  count1 = 0
  letter = str(input("Please Enter a Letter: "))
  for j in range(len(progress)):
    if progress[j] != "_":
      count1 = count1 + 1
      

  if count1 == len(progress) - 1:
    print("YOU WIN YAYYYAAYYAAYYAY")
    break

  for i in range(len(word)):
    if letter == word[i]:
      progress[i] = letter
      
      continue

      
      
  if letter not in progress:
    count = count + 1
    print("You have "+  str(6 - count) + " lives left")
    if count == 6:
      print("YOU LOSE HAHAAHHAAHAHAH")
      break
  print(str(progress))
  continue

  
  












