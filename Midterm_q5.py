
punctuation = ",.?!'"  # Define punctuation characters to remove
def find_pattern(text):
    """
    Finds occurrences of words that start with 'b', have any number of letters,
    and end with 'Bob', while handling punctuation.

    :param text: The text to search in
    :return: The number of matches
    """
    count = 0  # Initialize match counter

    # Remove punctuation
    for p in punctuation:
        text = text.replace(p, " ")  # Replace punctuation with space

    words = text.split()  # Split the sanitized text into words

    for word in words:  # Loop through each word
        if word.lower().startswith("b") and word.endswith("Bob"):
            count += 1  # If pattern matches, increase count

    return count  # Return total matches


# Example usage:
text = """Bob and bigBob! were walking in the park when they met blueBob.
A boy named brownBob, was there too, talking to b123Bob.
Meanwhile, bouncyBob and brightBob? were playing soccer.
Behind the trees, someone yelled "baldBob is here!"
The sun was shining, but BobBob did not care.
Back at home, butterBob! was cooking, while bashfulBob? read a book.
Interestingly, bashBob and beepBob were not part of the game.
However, only Bob and blueBob were interested in the contest.
"""

print(find_pattern(text))