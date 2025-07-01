from django import forms
# from .models import Question

class QuestionForm(forms.Form):
    def __init__(self, questions, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for question in questions :
            self.fields[f'question_{question.id}'] = forms.ChoiceField(
                    label=question.text,
                    choices=[
                        (1, question.option1),
                        (2, question.option2),
                        (3, question.option3),
                        (4, question.option4),
                    ],
                    widget=forms.RadioSelect,
                    required=True
            )
