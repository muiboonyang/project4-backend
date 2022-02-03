from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import PersonalDetailsSerializer
from .models import PersonalDetails


# Create your views here.

class PersonalDetailsAll(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        reviews = PersonalDetails.objects.all()
        serializer = PersonalDetailsSerializer(reviews, many=True)

        return Response(serializer.data)


class PersonalDetailsOne(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        tasks = PersonalDetails.objects.get(id=pk)
        serializer = PersonalDetailsSerializer(tasks, many=False)

        return Response(serializer.data)


class PersonalDetailsCreate(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = PersonalDetailsSerializer(data=request.data)

        # if you dont have this, Django will throw an error saying you have not validated
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        else:
            return Response('Error with creating review')


class PersonalDetailsUpdate(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk):
        personal_details = PersonalDetails.objects.get(id=pk)
        serializer = PersonalDetailsSerializer(instance=personal_details, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)


class PersonalDetailsDelete(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, pk):
        personal_details = PersonalDetails.objects.get(id=pk)
        personal_details.delete()

        return Response('Review deleted')
