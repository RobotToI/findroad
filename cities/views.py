import django.shortcuts
from cities.models import City

__all__ = (
    'home',
)

def home(request, pk=None):
    if pk:
        city = django.shortcuts.get_object_or_404(City, id=pk)
        context = {'object': city}
        return django.shortcuts.render(request, 'cities/detail.html', context)

    qs = City.objects.all()
    context = {'objects_list':qs}
    return django.shortcuts.render(request, 'cities/home.html', context)