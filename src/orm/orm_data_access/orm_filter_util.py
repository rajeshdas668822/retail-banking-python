class DynamicFilter:

    def __init__(self, session=None, query=None, model_class=None, filter_condition=None):
        # super().__init__(*args, **kwargs)
        self.query = query
        self.model_class = model_class
        self.filter_condition = filter_condition
        self.session = session

    def get_query(self):
        '''
        Returns query with all the objects
        :return:
        '''
        if not self.query:
            self.query = self.session.query(self.model_class)
        return self.query

    def filter_query(self, query, filter_condition):
        '''
        Return filtered queryset based on condition.
        :param query: takes query
        :param filter_condition: Its a list, ie: [(key,operator,value)]
        operator list:
            eq for ==
            lt for <
            ge for >=
            in for in_
            like for like
            value could be list or a string
        :return: queryset

        '''

        if query is None:
            query = self.get_query()
        model_class = self.model_class  # returns the query's Model
        for raw in filter_condition:
            try:
                key, op, value = raw
            except ValueError:
                raise Exception('Invalid filter: %s' % raw)
            column = getattr(model_class, key, None)
            if not column:
                raise Exception('Invalid filter column: %s' % key)
            if op == 'in':
                if isinstance(value, list):
                    filt = column.in_(value)
                else:
                    filt = column.in_(value.split(','))
            else:
                try:
                    attr = list(filter(
                        lambda e: hasattr(column, e % op),
                        ['%s', '%s_', '__%s__']
                    ))[0] % op
                except IndexError:
                    raise Exception('Invalid filter operator: %s' % op)
                if value == 'null':
                    value = None
                filt = getattr(column, attr)(value)
            query = query.filter(filt)
        return query

    def return_query(self):
        return self.filter_query(self.get_query(), self.filter_condition)


class FilterSpecification:
    filters = None
    order_by = None

    def __init__(self, filters, order_by=[]):
        self.filters = filters
        self.order_by = order_by

    def get_filters(self):
        return self.filters

    def get_order_by(self):
        return self.order_by
