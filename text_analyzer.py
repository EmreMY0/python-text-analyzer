import locale
from sys import argv
locale.setlocale(locale.LC_ALL,"en_US")

# Reads characters from the file and calculates the total number of characters.
def total_characters():
    with open(argv[1], encoding="utf-8", errors="ignore") as input_file:
        number_of_characters=0
        for line in input_file:
            number_of_characters+=len(line)
    return number_of_characters

# Reads words from the file without cleaning them from punctuations.
def uncleaned_words():
    with open(argv[1], encoding="utf-8", errors="ignore") as input_file:
        words = []
        for line in input_file:
            words += line.split()
    return words


 # Cleans words by removing punctuation and converts them to lowercase.
def pure_words(uncleaned_words_list):
    pure_words_list = []
    punctuations = ["(", ")", ".", ",", ":", ";", "'", "?", "!"]

    for uncleaned_word in uncleaned_words_list:
        while uncleaned_word[0] in punctuations:
            uncleaned_word = uncleaned_word[1:]
        while uncleaned_word[-1] in punctuations:
            uncleaned_word = uncleaned_word[:-1]
        pure_words_list.append(uncleaned_word.lower())
    return pure_words_list

# Identifies the end of sentences and returns the total number of sentences.
def sentence_finder(uncleaned_words_list):
    sentences=[]
    for sentFinishers in uncleaned_words_list:
        if list(sentFinishers)[-3:]==[".", ".", "."]: # Firstly checked for the "..." because they can be easily confused with ordinary dot(.) .
            sentences.append("...")
        else:
            if list(sentFinishers.strip("()"))[-1]== "." or list(sentFinishers.strip("()"))[-1]== "?" or list(sentFinishers.strip("()"))[-1]== "!":
                sentences.append(list(sentFinishers.strip("()"))[-1]) #Removing the "()" because they can be confused with sentence finisher punctuations.
    return len(sentences)

# Finds the shortest words and their frequencies as a list and sorting the list.
def shortest_words(clean_words):

    shortest_word=clean_words[0]
    shortest_words_list=[]
    for clean_word in clean_words:
        if len(shortest_word)>len(clean_word):
            shortest_word=clean_word
    # Packing list is used to list the word-frequency pair as a single element.
    packing_list=[]
    str_short=[] # This list is used for removing recurring elements with using not in property .
    packing_list.append(shortest_word)
    str_short.append(shortest_word)
    packing_list.append(clean_words.count(shortest_word) / len(clean_words))
    shortest_words_list.append(packing_list)

    for clean_word in clean_words:
        packing_list=[]
        if len(shortest_word)==len(clean_word):
            if clean_word not in str_short:
                str_short.append(clean_word)
                packing_list.append(clean_word)
                packing_list.append(clean_words.count(clean_word) / len(clean_words))
                shortest_words_list.append(packing_list)
    shortest_words_list.sort(key=lambda x:(-float(x[-1]),x[0]))
    return shortest_words_list

# Finds the longest words and their frequencies as a list and sorting the list.
def longest_words(clean_words):

    longest_word=clean_words[0]
    longest_words_list=[]
    for clean_word in clean_words:
        if len(longest_word)<len(clean_word):
            longest_word=clean_word
    # Packing list is used to list the word-frequency pair as a single element.
    packing_list=[]
    str_long=[] # This list is used for removing recurring elements with using not in property.
    packing_list.append(longest_word)
    str_long.append(longest_word)
    packing_list.append(clean_words.count(longest_word) / len(clean_words))
    longest_words_list.append(packing_list)

    for clean_word in clean_words:
        packing_list=[]
        if len(longest_word)==len(clean_word):
            if clean_word not in str_long:
                str_long.append(clean_word)
                packing_list.append(clean_word)
                packing_list.append(clean_words.count(clean_word) / len(clean_words))
                longest_words_list.append(packing_list)
    longest_words_list.sort(key=lambda x:(-float(x[-1]),x[0]))
    return longest_words_list

