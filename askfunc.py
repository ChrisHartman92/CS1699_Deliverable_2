import classify

'''
	A possible unit test for these four functions found below would be to compare the cannedarray before and after the array. Before should be empty, after should be not.
	We should probably also check to make sure all underscores are replaced.
	More unit tests are possible if we really need it as well.
'''
def personQuest():
 cannedarray=[]
 cannedarray.append('On what date was %s born?' % sentences[0].replace('_',' '))
 cannedarray.append('On what date did %s die?' % sentences[0].replace('_',' '))
 cannedarray.append('How old was %s when he died?' % sentences[0].replace('_',' '))
 cannedarray.append('Was %s ever married?' % sentences[0].replace('_',' '))
 cannedarray.append('Who was %s?' % sentences[0].replace('_',' '))
 cannedarray.append('Did %s attend college?' % sentences[0].replace('_',' '))
 cannedarray.append('When did %s come into this world?' % sentences[0].replace('_',' '))
 cannedarray.append('Does the article mention that %s published anything?' % sentences[0].replace('_',' '))
 return cannedarray

def languageQuest(): 
 cannedarray=[]
 cannedarray.append('Where is the %s spoken?' % sentences[0].replace('_',' '))
 cannedarray.append('What language family is the %s a part of?' % sentences[0].replace('_',' '))
 cannedarray.append('Approximately how many people speak the %s?' % sentences[0].replace('_',' '))
 cannedarray.append('Who speaks the %s?' % sentences[0].replace('_',' '))
 cannedarray.append('What is the word order in %s?' % sentences[0].replace('_',' '))
 cannedarray.append('Does the %s have vowels?' % sentences[0].replace('_',' '))
 cannedarray.append('How many vowels does %s have?' % sentences[0].replace('_',' '))
 return cannedarray

def cityQuest():
 cannedarray=[]
 cannedarray.append('What is the population of %s?' % sentences[0].replace('_',' '))
 cannedarray.append('In what country is %s?' % sentences[0].replace('_',' '))
 cannedarray.append('What is the population density of %s?' % sentences[0].replace('_',' '))
 cannedarray.append('What kind of transportation exists in %s?' % sentences[0].replace('_',' '))
 cannedarray.append('Where is %s?' % sentences[0].replace('_',' '))
 cannedarray.append('How old is %s?' % sentences[0].replace('_',' '))
 cannedarray.append('What kind of climate does %s have?' % sentences[0].replace('_',' '))
 return cannedarray

def instrumentQuest():
 cannedarray=[]
 cannedarray.append('What is the %s?' % sentences[0].replace('_',' '))
 cannedarray.append('How is the %s played?' % sentences[0].replace('_',' '))
 cannedarray.append('How does one play the %s?' % sentences[0].replace('_',' '))
 cannedarray.append('Does the %s have strings?' % sentences[0].replace('_',' '))
 cannedarray.append('Is the %s a wind instrument?' % sentences[0].replace('_',' '))
 cannedarray.append('Is the %s a percussion instrument?' % sentences[0].replace('_',' '))
 cannedarray.append('Where does the %s originate?' % sentences[0].replace('_',' '))
 cannedarray.append('What kind of music is played on the %s?' % sentences[0].replace('_',' '))
 return cannedarray

'''
	For this function we can test to see what happens for each expected input (person, language, city, instrument) as well as unexpected input.
	We can have a few tests that we expect to fail here (entering an int should not work), and we can include that in the write up.
	We can also make sure that classify.classify_article() returns what it should based on what it is fed.
'''
def getClassification(article):
 classification=classify.classify_article(article)
 if classification == 'person':
  return personQuest()
 elif classification == 'language':
  return languageQuest()
 elif classification == 'city':
  return cityQuest()
 elif classification == 'instrument':
  return instrumentQuest()