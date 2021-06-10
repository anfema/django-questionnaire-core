from django.urls import reverse

from questionnaire_core.forms import QuestionnaireFormBase

from .base import TestCaseBase


class ViewTestCase(TestCaseBase):

    def test_generic_view_get(self):
        """Generic view renders on GET"""
        response = self.client.get(reverse('test_view'))

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], QuestionnaireFormBase)

    def test_generic_view_post(self):
        """Generic view renders on POST"""
        response = self.client.post(reverse('test_view'), data={}, follow=True)

        self.assertEqual(response.status_code, 200)
