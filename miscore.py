def miScore(wordOne, wordTwo, source):

    # Import modules
    import re
    import math 

    # If a list, convert to string
    if type(source) is list: 
        source = ' '.join(source) 
    # If not a string, raise error (elif)
    elif not type(source) is str:
        raise TypeError(f"Only strings and lists may be used with the miScore function. Source is {str(type(source))[1:-1]}")

    # If wordOne equals word two, raise error
    if wordOne == wordTwo:
        raise ValueError("wordOne and wordTwo cannot be the same")
    
    # If wordOne or wordTwo are not in string, raise error
    for x in [wordOne, wordTwo]:
        if x not in source:
            raise ValueError(f'Ensure that word "{x}" is in the source')
    # Raise error if wordOne and wordTwo don't contain alphanumeric characters
        elif x.isalpha() == False:
            raise ValueError(f'Ensure that word "{x}" only contains alphanumeric characters')

    # Remove special characters
    source = re.sub("[^\w\s]", "", source)

    # Replace linespaces with a dash so that words on either side of the linespace are not identified by regex 
    source = source.replace("\n", " - ") 
                        
    # Initialise pattern to count collocations                
    contingencyApattern = rf'\b{wordOne}\s{wordTwo}\b'

    # Initialise pattern to count valid words in string 
    contingencyDpattern = r'\b\w+\b'

    # Counts number of collocations
    contingencyA = len(re.findall(contingencyApattern, source))

    # Counts instances of word one 
    contingencyB = source.count(wordOne)

    # Counts instances of word two
    contingencyC = source.count(wordTwo)

    # Counts number of words
    contingencyD = len(re.findall(contingencyDpattern, source))

    # Perform mi score formula 
    miScore = math.log2((contingencyA / contingencyD) / ((contingencyB / contingencyD) * (contingencyC / contingencyD)))

    return miScore