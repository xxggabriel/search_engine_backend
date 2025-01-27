from math import ceil
# from typing import List
# from elasticsearch_dsl import Search, Q

# from app.db_utils.elastic_search_client import get_elasticsearch


def translate_to_dsl(terms_list: list[str]):
    # This is a simple translation. In practice you will need to make a more sophisticated translation.
    should_clauses = [
        {
          "multi_match": {
            "query": term,
            "fields": [
              "inteiro_teor.with_stemmer",
              "ementas.with_stemmer^2"
            ],
            "fuzziness": "AUTO"
          }
        }
        for term in terms_list
    ]


    return {
        # "query": {
        #     "bool": {
        #         "should": should_clauses,
        #         "minimum_should_match": ceil(
        #             (len(should_clauses) / 2)
        #         ),  # Aceita documentos que correspondam a pelo menos 1 dos termos fuzzy
        #         # "minimum_should_match": len(terms_list)  # Aceita documentos que correspondam a pelo menos 1 dos termos fuzzy
        #     },
            
        # },
        "query":{
            "bool": {
                "must": should_clauses
            }
        },
        "highlight": {
            "fields": {
                "inteiro_teor.with_stemmer": {
                    "pre_tags": ["<strong>"],  # Tag HTML antes do termo destacado
                    "post_tags": ["</strong>"],  # Tag HTML após o termo destacado
                    "fragment_size": 150,  # Tamanho máximo de cada fragmento
                    "number_of_fragments": 3,  # Número máximo de fragmentos retornados
                }
            }
        },
        "aggs": {
            "max_score": {"max": {"script": "_score"}},
            "min_score": {"min": {"script": "_score"}},
        },
        "sort": [
            {
                "_score": {
                    # "order": "asc"
                    "order": "desc"
                }
            }
        ],
        "_source": [
            "id",
            "inteiro_teor.with_stemmer",
            "inteiro_teor.with_stopwords",
            "ementas.with_stemmer",
            "source_court_name",
            "date",
            "numeroProcesso",
            "status_decisao",
        ],
        "size": 20
        # "min_score": max_score * .70,
        # "min_score": 15,
    }
