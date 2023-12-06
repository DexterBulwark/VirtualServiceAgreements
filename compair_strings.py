import string


def normalize_string(s):
    # Convert to lowercase and remove punctuation
    return s.lower().translate(str.maketrans("", "", string.punctuation))


def tokenize(s):
    # Split the string into words/tokens
    return s.split()


def jaccard_similarity(str1, str2):
    # Create sets of tokens
    set1 = set(tokenize(normalize_string(str1)))
    set2 = set(tokenize(normalize_string(str2)))

    # Calculate intersection and union
    intersection = set1.intersection(set2)
    union = set1.union(set2)

    # Compute Jaccard similarity
    return len(intersection) / len(union)


def compare_strings(strings, reference_string):
    n = len(strings)
    count = 0
    # Iterate through each string and compare it to the reference string
    for i in range(n):
        count += 1
        similarity = jaccard_similarity(strings[i], reference_string)
        # Display only the first 20 characters of each string
        short_str = strings[i][:20] + "..." if len(strings[i]) > 20 else strings[i]
        print(
            f'{count}: Similarity between "{short_str}" and reference: {similarity:.2%}'
        )


# Example usage
list_of_strings = [
    "Customer waives any claims for personal injury and/or property damages related to the Services BULWARK performs under this Agreement. Customer agrees that BULWARK shall not be responsible for any damage to Customer's premises while treating their structures, including any damage to shrubs, trees, or plants. The Services performed by BULWARK may include drilling into soil, through concrete or the structure itself. Customer agrees that BULWARK shall not be responsible for any damage to Customer's premises as a result of drilling, including but not limited to damage caused to plumbing or electrical pipes, wires, or conduits. To avoid potential damage, customer is advised to use a utility locating service to identify the location of the utility lines in or near the structures prior to BULWARK'S Services. When performing the Services, it may be necessary for Customer to remove floor coverings, floors, excavate crawl spaces and provide access to walls, ceilings, or floors. Customer shall be responsible for the cost of dismantling and reconstruction of any item required in order to provide adequate access for providing Services. Customer acknowledges that modifications or alterations to the structure during this agreement may void this Retreatment Guarantee. Customer is advised to notify BULWARK in advance to determine whether such modifications or alterations will void the Retreatment Guarantee or if additional Services will be required at an additional cost to the Customer in order to validate the Retreatment Guarantee. Customer expressly waives and releases BULWARK from and against any claims for (a) loss of use or diminution of property value, (b) economic, compensatory, incidental, or consequential damages and/or (c) exemplary or punitive damages. Customer further agrees that under no circumstances shall BULWARK be liable for any amount greater than the amount paid by Customer to BULWARK for the Services performed.",
    "Customer waives any claims for personal injury and/or property damages related to the Services BULWARK performs under this Agreement. Customer agrees that BULWARK shall not be responsible for any damage to Customer's premises while treating their structures, including any damage to shrubs, trees, or plants. The Services performed by BULWARK may include drilling into soil, through concrete or the structure itself. Customer agrees that BULWARK shall not be responsible for any damage to Customer's premises as a result of drilling, including but not limited to damage caused to plumbing or electrical pipes, wires, or conduits. To avoid potential damage, customer is advised to use a utility locating service to identify the location of the utility lines in or near the structures prior to BULWARK'S Services. When performing the Services, it may be necessary for Customer to remove floor coverings, floors, excavate crawl spaces and provide access to walls, ceilings, or floors. Customer shall be responsible for the cost of dismantling and reconstruction of any item required in order to provide adequate access for providing Services. Customer acknowledges that modifications or alterations to the structure during this agreement may void this Retreatment Guarantee. Customer is advised to notify BULWARK in advance to determine whether such modifications or alterations will void the Retreatment Guarantee or if additional Services will be required at an additional cost to the Customer in order to validate the Retreatment Guarantee. Customer expressly waives and releases BULWARK from and against any claims for (a) loss of use or diminution of property value, (b) economic, compensatory, incidental, or consequential damages and/or (c) exemplary or punitive damages. Customer further agrees that under no circumstances shall BULWARK be liable for any amount greater than the amount paid by Customer to BULWARK for the Services performed.",
]
reference_string = "Customer waives any claims for personal injury and/or property damages related to the Services BULWARK performs under this Agreement. Customer agrees that BULWARK shall not be responsible for any damage to Customer's premises while treating their structures, including any damage to shrubs, trees, or plants. The Services performed by BULWARK may include drilling into soil, through concrete or the structure itself. Customer agrees that BULWARK shall not be responsible for any damage to Customer's premises as a result of drilling, including but not limited to damage caused to plumbing or electrical pipes, wires, or conduits. To avoid potential damage, customer is advised to use a utility locating service to identify the location of the utility lines in or near the structures prior to BULWARK'S Services. When performing the Services, it may be necessary for Customer to remove floor coverings, floors, excavate crawl spaces and provide access to walls, ceilings, or floors. Customer shall be responsible for the cost of dismantling and reconstruction of any item required in order to provide adequate access for providing Services. Customer acknowledges that modifications or alterations to the structure during this agreement may void this Retreatment Guarantee. Customer is advised to notify BULWARK in advance to determine whether such modifications or alterations will void the Retreatment Guarantee or if additional Services will be required at an additional cost to the Customer in order to validate the Retreatment Guarantee. Customer expressly waives and releases BULWARK from and against any claims for (a) loss of use or diminution of property value, (b) economic, compensatory, incidental, or consequential damages and/or (c) exemplary or punitive damages. Customer further agrees that under no circumstances shall BULWARK be liable for any amount greater than the amount paid by Customer to BULWARK for the Services performed."
compare_strings(list_of_strings, reference_string)
