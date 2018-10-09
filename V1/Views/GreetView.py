from rest_framework.response import Response
from rest_framework.views import APIView
from V1.Core.GreetUser import GreetUser



class GreetView(APIView):
    def get(self, request,username):
        """
        Greets you :)

        **Example Response**

                {
                    "Greetings": "string",

                }

        """
        greet = GreetUser(username)
        return Response({
            "Greetings": greet.Greet()

        })