import os
import nltk
import nltk.corpus
import nltk.corpus.stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.util import bigrams,trigrams,ngrams
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.corpus import stopwords
import re

AI="Knowledge engineering is a core part of AI research. Machines can often act and react like humans only if they have abundant information relating to the world. Artificial intelligence must have access to objects, categories, properties and relations between all of them to implement knowledge engineering. Initiating common sense, reasoning and problem-solving power in machines is a difficult and tedious task. Machine learning is also a core part of AI. Learning without any kind of supervision requires an ability to identify patterns in streams of inputs, whereas learning with adequate supervision involves classification and numerical regressions. Classification determines the category an object belongs to and regression deals with obtaining a set of numerical input or output examples, thereby discovering functions enabling the generation of suitable outputs from respective inputs. Mathematical analysis of machine learning algorithms and their performance is a well-defined branch of theoretical computer science often referred to as computational learning theory. Machine perception deals with the capability to use sensory inputs to deduce the different aspects of the world, while computer vision is the power to analyze visual inputs with a few sub-problems such as facial, object and gesture recognition. Robotics is also a major field related to AI. Robots require intelligence to handle tasks such as object manipulation and navigation, along with sub-problems of localization, motion planning and mapping."

AI_tokens=word_tokenize(AI)
for word in AI_tokens:
 fdist[word.lower()]+=1
print(fdist)
fdist.most_common(5)
list(nltk.ngrams(quotes_tokens,5))
pst=PorterStemmer()
lst=LancasterStemmer()
punctuation=re.compile(r'[-.?!,:;()|0-9]')
for words in AI_tokens:
 word=punctuation.sub("",words)
 if len(word)>0:
  post_punctuation.append(word)
print(post_punctuation)
for token in sent_tokens:
 print(nltk.pos_tag([token]))
ne_ner=ne_chunk(ne_tags)
grammar_np=r"NP: {<DT>?<JJ>*<NN>}"
chunk_parser=nltk.RegexpParser(grammar_np)
chunk_result=chunk_parser.parse(new_tokens)







