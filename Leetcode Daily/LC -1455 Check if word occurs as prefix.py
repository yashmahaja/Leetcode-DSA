"""
Given a sentence that consists of some words separated by a single space, and a searchWord, check if searchWord is a prefix of any word in sentence.

Return the index of the word in sentence (1-indexed) where searchWord is a prefix of this word. If searchWord is a prefix of more than one word, return the index of the first word (minimum index). If there is no such word return -1.

A prefix of a string s is any leading contiguous substring of s.
"""



def isPrefixOfWord(sentence: str, searchWord: str) -> int:
    mini = float("inf")
    sentenceList = sentence.split()
    indx = 0
    for idx, word in enumerate(sentenceList):
        if searchWord in word:
            while indx < len(searchWord) and searchWord[indx] == word[indx]:
                if searchWord[indx] == word[indx]:
                    indx += 1
                else:
                    mini = 1
                    break
                if indx == len(searchWord):
                    mini = idx + 1
                mini = min(mini, idx + 1)

            indx = 0
    if mini == float("inf"):
        mini = -1
    return mini

sen = "i love eating bunburger burger"
word = "burg"
print(isPrefixOfWord(sen,word))

