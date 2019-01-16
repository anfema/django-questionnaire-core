# -*- coding: utf-8 -*-
from django import forms

from .base import QuestionTypeBase


class ChoicesBase(QuestionTypeBase):
    class Meta:
        abstract = True

    def clean_question_options(self, question_options):
        """
        expected question_options format:
        {
            choices: [
                {value: "", label: ""}, ...
            ]
        }
        """
        if 'choices' not in question_options:
            raise forms.ValidationError('key "choices" required')
        if not isinstance(question_options.get('choices'), list):
            raise forms.ValidationError('list in "choices" required')
        if len(question_options.get('choices')) < 1:
            raise forms.ValidationError('list of "choices" is empty')
        for choice in question_options.get('choices'):
            if 'label' not in choice:
                raise forms.ValidationError('key "label" in choice is required')
            if 'value' not in choice:
                raise forms.ValidationError('key "value" in choice is required')

            # Clean whitespace and set 'value' to 'label' if it is empty.
            value = choice['value'].strip()
            label = choice['label'].strip()
            choice['value'] = value if value else label
            choice['label'] = label

        return question_options


class Choices(ChoicesBase):
    class Meta:
        name = 'choices'
        verbose_name = 'Choices'
        widget_class = forms.Select

    def formfield(self, result_set):
        choices = [(c.get('value'), c.get('label')) for c in self.question.question_options.get('choices')]

        if self.question.question_options.get('empty_label'):
            choices = [('', self.question.question_options.get('empty_label'))] + choices

        return forms.ChoiceField(
            widget=self.formfield_widget(),
            label=self.question.question_text,
            required=self.question.required,
            choices=choices,
            # validators=[validators.validate_slug],
        )


class ChoicesMultiple(ChoicesBase):
    class Meta:
        name = 'choices_multiple'
        verbose_name = 'Choices multiple'
        multiple = True
        widget_class = forms.CheckboxSelectMultiple

    def formfield(self, result_set):
        choices = [(c.get('value'), c.get('label')) for c in self.question.question_options.get('choices')]

        return forms.MultipleChoiceField(
            widget=self.formfield_widget(),
            label=self.question.question_text,
            required=self.question.required,
            choices=choices,
            # validators=[validators.validate_slug],
        )
