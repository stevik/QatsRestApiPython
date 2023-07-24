from datetime import datetime

from com.essai.testautomation.reqresapi.main.model.rest.getusers.users_response import UsersResponse
from com.essai.testautomation.reqresapi.main.model.rest.postuser.user_request import UserRequest
from com.essai.testautomation.reqresapi.main.model.rest.postuser.user_response import UserResponse
from com.essai.testautomation.reqresapi.main.rest_api_methods import ReqResApi
from com.essai.testautomation.utils.json_transformation import deserialize_json

API = ReqResApi()


def get_users_request(page: int):
    json = API.get_users(page)
    return deserialize_json(json, UsersResponse)


def post_user_request(request: UserRequest, max_resp_time_in_millis: int):
    json = API.post_user(request, max_resp_time_in_millis)
    return deserialize_json(json, UserResponse)


def verify_users_response(actual_response, expected_total_records, expected_names):
    assert actual_response.total == expected_total_records, "total"
    verify_data_of_users_response(actual_response.data, expected_names)
    assert actual_response.per_page == len(actual_response.data), "Size of page"


def verify_data_of_users_response(actual_data, expected_names):
    for db_id, expected_name in expected_names.items():
        matching_items = [item for item in actual_data if item.id == db_id]
        if not matching_items:
            raise ValueError(f"User with id {db_id} was not found")
        actual_name = matching_items[0].last_name
        assert actual_name == expected_name, "LastName"


def verify_post_user_response(request, actual_response):
    expected_year = datetime.now().year
    assert actual_response.name == request.name, "Name"
    assert actual_response.job == request.job, "Job"
    assert actual_response.id is not None, "Id"
    assert actual_response.createdAt.year == expected_year, "Year"
