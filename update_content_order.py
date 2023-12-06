""" 
This will return a query to update the service agreement content order
"""


def increment(current_location, desired_location):
    """
    Args:
        current_location (int): The current location of the content
        desired_location (int): The desired location of the content

    Returns:
        str: The query to update the content order
    """
    return f"""
UPDATE Tempest.dbo.ServiceAgreementFinePrintContentOrder
SET ContentOrder = 0
WHERE ContentOrder = {current_location};

UPDATE Tempest.dbo.ServiceAgreementFinePrintContentOrder
SET ContentOrder = ContentOrder + 1
WHERE ContentOrder BETWEEN {desired_location} AND {current_location - 1};

UPDATE Tempest.dbo.ServiceAgreementFinePrintContentOrder
SET ContentOrder = {desired_location}
WHERE ContentOrder = 0;
"""


def decrement(current_location, desired_location):
    """
    Args:
        current_location (int): The current location of the content
        desired_location (int): The desired location of the content

    Returns:
        str: The query to update the content order
    """
    return f"""
UPDATE Tempest.dbo.ServiceAgreementFinePrintContentOrder
SET ContentOrder = 0
WHERE ContentOrder = {current_location};

UPDATE Tempest.dbo.ServiceAgreementFinePrintContentOrder
SET ContentOrder = ContentOrder - 1
WHERE ContentOrder BETWEEN {current_location + 1} AND {desired_location};

UPDATE Tempest.dbo.ServiceAgreementFinePrintContentOrder
SET ContentOrder = {desired_location}
WHERE ContentOrder = 0;
"""


def update_content_order(current_location, desired_location):
    """
    Args:
        current_location (int): The current location of the content
        desired_location (int): The desired location of the content

    Returns:
        None: Prints the query to update the content order to the terminal here to maintain the integrity of the query
    """
    select_query = f"""
SELECT ct.Title
,ContentOrder
FROM Tempest.dbo.ServiceAgreementFinePrintContentOrder co 
LEFT JOIN Tempest.dbo.ServiceAgreementFinePrintContentTitle ct 
ON co.ServiceAgreementFinePrintContentTitle_Id = ct.Id
ORDER BY ContentOrder
"""
    if current_location > desired_location:
        print(
            increment(current_location, desired_location),
            select_query,
        )
    elif current_location < desired_location:
        print(decrement(current_location, desired_location), select_query)
    else:
        print("The content is already in the desired location")


if __name__ == "__main__":
    # (current_location, desired_location)
    update_content_order(12, 9)
