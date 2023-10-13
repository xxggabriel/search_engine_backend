from elasticsearch_dsl import Search, Q


def translate_to_dsl(query: str):
    # This is a simple translation. In practice you will need to make a more sophisticated translation.
    dsl_query = Q("multi_match", query=query, fields=['title', 'content', 'description'])
    return dsl_query
