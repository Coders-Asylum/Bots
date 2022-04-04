from json import dumps


class Message:
    http_body_empty: str = dumps({"message": "Request Body Empty."})
    http_body_incorrect: str = dumps({"message": "Request body incorrect."})
    http_body_semantic_error: str = dumps({"message": "Semantic Error in body, hence the request is not processable."})

    no_processing_required: str = dumps({'message': 'Current payload does not require any processing'})
