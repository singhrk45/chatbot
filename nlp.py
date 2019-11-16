import nltk
import random
import string
from nn import NN
from jd import Normal
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

k=NN()
n = Normal()
class NLP:
	def __init__(self):
		self.symptoms=set()
		self.sentence=''
		self.greeting_input = ("hello", "hi", "greetings", "sup", "what's up","hey",)
		self.greeting_response = ["hi", "hey", "*nods*", "hi there", "hello"]
		self.newquestions=["what has exactly happened to you?","I am glad! You are talking to me","whats wrong with you my friend?"]
		self.repeatquestions = ["tell me more about your disease","tell me some symptoms of your illness","Tell me more! i will help you"] 



	def verifyGreeting(self):
		for word in self.sentence.split():
			if  word.lower() in self.greeting_input:
				return True
		return False
	


	def verifySymptoms(self):
		symlist = k.getSymptoms()
		tmp = []
		flag = False
		for word in self.sentence.split():
			if word.lower() in symlist:
				tmp.append(word)
				flag = True

		for i in symlist:
			if i in self.sentence:
				if i not in tmp:
					tmp.append(i)
				flag = True
		for i in tmp:
			self.symptoms.add(i)
		return flag


	def predict(self):
		return n.predict(list(self.symptoms))









	def processing(self,req):
		self.sentence = req
		self.sentence  = self.sentence.lower()
		if self.sentence == 'thank you':
			k= self.predict()
			if len(k)==0:
				return (1,"Sorry unable to detect your problem")
			if len(k)==1:
				return (1,"You are suffering from "+','.join(k))
			else:
				return (1,"You may suffer from one of these diseases - "+','.join(k))
		if self.verifyGreeting():
			return (0,random.choice(self.greeting_response))
		elif self.verifySymptoms():
			return (0,random.choice(self.repeatquestions))
		else:
			return (0,random.choice(self.newquestions))
		
