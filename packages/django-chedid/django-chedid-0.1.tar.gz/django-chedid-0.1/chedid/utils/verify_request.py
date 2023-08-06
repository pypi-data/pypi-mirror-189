def verify_request(labels: dict, request: dict) -> list:
    """
    This function verify if request contains all labels, requireds and optionals, and if his type is correctly

    :param labels:
        label_name: str
        type: cls
        required: bool

        dict: {
        label_name: (type, required),
        }

    :param request:
        dict, request from user

    :return fails: list<str>:
    """

    fails = []

    for label in labels.keys():
        if label in request.keys():
            if type(request.get(label)) != labels[label][0]:
                fails.append(f"The type of '{label}' is incorrect;")

        elif labels[label][1]:
            fails.append(f"'{label}' is missing;")

    return fails
