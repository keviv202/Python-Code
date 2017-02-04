def tokenize(string, lowercase=False):
    """Extract words from a string containing English words.
    Handling of hyphenation, contractions, and numbers is left to your
    discretion.
    Tip: you may want to look into the `re` module.
    Args:
        string (str): A string containing English.
        lowercase (bool, optional): Convert words to lowercase.
    Returns:
        list: A list of words.
    """
    import re
    if lowercase == True:
        string = (string).lower()
    m = re.findall(r"[\w']+", string)
    return m

def lexical_density(string):
    """Calculate the lexical density of a string containing English words.
    The lexical density of a sequence is defined to be the number of
    unique words divided by the number of total words. The lexical
    density of the sentence "The dog ate the hat." is 4/5.
    Ignore capitalization. For example, "The" should be counted as the same
    type as "the".
    This function should use the `text2wordfreq` function.
    Args:
        string (str): A string containing English.
    Returns:
        float: Lexical density.
    """
    l = tokenize(string,True)
    l1 = []
    print(l)
    for i in l:
        if i not in l1:
            l1.append(i)
    return (len(l1)/len(l))


def shared_words(text1, text2):
    """Identify shared words in two texts written in English.
    Your function must make use of the `tokenize` function above. You should
    considering using Python `set`s to solve the problem.
    Args:
        text1 (str): A string containing English.
        text2 (str): A string containing English.
    Returns:
        set: A set with words appearing in both `text1` and `text2`.
    """
    a = tokenize(text1)
    b = tokenize(text2)
    return set(a).intersection(b)



def jaccard_similarity(text1, text2):
    """Calculate Jaccard Similarity between two texts.
    The Jaccard similarity (coefficient) or Jaccard index is defined to be the
    ratio between the size of the intersection between two sets and the size of
    the union between two sets. In this case, the two sets we consider are the
    set of words extracted from `text1` and `text2` respectively.
    This function should ignore capitalization. A word with a capital
    letter should be treated the same as a word without a capital letter.
    Args:
        text1 (str): A string containing English words.
        text2 (str): A string containing English words.
    Returns:
        float: Jaccard similarity
    """
    # YOUR CODE HERE
    a = tokenize(text1,True)
    a1 = tokenize(text2,True)
    l = shared_words(a,a1)
    l2 = list(set(a).union(a1))

    print(l)
    print(l2)

    return len(l)/len(l2)




text1 = "Eight million Americans"
text2 = "Americans in the South"

jaccard_similarity(text1, text2)