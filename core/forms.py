from django import forms
from .models import Habit, Record


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = [
            "noun",
            "verb",
            "number",
            "noun_singular",
            "user",
        ]


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ["number"]
