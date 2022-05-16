from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status, permissions

from .models import Address, Bank, CustomUser, Experience, PersonalDetails, Qualification
from .serializers import AadharSerializer, AddressSerializer, BankSerializer, ExperienceSerializer, LoginSerializer, PersonalDetailsSerializer, QualificationSerializer, RegisterSerializer


class IsManager(permissions.BasePermission):
    message = 'Only Managers can edit data. '

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.is_manager



class RegisterAPI(APIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny, ]
    
    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        token = Token.objects.create(user=user)
        return Response({'Success':'Your account is successfully created.'},status=status.HTTP_201_CREATED)


class LoginAPI(APIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny, ]
    
    def post(self,request):
        email = request.data.get('email',None)
        password = request.data.get('password',None)
        user = authenticate(email = email, password = password)
        if user :
            serializer = self.serializer_class(user)
            token = Token.objects.get(user=user)
            return Response({'token' : token.key,'email' : user.email},status = status.HTTP_200_OK)
        return Response('Invalid Credentials',status = status.HTTP_404_NOT_FOUND)


class AadharAPI(APIView):

    serializer_class = AadharSerializer

    def post(self,request):
        return Response({'trial' : "demo"},status = status.HTTP_200_OK)


class QualificationListCreateAPI(APIView):

    serializer_class = QualificationSerializer
    query_set = Qualification.objects.all()

    def get(self,request):
        queryset = self.query_set
        serializer = self.serializer_class(queryset, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


class QualificationRetrieveUpdateDestroy(APIView):

    serializer_class = QualificationSerializer

    def get(self,request,pk):
        user = CustomUser.objects.get(id = pk)
        try:
            object = Qualification.objects.get(user = user)
            serializer = self.serializer_class(object)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'detail' : "No data for this user."}, status=status.HTTP_404_NOT_FOUND)

    def put(self,request,pk):
        user = CustomUser.objects.get(id = pk)
        object = Qualification.objects.get(user = user)
        serializer = self.serializer_class(object, data = request.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self,request,pk):
        user = CustomUser.objects.get(id = pk)
        object = Qualification.objects.get(user = user)
        object.delete()
        return Response({'detail' : "Deleted"}, status=status.HTTP_202_ACCEPTED)


class AddressListCreateAPI(APIView):

    serializer_class = AddressSerializer
    query_set = Address.objects.all()

    def get(self,request):
        queryset = self.query_set
        serializer = self.serializer_class(queryset, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


class AddressRetrieveUpdateDestroy(APIView):

    serializer_class = AddressSerializer

    def get(self,request,pk):
        try:
            user = CustomUser.objects.get(pk =pk)
            object = Address.objects.get(user = user)
            serializer = self.serializer_class(object)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'detail' : "No data for this user."}, status=status.HTTP_404_NOT_FOUND)

    def put(self,request,pk):
        user = CustomUser.objects.get(pk =pk)
        object = Address.objects.get(user = user)
        serializer = self.serializer_class(object, data = request.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self,request,pk):
        user = CustomUser.objects.get(pk =pk)
        object = Address.objects.get(user = user)
        object.delete()
        return Response({'detail' : "Deleted"}, status=status.HTTP_202_ACCEPTED)


class BankListCreateAPI(APIView):

    serializer_class = BankSerializer
    query_set = Bank.objects.all()

    def get(self,request):
        queryset = self.query_set
        serializer = self.serializer_class(queryset, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


class BankRetrieveUpdateDestroy(APIView):

    serializer_class = BankSerializer

    def get(self,request,pk):
        try:
            user = CustomUser.objects.get(pk=pk)
            object = Bank.objects.get(user=user)
            serializer = self.serializer_class(object)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'detail' : "No data for this user."}, status=status.HTTP_404_NOT_FOUND)

    def put(self,request,pk):
        user = CustomUser.objects.get(pk=pk)
        object = Bank.objects.get(user=user)
        serializer = self.serializer_class(object, data = request.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self,request,pk):
        user = CustomUser.objects.get(pk=pk)
        object = Bank.objects.get(user=user)
        object.delete()
        return Response({'detail' : "Deleted"}, status=status.HTTP_202_ACCEPTED)


class ExperienceListCreateAPI(APIView):

    serializer_class = ExperienceSerializer
    query_set = Experience.objects.all()

    def get(self,request):
        queryset = self.query_set
        serializer = self.serializer_class(queryset, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


class ExperienceRetrieveUpdateDestroy(APIView):

    serializer_class = ExperienceSerializer

    def get(self,request,pk):
        try:
            user = CustomUser.objects.get(pk=pk)
            object = Experience.objects.get(user=user)
            serializer = self.serializer_class(object)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'detail' : "No data for this user."}, status=status.HTTP_404_NOT_FOUND)

    def put(self,request,pk):
        user = CustomUser.objects.get(pk=pk)
        object = Experience.objects.get(user=user)
        serializer = self.serializer_class(object, data = request.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self,request,pk):
        user = CustomUser.objects.get(pk=pk)
        object = Experience.objects.get(user=user)
        object.delete()
        return Response({'detail' : "Deleted"}, status=status.HTTP_202_ACCEPTED)


class PersonalDetailsListCreateAPI(APIView):

    serializer_class = PersonalDetailsSerializer
    query_set = PersonalDetails.objects.all()

    def get(self,request):
        queryset = self.query_set
        serializer = PersonalDetailsSerializer(queryset, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = PersonalDetailsSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


class PersonalDetailsRetrieveUpdateDestroy(APIView):

    serializer_class = PersonalDetailsSerializer

    def get(self,request,pk):
        try:
            user = CustomUser.objects.get(pk=pk)
            object = PersonalDetails.objects.get(user=user)
            serializer = self.serializer_class(object)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'detail' : "No data for this user."}, status=status.HTTP_404_NOT_FOUND)

    def put(self,request,pk):
        user = CustomUser.objects.get(pk=pk)
        object = PersonalDetails.objects.get(user=user)
        serializer = self.serializer_class(object, data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def delete(self,request,pk):
        user = CustomUser.objects.get(pk=pk)
        object = PersonalDetails.objects.get(user=user)
        object.delete()
        return Response({'detail' : "Deleted"}, status=status.HTTP_202_ACCEPTED)