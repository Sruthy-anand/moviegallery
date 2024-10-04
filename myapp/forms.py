from typing import Any
from django import forms

class MovieForm(forms.Form):

    title=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-3"}))

    options=(

        ("Action","Action"),
        ("Fiction","Fiction"),
        ("Drama","Drama"),
        ("Comedy","Comedy"),
    )

    genre=forms.ChoiceField(choices=options,widget=forms.Select(attrs={"class":"form-control form-select"}))

    language=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-3"}))

    year=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-3"}))

    run_time=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))

    director=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-3"}))

    def clean(self):
        
        cleaned_data=super().clean()

        year=cleaned_data.get("year")

        run_time=cleaned_data.get("run_time")

        if int(year)<1990:

            error_message="year > 1990"

            self.add_error("year",error_message)


        if run_time not in range(60,360):

            error_message="movie run_time in between 60 and 360"

            self.add_error("run_time",error_message)