# Counts the total number of characters in words only.
def characters_just_words(clean_words):
    character_word=0
    for z in clean_words:
        character_word+=len(z)
    return character_word

# Calculates the word-to-sentence ratio.
def word_sentence_ratio(clean_words,sentences):
    return len(clean_words) / sentences

# Calculates word frequencies and returns a sorted list.
def  word_frequency(clean_words):
    word_frq_list=[]
    for h in clean_words:
        word_frq=[] # This list is used to  list the word-frequency pair as a single element.
        frequency=(clean_words.count(h) / len(clean_words))
        word_frq.append(h)
        word_frq.append(frequency)
        word_frq_list.append(word_frq)

    # sorting the elements of word frequency list
    word_frq_list.sort(key=lambda x:(-float(x[-1]),x[0]))

    # removing recurring elements from the word frequency list
    final_list=[]
    for g in word_frq_list:
        if g not in final_list:
            final_list.append(g)
    return final_list

# Main function is used for combine all operations and write the output to a file.
def main():

    short_word_list=shortest_words(pure_words(uncleaned_words()))
    long_word_list=longest_words(pure_words(uncleaned_words()))
    word_frequency_list=word_frequency(pure_words(uncleaned_words()))
    number_of_sentences=sentence_finder(uncleaned_words())
    cleaned_word_list=pure_words(uncleaned_words())
    number_of_characters_in_words=characters_just_words(pure_words(uncleaned_words()))
    words_per_sentence=word_sentence_ratio(pure_words(uncleaned_words()),number_of_sentences)
    number_of_characters=total_characters()
    number_of_words=len(cleaned_word_list)
    file_name=argv[1]

    # Writes the results to the output file.
    f = open(argv[2], "w", encoding="utf-8")
    f.write("{:24}:\n".format("Statistics about {}".format(file_name)))
    f.write("{:24}: {}\n".format("#Words", number_of_words))
    f.write("{:24}: {}\n".format("#Sentences", number_of_sentences))
    f.write("{:24}: {:.2f}\n".format("#Words/#Sentences", words_per_sentence))
    f.write("{:24}: {}\n".format("#Characters", number_of_characters))
    f.write("{:24}: {}\n".format("#Characters (Just Words)", number_of_characters_in_words))
    if len(short_word_list)>1:
        f.write("{:24}:\n".format("The Shortest Words"))
        for shrt_word in short_word_list:
            f.write("{:24} ({:.4f})\n".format(shrt_word[0], shrt_word[-1]))
    else:
        f.write("{:24}: {:24} ({:.4f})\n".format("The Shortest Word", short_word_list[0][0], short_word_list[0][1]))
    if len(long_word_list)>1:
        f.write("{:24}:\n".format("The Longest Words"))
        for long_word in long_word_list:
            f.write("{:24} ({:.4f})\n".format(long_word[0], long_word[-1]))
    else:
        f.write("{:24}: {:24} ({:.4f})\n".format("The Longest Word", long_word_list[0][0], long_word_list[0][1]))
    f.write("{:24}:\n".format("Words and Frequencies"))
    for word_and_freq in word_frequency_list:
        if word_and_freq== word_frequency_list[len(word_frequency_list)-1]:
            f.write("{:24}: {:.4f}".format(word_and_freq[0], word_and_freq[1]))
        else:
            f.write("{:24}: {:.4f}\n".format(word_and_freq[0], word_and_freq[1]))
    f.close()

# Executes the main function.
if __name__=="__main__":
    main()

"""
 Challenging Parts of this Assignment:
 1) Creating a list that contains the word and its frequency as a single element of the list.
    I also implemented this system when i creating the shortest and longest words list.
  
 2)Another challenging part was detecting the "..." as a sentence finisher since they could be easily confused with ordinary dot(.)
   while searching for a sentence finisher punctuation.Therefore, i firstly checked for the "...".
 
 3)Removing the last new line at the end of the ":" .I used for and if to solve this problem by deciding if the line is the last line.    
"""