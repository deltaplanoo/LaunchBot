import requests

# TEST QUERY
query_url = "https://lldev.thespacedevs.com/2.2.0/launch/?net__gte=2023-10-22T12:10:42.168983&net__lte=2023-11-22T12:10:42.168983&lsp__name=SpaceX&include_suborbital=false&mode=list&limit=2&ordering=-net"


def get_results(query_url: str) -> dict or None:
    # This script prints exceptions instead of raising them as this is script is only meant as a tutorial.
    try:
        # Requesting data
        results = requests.get(query_url)
    except Exception as e:
        # Print exception when it occurs
        print(f'Exception: {e}')
    else:
        # Checking status of the query
        status = results.status_code
        print(f'Status code: {status}')

        # Return when the query status isn't 200 OK
        # See: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
        if status != 200:
            return

        # Converting to JSON and returning
        return results.json()

# Perform first query
results = get_results(query_url)
