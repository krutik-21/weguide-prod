from .serializers import ScholarshipSerializer,CrowdSourceSerializer
from scholarships.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
import datetime
from ..forms import ScholarshipFilter
from django_filters import rest_framework as filters
from django.core.paginator import Paginator
from .fieldSerializers import *

#Pagination Setting
PAGE_SIZE = 18


class api_filter_scholarship(generics.ListAPIView):
    '''filter.Get scholarships whose deadline has not yet passed.'''
    queryset = Scholarship.objects.all().filter(deadline__gte = datetime.datetime.now().strftime("%Y-%m-%d") ).order_by('deadline')
    serializer_class = ScholarshipSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ScholarshipFilter 
    pagination_class = PageNumberPagination
    

@api_view(['GET',])
def api_detail_scholarship(request,slug):
    '''get scholarship detail using slug'''
    try:
        sch = Scholarship.objects.get(slug=slug)
    except Scholarship.DoesNotExist :
        return Response(status.HTTP_404_NOT_FOUND)

    serializer = ScholarshipSerializer(sch)
    context = {
        
        "results" : serializer.data
    }
    return Response(context)


""" @api_view(['GET',])
def api_state_list_scholarship(request,state):
    try:
        sort = request.GET.get('sort')
        sch = Scholarship.objects.all()
        if sort:
            qs = sch.filter(state__name__icontains=state).filter(deadline__gte = datetime.datetime.now().strftime("%Y-%m-%d") ).order_by('-updated_on')
        else:
            qs = sch.filter(state__name__icontains=state).filter(deadline__gte = datetime.datetime.now().strftime("%Y-%m-%d") ).order_by('deadline')
        paginator = Paginator(qs, PAGE_SIZE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    except Scholarship.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    serializer = ScholarshipSerializer(page_obj,many = True)
    context = {
        "count" : qs.count(),
        "results" : serializer.data
    }
    return Response(context) """
 

""" @api_view(['GET',])
def api_class_list_scholarship(request,sclass):
    try:
        sort = request.GET.get('sort')
        sch = Scholarship.objects.all()
        if sort:
            qs = sch.filter(sclass__name__icontains=sclass).filter(deadline__gte = datetime.datetime.now().strftime("%Y-%m-%d") ).order_by('-updated_on')
        else:
            qs = sch.filter(sclass__name__icontains=sclass).filter(deadline__gte = datetime.datetime.now().strftime("%Y-%m-%d") ).order_by('deadline')
        paginator = Paginator(qs, PAGE_SIZE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    except Scholarship.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    serializer = ScholarshipSerializer(page_obj,many = True)
    context = {
        "count" : qs.count(),
        "results" : serializer.data
    }
    return Response(context)  """
 

""" @api_view(['GET',])
def api_type_list_scholarship(request,stype):
    try:
        sort = request.GET.get('sort')
        sch = Scholarship.objects.all()
        if sort:
            qs = sch.filter(stype__icontains=stype).filter(deadline__gte = datetime.datetime.now().strftime("%Y-%m-%d") ).order_by('-updated_on')
        else:
            qs = sch.filter(stype__icontains=stype).filter(deadline__gte = datetime.datetime.now().strftime("%Y-%m-%d") ).order_by('deadline')
        paginator = Paginator(qs, PAGE_SIZE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    except Scholarship.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    serializer = ScholarshipSerializer(page_obj,many = True)
    context = {
        "count" : qs.count(),
        "results" : serializer.data
    }
    return Response(context) """


@api_view(['GET',])
def api_list_active_scholarship(request):
    '''list of active scholarship whose deadline has not yet passed'''
    try:
        sort = request.GET.get('sort')
        if sort:
            qs = Scholarship.objects.all().filter(deadline__gte = datetime.datetime.now().strftime("%Y-%m-%d") ).order_by('-updated_on')
        else:
            qs = Scholarship.objects.all().filter(deadline__gte = datetime.datetime.now().strftime("%Y-%m-%d") ).order_by('deadline')
        paginator = Paginator(qs, PAGE_SIZE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    except Scholarship.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    serializer = ScholarshipSerializer(page_obj,many = True)
    context = {
        "count" : qs.count(),
        "results" : serializer.data
    }
    return Response(context)


@api_view(['GET',])
def api_list_inactive_scholarship(request):
    '''list of inactive scholarship'''
    try:
        sort = request.GET.get('sort')
        if sort:
            qs = Scholarship.objects.all().exclude(deadline__gte = datetime.datetime.now().strftime("%Y-%m-%d") ).order_by('updated_on')
        else:
            qs = Scholarship.objects.all().exclude(deadline__gte = datetime.datetime.now().strftime("%Y-%m-%d") ).order_by('-deadline')
        paginator = Paginator(qs, PAGE_SIZE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        

    except Scholarship.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    serializer = ScholarshipSerializer(page_obj,many = True)
    context = {
        "count" : qs.count(),
        "results" : serializer.data
    }
    return Response(context) 


""" @api_view(['GET',])
def api_category_list_scholarship(request,category):
    try:
        sort = request.GET.get('sort')
        sch = Scholarship.objects.all()
        if sort:
            qs = sch.filter(category__icontains=category).filter(deadline__gte = datetime.datetime.now().strftime("%Y-%m-%d") ).order_by('-updated_on')
        else:
            qs = sch.filter(category__icontains=category).filter(deadline__gte = datetime.datetime.now().strftime("%Y-%m-%d") ).order_by('deadline')
        paginator = Paginator(qs, PAGE_SIZE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    except Scholarship.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    serializer = ScholarshipSerializer(page_obj,many = True)
    context = {
        "count" : qs.count(),
        "results" : serializer.data
    }
    return Response(context) """


@api_view(['GET',])
def api_search_scholarship(request):
    '''search.q=search item , sort=True to sort by updated_on'''
    try:
        sort = request.GET.get('sort')
        q = request.GET.get('q')
        sch = Scholarship.objects.all()
        if sort:
            qs = sch.filter(title__icontains=q).filter(deadline__gte = datetime.datetime.now().strftime("%Y-%m-%d") ).order_by('-updated_on')
        else:
            qs = sch.filter(title__icontains=q).filter(deadline__gte = datetime.datetime.now().strftime("%Y-%m-%d") ).order_by('deadline')
        paginator = Paginator(qs, PAGE_SIZE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    except Scholarship.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    serializer = ScholarshipSerializer(page_obj,many = True)
    context = {
        "count" : qs.count(),
        "results" : serializer.data
    }
    return Response(context) 

@api_view(['GET'])
def form_fields(request):
    state = StateSerializer(State.objects.all(),many = True)
    course = CourseSerializer(Course.objects.all(),many = True)
    religion = ReligionSerializer(Religion.objects.all(),many = True)
    sclass = ClassSerializer(Class.objects.all(),many=True)
    country = CountrySerializer(Country.objects.all(),many = True)
    gender = GenderSerializer(Gender.objects.all(),many = True )
    stype = TypeSerializer(Type.objects.all(),many = True)
    category = CategorySerializer(Category.objects.all(),many = True)

    data = {
        'state':state.data,
        'course':course.data,
        'religion':religion.data,
        'class':sclass.data,
        'country':country.data,
        'gender':gender.data,
        'type':stype.data,
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


    


