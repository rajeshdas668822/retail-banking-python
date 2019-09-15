class ResultHelper:

    @classmethod
    def resultproxy_to_dict_list(cls, sql_alchemy_rowset):
        # return [{tuple[0]: tuple[1] for tuple in rowproxy.items()}
        #         for rowproxy in sql_alchemy_rowset]

        return [{column: value for column, value in rowproxy.items()} for rowproxy in sql_alchemy_rowset]
