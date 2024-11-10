import nltk
from nltk.corpus import wordnet as wn
from itertools import combinations

# Ensure NLTK WordNet data is available
nltk.download('wordnet')

def find_most_similar_group(words):
    """
    Groups words based on semantic similarity using WordNet synonyms.
    Returns a guess of four words that are most similar to each other.
    """
    max_similarity = 0
    best_group = []

    # Check combinations of 4 words
    for group in combinations(words, 4):
        # Calculate pairwise similarity within the group
        similarity_sum = 0
        for w1, w2 in combinations(group, 2):
            syn1 = wn.synsets(w1)
            syn2 = wn.synsets(w2)
            if syn1 and syn2:  # If synsets are found
                similarity = wn.path_similarity(syn1[0], syn2[0])
                if similarity:  # Avoid None values
                    similarity_sum += similarity

        # Average similarity within the group
        avg_similarity = similarity_sum / 6  # 6 pairs in a 4-word group

        # Select the group with highest average similarity
        if avg_similarity > max_similarity:
            max_similarity = avg_similarity
            best_group = list(group)

    return best_group

def model(words, strikes, isOneAway, correctGroups, previousGuesses, error):
    """
    Basic model implementation for Connections AI using WordNet-based heuristic.
    Returns a guessed group of 4 words.
    """
    # Find the most semantically similar group
    guess = find_most_similar_group(words)

    # Simple endTurn logic: continue guessing while strikes are less than 4
    endTurn = False if strikes < 4 else True

    return guess, endTurn
