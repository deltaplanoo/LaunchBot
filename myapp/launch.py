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
future = now + timedelta(days=90)

net_filters = f'net__gte={now.isoformat()}&net__lte={future.isoformat()}'
# lsp_filter = 'lsp__name=SpaceX'
orbital_filter = 'include_suborbital=false'

filters = '&'.join((net_filters, orbital_filter))

# normal, list or detailed
mode = 'mode=list'

# Limit returned results to just 2 per query
limit = 'limit=10'

# Ordering the results by ? (NET)
ordering = 'ordering=net'


# ===== [QUERY URL] ===== #
query_url = launch_url + '?' + '&'.join(
    (filters, mode, limit, ordering)
)

def split_datetime(data):
    for launch in data['results']:
        launch['date'] = launch['net'][:10]
        launch['time'] = launch['net'][11:19]
        # Move 'date' and 'time' after 'net'
        launch['net'] = {'date': launch['date'], 'time': launch['time']}
        launch.pop('date', None)
        launch.pop('time', None)

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
split_datetime(results)