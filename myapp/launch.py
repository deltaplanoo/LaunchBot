from datetime import datetime, timedelta
import requests

# ===== [URL] ===== #
base_url = 'https://lldev.thespacedevs.com'
launch = '/2.2.0/launch/'
agencies = '/2.2.0/agencies/'
# Compose
launch_url = base_url+launch
agencies_url = base_url+agencies

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
query_launch_url = launch_url + '?' + '&'.join(
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
    try:
        results = requests.get(query_url)
    except Exception as e:
        print(f'Exception: {e}')
    else:
        status = results.status_code
        print(f'Status code: {status}')
        # See: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
        if status != 200:
            return
        return results.json()


results = get_results(query_launch_url)
split_datetime(results)