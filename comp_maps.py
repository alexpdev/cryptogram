# Define functions of solving cyphertext

def configurations(phrase,matches):
    sorting = sorted(matches.items(),key=lambda x: len(x[1]["matches"]))
    least = sorting[0][1]
    first_word = least['words'][0]
    first_matches = least['matches']
    if len(least['words']) > 1:
        least['words'].remove(first_word)
    else:
        sorting = sorting[1:]
    final_matches = []
    for match in first_matches:
        p = phrase.update(first_word,match)
        # trace_words(p,matches)
