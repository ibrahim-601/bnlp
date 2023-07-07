__version__ = "4.0.0"


import os
from bnlp.pos import POS
from bnlp.ner import NER
from bnlp.tokenizer.nltk import NLTKTokenizer
from bnlp.tokenizer.basic import BasicTokenizer
from bnlp.tokenizer.sentencepiece import SentencepieceTokenizer
from bnlp.tokenizer.sentencepiece import SentencepieceTrainer
from bnlp.embedding.word2vec import BengaliWord2Vec
from bnlp.embedding.glove import BengaliGlove
from bnlp.embedding.doc2vec import BengaliDoc2vec
from bnlp.cleantext.clean import CleanText