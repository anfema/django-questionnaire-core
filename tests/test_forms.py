from questionnaire_core.models import Questionnaire, QuestionnaireResult

from .base import TestCaseBase


class ModelTestCase(TestCaseBase):
    def test_form_class_gets_created(self):
        """Form class gets created for questionnaire"""
        q1 = Questionnaire.objects.get(title="test1")
        form_class = q1.build_form_class(QuestionnaireResult())
        self.assertEqual(form_class.__name__, "QuestionnaireForm")
