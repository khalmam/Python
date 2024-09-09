# Write code to get a list with 
# words without typos

words_with_typos = ["Aple", "Wether", "Newpaper"]
words_without_typos = []

for word in words_with_typos:
    prompt = f"""Fix the spelling mistake in the following word: {word}
    Provide only the word.
    """
    correct_word = get_llm_response(prompt)
    ### WRITE CODE HERE  ###
    words_without_typos.append(correct_word)
    #Hint: Append the correct_word to the words_without_typos list 
    ### --------------- ###

print(words_without_typos)