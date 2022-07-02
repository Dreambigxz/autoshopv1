from modules import *
from django.shortcuts import render
# from rest_framework import viewsets
# from rest_framework.views import APIView
# from rest_framework.response import Response
from main import main
from .models import Car
# from .serializers import CarSerializer
# Create your views here.


# class CarViewSet(viewsets.ModelViewSet):
#     serializer_class = CarSerializer
#     queryset = Car.objects.all().order_by('-id')

class CarDetailView(DetailView):
    model = Car
    context_object_name = "data"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        zip_tag = decode(context['data'].tags)
        related_key = context['data'].which_city
        zip_sub_images = context['data'].thumbnails
        context['extra_data'] = {
        'tags': zip_tag,
        'thumbnails': decode(zip_sub_images),
        'related_products': Car.objects.filter(which_city=related_key)
        }
        return  context

class CarListView(ListView):
    """docstring for CarListView."""
    model = Car
    paginate_by = 22
    queryset = Car.objects.all().order_by('-datetime')
    context_object_name = 'object_list'

    def get_queryset(self):
        query = self.request.GET.get('option')
        print(query)
        if query is not None:
            if query in [i.which_city for i in self.model.objects.filter(which_city__icontains=query)]:
                object_list = self.model.objects.filter(which_city__icontains=query)
            elif query in [i.which_area for i in self.model.objects.filter(which_area__icontains=query)]:
                object_list = self.model.objects.filter(which_area__icontains=query)
            else:
                object_list = self.model.objects.none()
        else:
            object_list = Car.objects.all().order_by('-datetime')
        return object_list

    def get_context_data(self, **kwargs):
        """ Facilitates pagination and post count summary """
        context = super(CarListView, self).get_context_data(**kwargs)
        context['current_page'] = context.pop('page_obj', None)
        context['citits'] = dict(Car.CITY_CATEGORIES)
        context['sfbay'] = Car.all_sf_bayAreas
        # print(context)
        return context

def get_search_data(request):
    option = request.GET['option']
    print(option)
    city = option
    search_area = ''

    # call main and pass the city search option
    """
    set searches condition
    """
    if option in  Car.all_sf_bayAreas.keys():
        # send options tomain
        """
        https://sfbay.craigslist.org/search/nby/cta?postedToday=1&lang=en&cc=gb
        """
        city = 'sfbay'
        search_area = option
        print(city, search_area)

    print("sending", search_area, city)
    send_request = main(is_manual=True, search=search_area, city=city)
    print(send_request)
    if True:
        pass

    #url = f'{request.META[HTTP_HOST]}option={option}'
    #domain = get_current_site(request).domain
    #print(domain)
    search = f'?option={option}'
    return JsonResponse(search, safe=False)
