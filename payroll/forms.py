from django import forms


class MonthSelectionForm(forms.Form):
    MONTHS = [
        ('01', 'Январь'), ('02', 'Февраль'), ('03', 'Март'),
        ('04', 'Апрель'), ('05', 'Май'), ('06', 'Июнь'),
        ('07', 'Июль'), ('08', 'Август'), ('09', 'Сентябрь'),
        ('10', 'Октябрь'), ('11', 'Ноябрь'), ('12', 'Декабрь'),
    ]
    month = forms.ChoiceField(choices=MONTHS, label="Выберите месяц")
