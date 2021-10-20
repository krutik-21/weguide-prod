from .serializers import BookbankSerializer,CrowdSourceSerializer
from bookbanks.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
import datetime
from ..forms import BookbankFilter
from django_filters import rest_framework as filters
from django.core.paginator import Paginator
from .fieldSerializers import *

#Pagination Setting
PAGE_SIZE = 18


class api_filter_bookbank(generics.ListAPIView):
    '''filter for bookbank'''
    queryset = Bookbank.objects.all().order_by('-updated_on')
    serializer_class = BookbankSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BookbankFilter 
    pagination_class = PageNumberPagination
    

@api_view(['GET',])
def api_detail_bookbank(request,slug):
    '''get detail of a scholarship using slug'''
    try:
        sch = Bookbank.objects.get(slug=slug)
    except Bookbank.DoesNotExist :
        return Response(status.HTTP_404_NOT_FOUND)

    serializer = BookbankSerializer(sch)
    context = {
        
        "results" : serializer.data
    }
    return Response(context)



@api_view(['GET',])
def api_list_active_bookbank(request):
    '''get list of bookbanks'''
    try:
        qs = Bookbank.objects.all().order_by('-updated_on')
        paginator = Paginator(qs, PAGE_SIZE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    except Bookbank.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    serializer = BookbankSerializer(page_obj,many = True)
    context = {
        "count" : qs.count(),
        "results" : serializer.data
    }
    return Response(context)




@api_view(['GET',])
def api_search_bookbank(request):
    '''search bookbank'''
    try:
        q = request.GET.get('q')
        sch = Bookbank.objects.all()
        qs = sch.filter(title__icontains=q).order_by('-updated_on')
        paginator = Paginator(qs, PAGE_SIZE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    except Bookbank.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    serializer = BookbankSerializer(page_obj,many = True)
    context = {
        "count" : qs.count(),
        "results" : serializer.data
    }
    return Response(context) 

@api_view(['GET'])
def form_fields(request):
    '''form feilds for filter'''
    state = StateSerializer(State.objects.all(),many = True)
    """ district = DistrictSerializer(District.objects.all(),many = True) """
    books = BookSerializer(Books.objects.all(),many = True)

    data = {
        'state':state.data,
        'books':books.data,
    }

    return Response(data)

    
@api_view(['POST','GET'])
def crowdSourceView(request):
    ''' api for crowd source '''

    if request.method == 'GET':
        try:
            scholarship = CrowdSource.objects.all()
            serializer = CrowdSourceSerializer(scholarship,many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
            
    elif request.method=='POST':
        serializer = CrowdSourceSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def getDistrict(request):
    try:
        state = request.GET.get("state")
        district = District.objects.all().filter(state = state)
        result = DistrictSerializer(district, many = True)
        return Response(result.data)
    except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


