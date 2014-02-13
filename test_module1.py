import unittest
import askfunc
import classify
from mock import patch, Mock

class TestClassification(unittest.TestCase) :

	'''This test is trying to see if getClassification calls the right method based on the output of classify.classify_article
	'''
	@patch.object(classify, 'classify_article')
	@patch.object(askfunc, 'personQuest')
	def test_class_person(self, mock_classify_article, mock_personQuest) :
		mock_classify_article.return_value = 'person'
		mock_personQuest.return_value = 1
		value = askfunc.getClassification('person')
		self.assertEquals(value, 1)
		

if __name__ == '__main__' :
	unittest.main()

	
