from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class Calculate(APIView):
    def post(self, request):
        try:
            operation = request.data["operation"]
            firstValue = request.data["firstValue"]
            SecondValue = request.data["SecondValue"]

            if (operation == "addition"):
                data = firstValue + SecondValue
                return Response(data=data, status=status.HTTP_200_OK)
            if (operation == "subtraction"):
                data = firstValue - SecondValue
                return Response(data=data, status=status.HTTP_200_OK)
            if (operation == "multiplication"):
                data = firstValue * SecondValue
                return Response(data=data, status=status.HTTP_200_OK)

            return Response({"message": "Bad request"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            return Response({"message": "Server error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
