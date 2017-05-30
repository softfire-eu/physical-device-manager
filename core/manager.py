from sdk.softfire.manager import AbstractManager


class PDManager(AbstractManager):
    def refresh_resources(self, user_info) -> list:
        pass

    def validate_resources(self, user_info=None, payload=None) -> None:
        pass

    def release_resources(self, user_info, payload=None) -> None:
        pass

    def create_user(self, username, password):
        pass

    def list_resources(self, user_info=None, payload=None) -> list:
        pass

    def provide_resources(self, user_info, payload=None) -> list:
        pass