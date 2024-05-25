from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .models import CustomUser, Session, Booking
from .serializers import CustomUserSerializer, SessionSerializer, BookingSerializer,CustomUserWithPasswordSerializer
# from rest_framework import generics
# from rest_framework.permissions import IsAdminUser
# from .models import CustomUser
# from .serializers import CustomUserSerializer


class CreateUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]


class CreateSessionView(generics.CreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = [permissions.IsAdminUser]

class ListSessionsView(generics.ListAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserListSessionsView(generics.ListAPIView):
    serializer_class = SessionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        month = self.request.query_params.get('month')
        if month:
            return Session.objects.filter(date__month=month)
        return Session.objects.all()


class BookSessionView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        session_id = request.data.get('session_id')
        user = request.user
        session = Session.objects.get(id=session_id)
        if Booking.objects.filter(session=session).exists():
            return Response({'error': 'Session already booked'}, status=400)
        Booking.objects.create(session=session, user=user)
        return Response({'success': 'Session booked'})

# class CustomAuthToken(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'token': token.key,
#             'user_id': user.pk,
#             'is_admin': user.is_admin,
#         })


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)

            return Response({
                'token': token.key,
                'user_id': user.pk,

            })
        else:
            # Log serializer errors for debugging
            print(serializer.errors)
            return Response(serializer.errors, status=400)

# class CustomUserPasswordListView(generics.ListAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserWithPasswordSerializers
#     permission_classes = [permissions.IsAdminUser]

