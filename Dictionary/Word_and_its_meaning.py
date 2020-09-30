# Make a dictionary and take input from the user and display the meaning of the word.
# Input words are mutable, immutable, wise, manmade, which each have their seperate meanings coded in the dictionary labeled as Dict1.

Dict1 = {"Mutable":"Something that can be changed",
         "Immutable":"Something that cannot be changed",
         "Wise":"The person who is morally correct",
         "Manmade":"The objects that were not readily available in nature."}
print("Search for the meanings of the following words:\n",
      "1. Immutable\n","2. Mutable\n","3. Wise\n","4. Manmade\n")
word = input()
print(Dict1[word])
