from datetime import datetime, timedelta
import requests

# ===== [URL] ===== #
base_url = 'https://lldev.thespacedevs.com'
# Get info about
launch = '/2.2.0/launch/'
# Compose
launch_url = base_url+launch


# ===== [FILTERS & MORE] ===== #
now = datetime.now()
month_ago = now - timedelta(days=31)
next_month = now + timedelta(days=31)

net_filters = f'net__gte={now.isoformat()}&net__lte={next_month.isoformat()}'
lsp_filter = 'lsp__name=SpaceX'
orbital_filter = 'include_suborbital=false'

filters = '&'.join((net_filters, lsp_filter, orbital_filter))

# normal, list or detailed
mode = 'mode=list'

# Limit returned results to just 2 per query
limit = 'limit=5'

# Ordering the results by ? (NET)
ordering = 'ordering=net'


# ===== [QUERY URL] ===== #
query_url = launch_url + '?' + '&'.join(
    (filters, mode, limit, ordering)
)
print(f'query URL: {query_url}')


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

# Checking if it was succesful
if not results:
    # Quitting the program as an example
    # use your own error handling here
    quit()

# Printing resulting dictionary
print(results)

# Paginating through all the results
next_url = results['next']
while next_url:
    # Requesting next data
    next_results = get_results(next_url)

    # Checking if it was succesful
    if not results:
        # Quitting the program as an example
        # use your own error handling here
        quit()

    # Printing next results
    print(next_results)
    
    # Adding to the original results dictionary
    results['results'] += next_results['results']

    # Updating the next URL
    next_url = next_results['next']

print('Done!')