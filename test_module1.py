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
		mock = MagicMock();
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
		mock = MagicMock();
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
		mock = MagicMock();
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
		mock = MagicMock();
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
		mock = MagicMock();
		with mock as sentences :
			value = askfunc.getClassification('abcdef', sentences)
		assert not mock_personQuest.called
		assert not mock_languageQuest.called
		assert not mock_instrumentQuest.called
		assert not mock_cityQuest.called

if __name__ == '__main__' :
	unittest.main()
