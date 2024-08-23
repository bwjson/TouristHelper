from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
)

from cities.models import City

def query_search(query):
    vector = SearchVector("name", "description")
    query = SearchQuery(query)

    result = (
        City.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by("-rank")
    )

    '''result = (
        City.objects
        .annotate(
            rank=SearchRank(vector, query),
            similarity=TrigramSimilarity("name", query) + TrigramSimilarity("description", query)
        )
        .filter(rank__gt=0)  
        .filter(similarity__gt=0.1)  
        .order_by("-rank", "-similarity") 
    )'''

    return result

