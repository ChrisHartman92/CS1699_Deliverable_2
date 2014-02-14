import unittest
import askfunc
import classify
from mock import patch, Mock, MagicMock

class TestClassification(unittest.TestCase) :

	'''
		Function under test: getClassification()
		Location of function: askfunc
		Purpose of test: Ensure correct function is called when 'person' is received from classify.classify_article
		Notes: stubs used for personQuest(), classify_article()
			mock used for sentences
	'''
	@patch.object(askfunc, 'personQuest')
	@patch.object(classify, 'classify_article')
	def test_class_person(self, mock_classify_article, mock_personQuest) :
		mock_classify_article.return_value = 'person'
		mock = MagicMock()
		with mock as sentences :
			value = askfunc.getClassification('person', sentences)
		mock_personQuest.assert_called()

	'''
		Function under test: getClassification()
		Location of function: askfunc
		Purpose of test: Ensure correct function is called when 'language' is received from classify.classify_article
		Notes: stubs used for languageQuest(), classify_article()
			mock used for sentences
	'''
	
	@patch.object(askfunc, 'languageQuest')
	@patch.object(classify, 'classify_article')
	def test_class_language(self, mock_classify_article, mock_languageQuest) :
		mock_classify_article.return_value = 'language'
		mock = MagicMock()
		with mock as sentences :
			value = askfunc.getClassification('language', sentences)
		mock_languageQuest.assert_called()

	'''
		Function under test: getClassification()
		Location of function: askfunc
		Purpose of test: Ensure correct function is called when 'instrument' is received from classify.classify_article
		Notes: stubs used for instrumentQuest(), classify_article()
			mock used for sentences
	'''

	@patch.object(askfunc, 'instrumentQuest')
	@patch.object(classify, 'classify_article')
	def test_class_instrument(self, mock_classify_article, mock_instrumentQuest) :
		mock_classify_article.return_value = 'instrument'
		mock = MagicMock()
		with mock as sentences :
			value = askfunc.getClassification('instrument', sentences)
		mock_instrumentQuest.assert_called()

	'''
		Function under test: getClassification()
		Location of function: askfunc
		Purpose of test: Ensure correct function is called when 'city' is received from classify.classify_article
		Notes: stubs used for cityQuest(), classify_article()
			mock used for sentences
	'''

	@patch.object(askfunc, 'cityQuest')
	@patch.object(classify, 'classify_article')
	def test_class_city(self, mock_classify_article, mock_cityQuest) :
		mock_classify_article.return_value = 'city'
		mock = MagicMock()
		with mock as sentences :
			value = askfunc.getClassification('city', sentences)
		mock_cityQuest.assert_called()
	
	'''
		Function under test: getClassification()
		Location of function: askfunc
		Purpose of test: Ensure no functions are called when unmatched keyword is returned from classify.classify_article()
		Notes: stubs used for personQuest(), languageQuest(), instrumentQuest(), cityQuest(), classify_article()
			mock used for sentences
	'''

	@patch.object(askfunc, 'personQuest')
	@patch.object(askfunc, 'languageQuest')
	@patch.object(askfunc, 'instrumentQuest') 
	@patch.object(askfunc, 'cityQuest')
	@patch.object(classify, 'classify_article')
	def test_class_unmatched(self, mock_classify_article, mock_personQuest, mock_languageQuest, mock_instrumentQuest, mock_cityQuest) :
		mock_classify_article.return_value = 'abcdef'
		mock = MagicMock()
		with mock as sentences :
			value = askfunc.getClassification('abcdef', sentences)
		assert not mock_personQuest.called
		assert not mock_languageQuest.called
		assert not mock_instrumentQuest.called
		assert not mock_cityQuest.called

	'''
		Function under test: personQuest()
		Location of function: askfunc
		Purpose of test: To ensure that personQuest does three things, namely:
				-Replace all underscores "_" with spaces " "
				-Place pre-generated sentences into cannedarray in the correct order
				-Return cannedarray correctly at the end of the function		
		Notes: String "abraham_lincoln" can be replaced with any String that has two or more words seperated by underscores
				-Example: mother_of_dragons is okay
				-	  mother_of_dragons_ is not
	'''

	def test_personQuest(self) :
		correctSentences = []
		correctSentences.append('On what date was abraham lincoln born?')
		correctSentences.append('On what date did abraham lincoln die?')
		correctSentences.append('How old was abraham lincoln when he died?')
		correctSentences.append('Was abraham lincoln ever married?')
		correctSentences.append('Who was abraham lincoln?')
		correctSentences.append('Did abraham lincoln attend college?')
		correctSentences.append('When did abraham lincoln come into this world?')
		correctSentences.append('Does the article mention that abraham lincoln published anything?')

		word = ['abraham_lincoln']
		sentences = askfunc.personQuest(word)
		self.assertEquals(correctSentences, sentences)

	'''
		Function under test: languageQuest()
		Location of function: askfunc
		Purpose of test: To ensure that languageQuest does three things, namely:
				-Replace all underscores "_" with spaces " "
				-Place pre-generated sentences into cannedarray in the correct order
				-Return cannedarray correctly at the end of the function		
		Notes: String "old_american_english" can be replaced with any String that has two or more words seperated by underscores
				-Example: old_valyrian is okay
				-	  old_valyrian_ is not
	'''


	def test_languageQuest(self) :
		correctSentences = []
		correctSentences.append('Where is the old american english spoken?')
		correctSentences.append('What language family is the old american english a part of?')
		correctSentences.append('Approximately how many people speak the old american english?')
		correctSentences.append('Who speaks the old american english?')
		correctSentences.append('What is the word order in old american english?')
		correctSentences.append('Does the old american english have vowels?')
		correctSentences.append('How many vowels does old american english have?')
		
		word = ['old_american_english']
		sentences = askfunc.languageQuest(word)
		self.assertEquals(correctSentences, sentences)

	'''
		Function under test: cityQuest()
		Location of function: askfunc
		Purpose of test: To ensure that cityQuest does three things, namely:
				-Replace all underscores "_" with spaces " "
				-Place pre-generated sentences into cannedarray in the correct order
				-Return cannedarray correctly at the end of the function		
		Notes: String "san_diego" can be replaced with any String that has two or more words seperated by underscores
				-Example: kings_landing is okay
				-	  kings_landing_ is not
	'''


	def test_cityQuest(self) :
		correctSentences = []
		correctSentences.append('What is the population of san diego?')
		correctSentences.append('In what country is san diego?')
		correctSentences.append('What is the population density of san diego?')
		correctSentences.append('What kind of transportation exists in san diego?')
		correctSentences.append('Where is san diego?')
		correctSentences.append('How old is san diego?')
		correctSentences.append('What kind of climate does san diego have?')
		
		word = ['san_diego'] 
		sentences = askfunc.cityQuest(word)
		self.assertEquals(correctSentences, sentences)

	'''
		Function under test: instrumentQuest()
		Location of function: askfunc
		Purpose of test: To ensure that instrumentQuest does three things, namely:
				-Replace all underscores "_" with spaces " "
				-Place pre-generated sentences into cannedarray in the correct order
				-Return cannedarray correctly at the end of the function		
		Notes: String "grand_paino" can be replaced with any String that has two or more words seperated by underscores
				-Example: dragon_binder is okay
				-	  dragon_binder_ is not
	'''


	def test_instrumentQuest(self) : 
		correctSentences = []
		correctSentences.append('What is the grand piano?')
		correctSentences.append('How is the grand piano played?')
		correctSentences.append('How does one play the grand piano?')
		correctSentences.append('Does the grand piano have strings?')
		correctSentences.append('Is the grand piano a wind instrument?')
		correctSentences.append('Is the grand piano a percussion instrument?')
		correctSentences.append('Where does the grand piano originate?')
		correctSentences.append('What kind of music is played on the grand piano?')
		
		word = ['grand_piano']
		sentences = askfunc.instrumentQuest(word)
		self.assertEquals(correctSentences, sentences)
	
	'''
		Function under test: fappend()
		Location of function: askfunc
		Purpose of test: To ensure that fappend concatenates two strings correctly 
		Notes: N/a
	'''

	def test_fappend_words(self) :
		testword1 = "test"
		testword2 = "this"
		testword1 = testword1 + testword2
		self.assertEquals(testword1, askfunc.fappend('test', 'this'))
	'''
		Function under test: fappend()
		Location of function: askfunc
		Purpose of test: To ensure that fappend concatenates two lists correctly
		Notes: N/a 
	'''

	def test_fappend_lists(self) :
		testlist1 = ['a', 'b', 'c']
		testlist2 = ['d', 'e']
		testlist1 = testlist1 + testlist2
		self.assertEquals(testlist1, askfunc.fappend(testlist1, testlist2))
	'''
		Function under test: fappend()
		Location of function: askfunc
		Purpose of test: To ensure that fappend does not concatenate a string and list
		Notes: Test designed to fail
	'''
	def test_fappend_mixed(self) :
		testword1 = "test"
		testlist1 = ['a', 'b', 'c']
		testword = testword1 + testlist1
		self.assertEquals(testword, askfunc.fappend(testword1, testlist1))	

if __name__ == '__main__' :
	unittest.main()
