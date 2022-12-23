from django.shortcuts import render
from django.contrib.auth import login
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import *
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
# Create your views here.
from rest_framework import generics, permissions
from rest_framework.response import Response
from django.template import loader  
from knox.models import AuthToken
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .serializers import *
from django.contrib.auth import logout
from . models import *
from django.views.generic.list import ListView
import PyPDF2
import textract
import os
from pathlib import Path
from django.conf import settings
BASE_DIR = Path(__file__).resolve().parent.parent



def TextDisplay(request):
        context = {}
        context ['dataset'] = text.objects.filter(user = request.user)
        return render(request,'display.html',context)

@permission_classes([IsAuthenticated])
@api_view(['GET'])
def converter(request): 

    serializer_class = textSerializer

    pdfpath = pdf.objects.filter(user=request.user).latest('id')
    

    path = pdfpath.pdf.url
    pdfpath =  ((str(settings.BASE_DIR))) 
    pdfpath = pdfpath.replace(os.sep, '/')
    pdfFile = open((pdfpath+'/static'+path),'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    pageObj = pdfReader.getPage(0)
    text = pageObj.extractText()
    pdfFile.close()
    print(pdfpath)
    pdfpath = pdf.objects.filter(user=request.user).latest('id')
    title =  str(pdfpath),
    context = {
        
        "pdf"  :  pdf.objects.filter(user=request.user).latest('id').pk,
        'user' :  request.user.pk,
        'title': title,
        "text" : text,
    }

    serializer = textSerializer(data=context)
    serializer.is_valid(raise_exception=True)
    text = serializer.save()   
  

    return redirect('display')
 


def test(request):
    return render(request,'test.html')

def get_pdf(request):
    return render(request,'login.html')



@permission_classes([IsAuthenticated])
def home(request):
    return render(request,'home.html')


@permission_classes([IsAuthenticated])
class DataApi(viewsets.ModelViewSet):
    serializer_class = DataSerializer
    queryset = pdf.objects.all()
   
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        pdf = serializer.save()
        return redirect(test)

def UserLoggedIn(request):
    if request.user.is_authenticated == True:
        username = request.user.username
    else:
        username = None
    return username

def logout_view(request):
    username = UserLoggedIn(request)
    if username != None:
        logout(request)
    return redirect(get_pdf)
    




# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })



class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        context = {
            'user': user.username
        }
        return redirect(home)
        # return super(LoginAPI, self).post(request, format=None)


