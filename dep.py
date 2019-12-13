def sort_matches(matches):
    match = []
    for k,v in matches.items():
        if not match:
            match.append(k)
        elif total_alpha(k) >= total_alpha(match[-1]):
            if len(v['matches']) < len(matches[match[-1]]['matches']):
                match.append(k)
    return match[::-1]

def total_alpha(seq):
    return len([i for i in seq if isinstance(i,str)])
