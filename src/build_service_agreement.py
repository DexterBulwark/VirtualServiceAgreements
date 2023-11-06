from datetime import datetime
import json


def build_service_agreement(agreement_base: str, additonal_info: list = None):
    """
    Build the service agreement from infomation collected
    """

    # Tabs are formated properly in the response. \n in used to indicate a new line. This should be accesptable for the json
    final_service_agreement = """    The service agreement will be finalized here. This is a test to see how much formatiing I can do with this. I want to make sure that I can get this to work. 

        I want to see if it will keep indents and new lines.
    """

    if additonal_info:
        final_service_agreement += ": "
        for info in additonal_info:
            final_service_agreement += " ".format(info)

    return final_service_agreement


# Define your function that generates the JSON data
def jsonify_agreement(agreement: str):
    agreement_data = {
        "agreement": agreement,
        "customer": None,
        "signature": None,  # This will be a base64 encoded image
        "timestamps": {
            "createdOn": datetime.utcnow().isoformat(),
            "openedOn": None,
            "signatureFields": {
                "checkbox": None,
                "initial": None,
                "signature": None,
            },
            "completedAt": None,
        },
    }
    return agreement_data  # Return the actual data, not the JSON string
