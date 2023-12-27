# NLP-Grammar-Checker
We write a grammar and a parser to parse the POS tag sequence.

- Input data: sentences with POS tags
  The input is a tsv (tab-separated values) file like the sample:
  |id|label|sentence|pos|
  | -|-----|--------|---|
  |73|0|Many thanks in advance for your cooperation .| JJ NNS IN NN IN PRP$ NN .| 74| 1| At that moment we saw the bus to come .|IN DT NN PRP VBD DT NN TO VB .|

  The id column is the unique id for each sentence. The label column indicates whether a sentence contains grammar errors (1 means having errors and 0 means error-free). The pos column contains the POS tags for each token in the sentence, also separated by a single space. The POS tags follow the Penn Treebank (PTB) tagging scheme, as described [here](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html).


# Report 
Further details and results can be found [here]
# Contributors

Leen Alzebdeh (ccid:alzebdeh)

Sukhnoor Khehra (ccid:skhehra)

# Resources Consulted

[Penn Treebank P.O.S. Tags](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html)

Jurafsky, D., &amp; Martin, J. H. (2009). Speech and language processing: An introduction to natural language processing, computational linguistics, and speech recognition. Pearson Prentice Hall.

GitHub Copilot

## Libraries

We run this project using standard Python libraries csv, sys, nltk.

# Instructions to execute code

1. Ensure Python is installed, as well as the Python Standard Library.

2. Ensure the library nltk is installed, it can be installed using the following command: 

`pip install --user -U nltk`


Example usage: use the following command in the current directory.

`python3 src/main.py data/train.tsv grammars/toy.cfg output/train.tsv`


