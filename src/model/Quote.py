from datetime import datetime


class Quote:
    def __init__(self, quote_id, underlying_ref, quote_type, quote_side, ask, bid, mid):
        self._quote_id = quote_id
        self._underlying_ref = underlying_ref
        self._quote_type = quote_type
        self._quote_side = quote_side
        self._ask = ask
        self._bid = bid
        self._mid = mid
        self._quote_date_time = datetime.now()
        self._updated_time = datetime.now()

    def get_quote_id(self):
        return self._quote_id

    def get_underlying_ref(self):
        return self._underlying_ref

    def get_quote_type(self):
        return self._quote_type

    def get_quote_side(self):
        return self._quote_side

    def get_ask(self):
        return self._ask

    def get_bid(self):
        return self._bid

    def get_mid(self):
        return self._mid

    def get_quote_date_time(self):
        return self._quote_date_time

    def get_updated_time(self):
        return self._updated_time
