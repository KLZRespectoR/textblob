print("President’s Name: Joe Biden")
print("Date of speech: 20 January 2021")
print("Title of the speech: Inaugural Address Speech")
print("Source: https://millercenter.org/the-presidency/presidential-speeches/january-20-2021-inaugural-address")
import nltk as nltk
text= open('text.txt', encoding='utf-8').read()
print("the length of the speech:", len(text))
import string
lower_case= text.lower()
#print(lower_case)
print("the length of the text on lower case:", len(lower_case))

cleaned_text= lower_case.translate(str.maketrans('','',string.punctuation))
#print(cleaned_text)
print("the length of the text without punctuation:", len(cleaned_text))
from nltk.corpus import wordnet
from nltk.corpus import stopwords
sw= stopwords.words('english')
#print(sw)

from nltk.tokenize import word_tokenize
tokenized_words= word_tokenize(cleaned_text, "english")
final_words=[]
for word in tokenized_words:
    if word not in sw:
        final_words.append(word)
#print(final_words)
print("the length of the text after tokenization:", len(final_words))

from nltk.sentiment.vader import SentimentIntensityAnalyzer


def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    print("NLTK_sentimentintensityanalyzer:", score)
    neg = score['neg']
    pos = score['pos']
    if neg > pos:
        print("Negative Sentiment")
    elif pos > neg:
        print("Positive Sentiment")
    else:
        print("Neutral Vibes")




sentiment_analyse(cleaned_text)

from textblob import TextBlob
#from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analysis= TextBlob(text)
#print(dir(analysis))
print("Frequency: word of intreset: america:", analysis.word_counts['america'])
#print(analysis.tags)
noun_phrases= analysis.noun_phrases
#print(analysis.noun_phrases)
print("the number of noun phrases used:", len(noun_phrases))

print("Blobtext_sentimentintensityanalyzer:", analysis.sentiment)


print("Laith Alhmeidi: Bachelor Thesis")