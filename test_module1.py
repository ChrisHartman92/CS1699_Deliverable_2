import unittest
import askfunc
import classify
from mock import patch, Mock

class TestClassification(unittest.TestCase) :

	'''This test is trying to see if getClassification calls the right method based on the output of classify.classify_article
	'''
	@patch.object(askfunc, 'personQuest')
	@patch.object(classify, 'classify_article')
	def test_class_person(self, mock_classify_article, mock_personQuest) :
		mock_classify_article.return_value = 'person'
		value = askfunc.getClassification('person')
		mock_personQuest.assert_called_with()
	
	@patch.object(askfunc, 'languageQuest')
	@patch.object(classify, 'classify_article')
	def test_class_language(self, mock_classify_article, mock_languageQuest) :
		mock_classify_article.return_value = 'language'
		value = askfunc.getClassification('language')
		mock_languageQuest.assert_called_with()

	@patch.object(askfunc, 'instrumentQuest')
	@patch.object(classify, 'classify_article')
	def test_class_person1(self, mock_classify_article, mock_instrumentQuest) :
		mock_classify_article.return_value = 'instrument'
		value = askfunc.getClassification('instrument')
		mock_instrumentQuest.assert_called_with()

	@patch.object(askfunc, 'cityQuest')
	@patch.object(classify, 'classify_article')
	def test_class_person1(self, mock_classify_article, mock_cityQuest) :
		mock_classify_article.return_value = 'city'
		value = askfunc.getClassification('city')
		mock_cityQuest.assert_called_with()



if __name__ == '__main__' :
	unittest.main()

	
