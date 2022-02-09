from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import ClassDetailsSerializer
from .models import ClassDetails


# Create your views here.

class ClassLayoutList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        reviews = ClassDetails.objects.all()
        serializer = ClassDetailsSerializer(reviews, many=True)

        return Response(serializer.data)


class ClassLayoutDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        reviews = ClassDetails.objects.get(id=pk)
        serializer = ClassDetailsSerializer(reviews, many=False)

        return Response(serializer.data)


class ClassLayoutCreate(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = ClassDetailsSerializer(data=request.data)

        # if you dont have this, Django will throw an error saying you have not validated
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        else:
            return Response('Error with creating class layout')


class ClassLayoutUpdate(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, fk):
        review = ClassDetails.objects.get(user_id=fk)
        serializer = ClassDetailsSerializer(instance=review, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)


class ClassLayoutDelete(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, pk):
        review = ClassDetails.objects.get(id=pk)
        review.delete()

        return Response('Class layout deleted')
