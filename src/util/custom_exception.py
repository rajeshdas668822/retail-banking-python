class InsufficientBalance(Exception):
    """ Raise When balance is not sufficient to owner the withdrawal request"""


class EmptyData(Exception):
    """ Data is None or Empty"""


pass


class BadLoadFormat(Exception):
    pass


class BadSpec(Exception):
    pass


class FieldNotFound(Exception):
    pass


class BadQuery(Exception):
    pass


class InvalidPage(Exception):
    pass


class BadFilterFormat(Exception):
    pass
