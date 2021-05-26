
import nltk as nltk
text= open('text.txt', encoding='utf-8').read()
#print(text)
import string
lower_case= text.lower()
#print(lower_case)

cleaned_text= lower_case.translate(str.maketrans('','',string.punctuation))
#print(cleaned_text)
from nltk.corpus import wordnet
from nltk.corpus import stopwords
sw= stopwords.words('english')
#print(sw)



from textblob import TextBlob
#rom vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analysis= TextBlob(text)
#print(dir(analysis))

#print(analysis.tags)
noun_phrases= analysis.noun_phrases
#print(analysis.noun_phrases)
#print(len(noun_phrases))

print(analysis.sentiment)


