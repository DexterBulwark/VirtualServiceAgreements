def get_info_from_user():
    """
    Get the user's location and service manually
    """
    office = input("What office are you in? ")
    service = input("What service is being provided? ")
    return office, service


def get_agreement_base(office: str, service: str):
    """
    Get the agreement from the user based on location and service
    """
    agreement_base = "The service agreement for {} in {} will be finalized here".format(
        service, office
    )
    return agreement_base


def get_additional_info():
    additional_info = []
    while True:
        additional_info.append(input("What additional information is needed? "))
        if input("Is there more information needed? (y/n) ") == "n":
            break
    return additional_info
