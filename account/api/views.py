from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.authentication import BasicAuthentication,TokenAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,DjangoModelPermissions
from rest_framework import status,generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.parsers import *
from account.api.serializers import RegistrationSerializer ,LoginSerializer,ProfileSerializer
from account.models import Profile
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.decorators import api_view, authentication_classes, permission_classes






####Registration#####
@api_view(['POST',])
@authentication_classes(())
@permission_classes(())
def registration_view(request):
    if request.method=='POST':
        serializer = RegistrationSerializer(data=request.data)
        data ={}
        if serializer.is_valid():
            User = serializer.save()

            #Profile.objects.create(user=User)
            data['response']="OK. registered."

            data['address']=User.profile.address
            data['username']=User.username
            return Response(data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

####User details,update or delete#######
@api_view(['GET','PUT','DELETE'])
@authentication_classes((SessionAuthentication, TokenAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def api_user_details(request):

    try:
        user=User.objects.get(pk=request.user.id)

    except User.DoesNotExist :
        content ="User Does Not Exist !!"
        return Response(content)
    if request.method=='GET':
            if request.user.id:
                serializer=LoginSerializer(user)
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                content="Token Error!!!"
                return Response(content)
    elif request.method=='PUT':
            if request.user.id:
                serializer=LoginSerializer(user,data=request.data)
                if serializer.is_valid():
                      if ('password' in request.data):
                          password = make_password(request.data['password'])
                          serializer.save(password=password)
                      else:
                          serializer.save()

                      return Response(serializer.data)
                else:
                    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            else:
                content="Token Error!!!"
                return Response(content)
    #elif request.method=='DELETE':
            #if request.user.id:
                #user.delete()
                #return Response(status=status.HTTP_204_NO_CONTENT)
            #else:
                #content="Token Error!!!"
                #return Response(content)

####Profile details or update##########
@api_view(['GET','PUT'])
@authentication_classes((SessionAuthentication, TokenAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def api_profile_details(request):
    try:
        prof=Profile.objects.get(pk=request.user.profile.id)
    except Profile.DoesNotExist:
        content ="Profile Does Not Exist !!"
        return Response(content)
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
            if request.user.profile.id:
                serializer=ProfileSerializer(prof)
                return Response(serializer.data)
            else:
                content="Error Token"
                return Response(content)
    elif request.method=='PUT':
            serializer=ProfileSerializer(prof,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
