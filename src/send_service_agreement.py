"""
This file is used to send the service agreement to the user in json format
"""
from datetime import datetime
import json


def send_agreement(agreement: str):
    """
    Send the agreement to the user
    """

    # All None data needs to be filled in before it is returned
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

    # Use json.dumps to convert the dictionary to a JSON string
    json_agreement = json.dumps(agreement_data, indent=4)
    print(json_agreement)
