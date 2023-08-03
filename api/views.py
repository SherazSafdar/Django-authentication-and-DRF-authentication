from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
#tokenwise
#from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
#from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
#jwt
#from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

#token wise
#@api_view(['GET'])
#@authentication_classes([TokenAuthentication])
#@permission_classes([IsAuthenticated])
#def secure_view(request):
    # Your code for the authenticated view goes here
    #return Response({'message': 'This is a secure view.'})
#class MySecuredView(APIView):
#    authentication_classes = [JWTAuthentication]
#    permission_classes = [IsAuthenticated]

#    def get(self, request):
#        data = {'message': 'This data can only be accessed by authenticated users.'}
#        return Response(data)
#@api_view(['POST'])
#def obtain_auth_token(request):
#    username = request.data.get('username')
#    password = request.data.get('password')
#    user = authenticate(username=username, password=password)

#    if user:
#        token, created = Token.objects.get_or_create(user=user)
#        return Response({'token': token.key})
#    else:
#        return Response({'error': 'Invalid credentials'}, status=400)


#jwt
class MySecuredView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = {'message': 'This data can only be accessed by authenticated users.'}
        return Response(data)


@api_view(['GET', 'POST'])
def user_list(request):
    if request.method=='GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request,pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=404)
    
    if request.method=='GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method=='DELETE':
        user.delete()
        return Response(status=204)
    
        
