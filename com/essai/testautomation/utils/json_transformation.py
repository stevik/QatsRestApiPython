import jsons


def serialize_json(obj_to_serialize: object):
    if obj_to_serialize is None:
        return None
    try:
        return jsons.dumps(obj_to_serialize)
    except jsons.JsonsError as e:
        raise ValueError("Error during JSON serialization") from e


def deserialize_json(json_str: str, class_type):
    if json_str is None:
        return None
    try:
        return jsons.loads(json_str, class_type)
    except jsons.JsonsError as e:
        raise ValueError("Error during JSON deserialization") from e
