from com.essai.testautomation.reqresapi.main.model.rest.postuser.user_request import UserRequest


def create_post_user_request(name: str, job: str):
    return UserRequest(name, job)
