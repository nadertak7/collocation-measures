# Import modules
import re
import math 

class collocationScore:
    """Calculates collocation scores for two given words within a source text.

    Args:
        word_one (str): The first word for collocation comparison.
        word_two (str): The second word for collocation comparison.
        source (str): The source text used for collocation analysis.
        collocate_newlines (bool, optional): Flag determining whether to consider newlines for collocations. Default is False.

    Methods:
        t_score(): Calculate the t-score for the collocation of word_one and word_two.
        mi_score(): Calculate the mutual information score for the collocation of word_one and word_two.
        z_score(): Calculate the z-score for the collocation of word_one and word_two.

    Raises:
        TypeError: If the source is not a string or list.
        ValueError: If word_one and word_two are the same or not present in the source.
        ValueError: If word_one or word_two contains non-alphanumeric characters.
        ValueError: If no collocations are found in the source text.
    """  

    def __init__(self, word_one, word_two, source, collocate_newlines=False):
        # If a list, convert to string
        if type(source) is list: 
            source = ' '.join(str(x) for x in source) 
        # If not a source, raise error
        elif not type(source) is str:
            raise TypeError(f"Only strings and lists may be used with the miScore function. Source is {str(type(source))[1:-1]}")

        # Convert to lowercase 
        for string_var in [word_one, word_two, source]:
            string_var.lower()

        # If word_one equals word two, raise error
        if word_one == word_two:
            raise ValueError("word_one and word_two cannot be the same")
        
        # If word_one or word_two are not in source, raise error
        for word in [word_one, word_two]:
            if word not in source:
                raise ValueError(f"Ensure that word '{word}' is in the source")
        # Raise error if word_one and word_two don't contain alphabetical characters
            elif word.isalpha() == False:
                raise ValueError(f"Ensure that word '{word}' only contains alphabetical characters")
        
        # Prevents escape characters from interfering with the output score (by doubling them)
        source = source.replace('\\', '\\\\')

        # Remove special characters
        resubs = [  
                    (r"[^\w\s]", ""),
                    (r" +", " ")
                ]
        
        for old, new in resubs:
            source = re.sub(old, new, source)

        # Replace linespaces with a dash so that words on either side of the linespace are not identified by regex 
        if not collocate_newlines:
            source = source.replace("\n", " - ") 
        else:
            source = source.replace("\n", " ")

        self.source = source
                            
        # Initialise pattern to count collocations. There can be any number of spaces between word_one and word_two.              
        contingencyApattern = rf'\b{word_one}\s+{word_two}\b'

        # Initialise pattern to count valid words in source 
        contingencyDpattern = r'\b\w+\b'

        # Counts number of collocations
        self.contingencyA = len(re.findall(contingencyApattern, source))

        if self.contingencyA == 0: 
            raise ValueError("Ensure that both words are collocated within the source text")

        # Counts instances of word one 
        self.contingencyB = source.count(word_one)

        # Counts instances of word two
        self.contingencyC = source.count(word_two)

        # Counts number of words
        self.contingencyD = len(re.findall(contingencyDpattern, source))

    def t_score(self):
        """Calculate the t-score for the collocation of word_one and word_two.

        Returns:
            float: t-score value.
        """
        
        t_score = (self.contingencyA - (self.contingencyB * self.contingencyC) / self.contingencyD ) / math.sqrt(self.contingencyA)
        return t_score

    def mi_score(self):
        """Calculate the mutual information score for the collocation of word_one and word_two.

        Returns:
            float: mutual information score value.
        """

        mi_score = math.log2((self.contingencyA / self.contingencyD) / ((self.contingencyB / self.contingencyD) * (self.contingencyC / self.contingencyD)))
        return mi_score
    
    def z_score(self):
        """Calculate the z-score for the collocation of word_one and word_two.

        Returns:
            float: z-score value.
        """
        
        z_score = (self.contingencyA  - (self.contingencyB * self.contingencyC) / self.contingencyD ) / ((math.sqrt(self.contingencyB * self.contingencyC)) / self.contingencyD)
        return z_score
        
