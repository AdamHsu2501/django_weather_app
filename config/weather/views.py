from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.views.generic.edit import FormView, DeleteView
from .models import City
from .form import CityForm
from .utils import get_city, is_city_exist, get_less_weather_info

API_KEY = 'b81a075161990b878215f078050ea4a9'


class CityListView(FormView):
    form_class = CityForm
    success_url = reverse_lazy('cities')
    template_name = 'weather/weather.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cities = City.objects.all()
        weather_data = []
        for city in cities:
            city_weather = get_city(city.name)
            less_weather_info = get_less_weather_info(city_weather)
            less_weather_info['pk'] = city.pk
            weather_data.append(less_weather_info)
        context["weather_data"] = weather_data
        return context

    def form_valid(self, form):
        post = self.request.POST.copy()
        city = get_city(post['name'])

        if is_city_exist(city):
            city_name = city['name']
            if City.objects.filter(name=city_name).count() == 0:
                post['name'] = city_name
                form = CityForm(post)
                form.save()

                messages.success(
                    self.request, '{} has been added successfully'.format(city_name))

                return super().form_valid(form)
            else:
                messages.warning(
                    self.request, '{} already exists'.format(city_name))
        else:
            messages.warning(
                self.request, city['message'].upper())

        return super().form_invalid(form)


class CityDeleteView(DeleteView):
    model = City
    template_name = 'weather/city_delete_comfirm.html'
    context_object_name = 'city'
    success_url = reverse_lazy('cities')
