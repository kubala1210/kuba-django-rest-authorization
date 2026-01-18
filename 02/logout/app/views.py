from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

# Uzasadnienie decyzji projektowych:

# Permission Class (IsAuthenticated): Wymagamy zalogowania, ponieważ wylogowanie jest akcją autoryzowanego użytkownika. Zapobiega to próbom spamowania endpointu przez anonimowe podmioty, choć technicznie sama metoda .blacklist() sprawdza poprawność tokena.

# Kod statusu 205 Reset Content: Jest to semantycznie najtrafniejszy kod dla wylogowania. Informuje klienta, że żądanie zostało przetworzone pomyślnie i powinien on "zresetować" widok (np. usunąć tokeny z local storage). Alternatywnie 200 OK również jest poprawne, ale mniej precyzyjne.

# Błędy (400 Bad Request): Jeśli pole refresh jest puste, nieobecne lub token jest nieprawidłowy/już unieważniony, zwracamy 400, ponieważ żądanie klienta jest błędne.
