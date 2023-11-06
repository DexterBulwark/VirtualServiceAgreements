"""
When ran, this file will gather all of the needed information to build a service agreement. It will then send that agreement to the user in json format.
"""

from src import (
    get_info_from_user,
    get_agreement_base,
    get_additional_info,
    build_service_agreement,
    send_agreement,
)

if __name__ == "__main__":
    office, service = get_info_from_user()
    agreement_base = get_agreement_base(office, service)
    additional_info = get_additional_info()
    final_agreement = build_service_agreement(agreement_base, additional_info)
    send_agreement(final_agreement)
