from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import ClassDetailsSerializer
from .models import ClassDetails


# Create your views here.

class ClassLayoutList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        class_details = ClassDetails.objects.all()
        serializer = ClassDetailsSerializer(class_details, many=True)

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

    def post(self, request, pk):
        class_details = ClassDetails.objects.get(id=pk)
        serializer = ClassDetailsSerializer(instance=class_details, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)


class ClassLayoutDelete(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, pk):
        class_details = ClassDetails.objects.get(id=pk)
        class_details.delete()

        return Response('Class layout deleted')
