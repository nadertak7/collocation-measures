# Collocation measures
A future python package with simple collocation measure functions

## How to use

### 1. Instantiate the `collocationScore` class

```python
# Import the class
from collocationmeasure import collocationScore

# Initialize the collocationScore object with word_one, word_two, and source text
instance = collocationScore(word_one, word_two, source_text)
```

- word_one (str): The first word for collocation comparison.
- word_two (str): The second word for collocation comparison.
- source_text (str or list): The text where collocations need to be analyzed.


### 2. Call the `t_score`, `mi_score` and `z_score` methods

- T-score

```python
t_score_result = instance.t_score()
print("T-Score:", t_score_result)
```

- MI-score

```python
mi_score_result = instance.mi_score()
print("MI Score:", mi_score_result)
```

- Z-score 

```python
z_score_result = instance.z_score()
print("Z-Score:", z_score_result)
```

### 3. Error handling

The code will raise an error if:
- the source text is not a string or list
- `word_one` and `word_two` are not the same
- either `word_one` or `word_two` does not exist in the source text
- no collocations between `word_one` and `word_two` are found in the source text


### 4. Customisation

The collocate_newlines parameter (default is False) allows you to consider or ignore newlines in the source text for collocations. If set to `True`, words on either side of the newline will be treated as collocates. `False` treats both words as separate entities. 