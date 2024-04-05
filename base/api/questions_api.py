import allure
from httpx import Response

from models.questions import DefaultQuestion, UpdateQuestion
from utilities.clients.http.client import APIClient
from utilities.constans.routes import APIRoutes


class QuestionsClient(APIClient):
    @allure.step(f'Getting all questions')
    def get_questions_api(self) -> Response:
        return self.client.get(APIRoutes.QUESTIONS)