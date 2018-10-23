import datetime
import json
import urllib

from multicorn import ForeignDataWrapper
from multicorn.utils import log_to_postgres


class KiwiComSearch(ForeignDataWrapper):

    def __init__(self, options, columns):
        super(KiwiComSearch, self).__init__(options, columns)
        self.columns = columns

    def format_url(self, cols):
        param_map = {
            '_flyfrom': 'flyFrom',
            '_to': 'to',
            '_datefrom': 'dateFrom',
            '_dateto': 'dateTo',
            '_returnfrom': 'returnFrom',
            '_returnto': 'returnTo',
            '_passengers': 'passengers',
            '_typeflight': 'typeFlight'
        }
        all_params = []
        for col, value in cols.items():
            if type(value) == datetime.datetime:
                value = value.strftime('%d/%m/%Y')
            all_params.append('{}={}'.format(param_map[col], value))

        param_slug = '&'.join(all_params)
        base_url = 'http://api.skypicker.com/flights?v=2&limit=50&'

        return base_url + param_slug

    def filter_req_cols(self, quals):
        # TODO only supports X = Y, add LT GT BETWEEN
        req_cols = {}
        for qual in quals:
            if qual.field_name.startswith('_'):
                req_cols[qual.field_name] = qual.value

        return req_cols

    def get_flights(self, url):
        log_to_postgres(url)
        return json.load(urllib.urlopen(url))

    def execute(self, quals, columns):
        log_to_postgres('quals: {}\ncolumns: {}'.format(quals, columns))
        # TODO sanity check on underscore (request) params
        req_cols = self.filter_req_cols(quals)
        url = self.format_url(req_cols)
        resp_json = self.get_flights(url)
        log_to_postgres(json.dumps(resp_json, indent=2))
