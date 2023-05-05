# birthday/views.py 
from django.shortcuts import render

from .forms import BirthdayForm
# Импортируем из utils.py функцию для подсчёта дней.
from .utils import calculate_birthday_countdown
from .models import Birthday

def birthday(request):
    form = BirthdayForm(request.POST or None)
    # Создаём словарь контекста сразу после инициализации формы.
    context = {'form': form}
    # Если форма валидна...
    if form.is_valid():
        # ...вызовем функцию подсчёта дней:
        form.save()
        birthday_countdown = calculate_birthday_countdown(
            # ...и передаём в неё дату из словаря cleaned_data.
            form.cleaned_data['birthday']
        )
        # Обновляем словарь контекста: добавляем в него новый элемент.
        context.update({'birthday_countdown': birthday_countdown})
    return render(request, 'birthday/birthday.html', context)


def birthday_list(request):
    birthdays = Birthday.objects.all()
    template_name = 'birthday/birthday_list.html'
    context = {'birthdays': birthdays}
    return render(request, template_name, context)