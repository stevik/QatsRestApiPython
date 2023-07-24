import pytest

from com.essai.testautomation.reqresapi.main.helpers.post_user_request_helper import create_post_user_request
from com.essai.testautomation.reqresapi.main.teststeps.rest_teststeps import get_users_request
from com.essai.testautomation.reqresapi.main.teststeps.rest_teststeps import post_user_request
from com.essai.testautomation.reqresapi.main.teststeps.rest_teststeps import verify_post_user_response
from com.essai.testautomation.reqresapi.main.teststeps.rest_teststeps import verify_users_response
from com.essai.testautomation.utils.csv_utils import read_csv


class TestReqResApi:

    def test_get_users_page_2(self):
        # prepare
        expected_total = 12
        expected_last_names = {7: "Lawson", 8: "Ferguson"}

        # execute
        response = get_users_request(2)

        # verify
        verify_users_response(response, expected_total, expected_last_names)

    @pytest.mark.parametrize("name,job", read_csv("new_users.csv", True, ";"))
    def test_post_user(self, name, job):
        # prepare
        user_req = create_post_user_request(name, job)

        # execute
        response = post_user_request(user_req, 2000)

        # verify
        verify_post_user_response(user_req, response)
