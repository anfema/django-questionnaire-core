from django.test import TestCase

from questionnaire_core.models import Question, Questionnaire


class ModelTestCase(TestCase):
    def test_ordering_create(self):
        """Questions are ordered in creation order"""
        test_questionnaire = Questionnaire.objects.create(title="test_ordering_1")
        Question.objects.create(
            questionnaire=test_questionnaire,
            question_type="boolean",
            question_text="question 1",
        )
        Question.objects.create(
            questionnaire=test_questionnaire,
            question_type="boolean",
            question_text="question 2",
        )

        self.assertEqual(test_questionnaire.questions.get(question_text="question 1").order, 0)
        self.assertEqual(test_questionnaire.questions.get(question_text="question 2").order, 1)

    def test_ordering_bulk_create(self):
        """Questions are ordered in creation order by bulk_create()"""
        test_questionnaire = Questionnaire.objects.create(title="test_ordering_2")
        Question.objects.bulk_create(
            [
                Question(
                    questionnaire=test_questionnaire,
                    question_type="boolean",
                    question_text="question 1",
                ),
                Question(
                    questionnaire=test_questionnaire,
                    question_type="boolean",
                    question_text="question 2",
                ),
            ]
        )

        self.assertEqual(test_questionnaire.questions.get(question_text="question 1").order, 0)
        self.assertEqual(test_questionnaire.questions.get(question_text="question 2").order, 1)
