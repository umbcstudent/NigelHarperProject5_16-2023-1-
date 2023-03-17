# This function returns the entirety of "Dracula" as a string
def readBook():
  f = open("dracula.txt", "r")
  s = f.read().replace("-", " ")
  f.close()
  return ''.join(c for c in s if c.isalnum() or c == " ")
#This function analyze the string to calculate the variable total counts
def summarize_book():
    # Read the book
    draculaText = readBook()
    # Get word count and find most common word
    words = draculaText.lower().split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    most_common_word = max(word_count, key=word_count.get)
    most_common_word_count = word_count[most_common_word]

    # Get unique four-letter words
    unique_four_letter_words = set(word for word in words if len(word) == 4)

    # Get words that appear more than 500 times
    frequent_words = {word: count for word, count in word_count.items() if count > 500}

    # Display results
    print("============== Result =================")
    #Print two blank space
    print()
    print()
    
    print("'{}' is the word that appear the most throughout a text, the total of {} times".format(most_common_word, most_common_word_count))
    #Print blank space
    print()
    
    print("There are {} words that are four letter long".format(len(unique_four_letter_words)))
    #Print blank space
    print()
    
    print("I noticed that these words show up more than 500 times:")
    for word, count in frequent_words.items():
        print("{} - {}".format(word, count))
      
#Call the function
summarize_book()




