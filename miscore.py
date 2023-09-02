def miScore(wordOne, wordTwo, string):

    # Import modules
    import re
    import math 

    # Remove special characters
    string = re.sub("[^\w\s]", "", string)

    # Replace linespaces with a dash so that words on either side of the linespace are not identified by regex 
    string = string.replace("\n", " - ") 
                        
    # Initialise pattern to count collocations                
    contingencyApattern = rf'\b{wordOne}\s{wordTwo}\b'

    # Initialise pattern to count valid words in string 
    contingencyDpattern = r'\b\w+\b'

    # Counts number of collocations
    contingencyA = len(re.findall(contingencyApattern, string))

    # Counts instances of word one 
    contingencyB = string.count(wordOne)

    # Counts instances of word two
    contingencyC = string.count(wordTwo)

    # Counts number of words
    contingencyD = len(re.findall(contingencyDpattern, string))

    # Perform mi score formula
    miScore = math.log2( (contingencyA / contingencyD) / ((contingencyB / contingencyD) * (contingencyC / contingencyD)) )

    return miScore

