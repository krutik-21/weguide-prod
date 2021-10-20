from .serializers import LoanSerializer,LoanListSerializer,CrowdSourceSerializer
from loans.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
import datetime
from ..forms import LoanFilter
from django_filters import rest_framework as filters
from django.core.paginator import Paginator
from .fieldSerializers import *

#Pagination Setting
PAGE_SIZE = 18


class api_filter_loan(generics.ListAPIView):
    '''filter'''
    queryset = Loan.objects.all().order_by('-updated_on')
    serializer_class = LoanSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = LoanFilter 
    pagination_class = PageNumberPagination
    

""" @api_view(['GET',])
def api_detail_loan(request,slug):
    try:
        sch = Loan.objects.get(slug=slug)
    except Loan.DoesNotExist :
        return Response(status.HTTP_404_NOT_FOUND)

    serializer = LoanSerializer(sch)
    context = {
        
        "results" : serializer.data
    }
    return Response(context) """




@api_view(['GET',])
def api_list_active_loan(request):
    '''api for loan list'''
    try:
        qs = Loan.objects.all().order_by('-updated_on')
        paginator = Paginator(qs, PAGE_SIZE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    except Loan.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    serializer = LoanSerializer(page_obj,many = True)
    context = {
        "count" : qs.count(),
        "results" : serializer.data
    }
    return Response(context)


@api_view(['GET',])
def api_search_loan(request):
    '''Search . q = search item'''
    try:
        q = request.GET.get('q')
        sch = Loan.objects.all()
        qs = sch.filter(title__icontains=q).order_by('-updated_on')
        paginator = Paginator(qs, PAGE_SIZE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    except Loan.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    serializer = LoanSerializer(page_obj,many = True)
    context = {
        "count" : qs.count(),
        "results" : serializer.data
    }
    return Response(context) 

@api_view(['GET'])
def form_fields(request):
    '''get form fields'''
    """ state = StateSerializer(State.objects.all(),many = True)
    district = DistrictSerializer(District.objects.all(),many = True) """
    religion = ReligionSerializer(Religion.objects.all(),many = True)
    loan_amount = LoanAmtSerializer(LoanAmt.objects.all(),many=True)
    country = CountrySerializer(Country.objects.all(),many = True)
    category = CategorySerializer(Category.objects.all(),many = True)

    data = {
        'religion':religion.data,
        'loan_amount':loan_amount.data,
        'country':country.data,
        'category':category.data
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
def getState(request):
    try:
        country = request.GET.get("country")
        state = State.objects.all().filter(country = country)
        result = StateSerializer(state, many = True)
        return Response(result.data)
    except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getDistrict(request):
    try:
        state = request.GET.get("state")
        district = District.objects.all().filter(state = state)
        result = DistrictSerializer(district, many = True)
        return Response(result.data)
    except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    


