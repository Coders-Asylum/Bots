from json import dumps


class Message:
    http_body_empty: str = dumps({"message": "Request Body Empty."})
    http_body_incorrect: str = dumps({"message": "Request body incorrect."})
    http_body_semantic_error: str = dumps({"message": "Semantic Error in body, hence the request is not processable."})

    no_processing_required: str = dumps({'message': 'Current payload does not require any processing'})
    __dash_seperator: str = '-----------------------------------------------------'

    @property
    def seperator(self, sep_type: str = 'dash') -> str:
        """ Returns a seperator string.

        Args:
            sep_type (str): type of seperator (default=dash)

        Returns: string

        """
        if sep_type == 'dash':
            return self.__dash_seperator
        else:
            return self.__dash_seperator


class Status:
    __program_error: dict = {"status_code": 500, "status": 'Internal server Error'}

    @property
    def program_error(self) -> dict:
        return self.__program_error


class BotConfig:
    __repo_name: str = 'Bots'
    __repo_owner_name: str = 'Coders-Asylum'

    @property
    def repo_name(self) -> str:
        return self.__repo_name

    @property
    def repo_owner(self) -> str:
        return self.__repo_owner_name
