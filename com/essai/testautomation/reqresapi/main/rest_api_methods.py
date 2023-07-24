import requests

from com.essai.testautomation.reqresapi.main.model.rest.postuser.user_request import UserRequest
from com.essai.testautomation.utils.config_utils import get_property
from com.essai.testautomation.utils.json_transformation import serialize_json

REQRES_API_URL = "/api/users"
PARAM_PAGE = "page"


class ReqResApi:
    def __init__(self):
        self.base_url = get_property("../test/resources/reqresapi.ini", "reqresapi.url")

    def get_users(self, page=1):
        parameters = {PARAM_PAGE: page}
        response = requests.get(f'{self.base_url}{REQRES_API_URL}', params=parameters)
        assert response.status_code == 200, f'Bad response code: {response.status_code}'
        return response.text

    def post_user(self, request: UserRequest, max_resp_time_in_millis: int):
        headers = {'Content-Type': 'application/json'}
        req_as_json = serialize_json(request)
        response = requests.post(f'{self.base_url}{REQRES_API_URL}', data=req_as_json, headers=headers)

        elapsed_milliseconds = response.elapsed.total_seconds() * 1000
        assert response.status_code == 201, f'Bad response code: {response.status_code}'
        assert elapsed_milliseconds <= max_resp_time_in_millis, \
            f"Response time {elapsed_milliseconds} exceeded {max_resp_time_in_millis} milliseconds."

        return response.text
