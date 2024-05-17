from langchain_core.retrievers import BaseRetriever

from Single_Chain.MultiQueryChain import DerivedQueries


async def search_vector_store(
        multi_query: DerivedQueries,
        retriever: BaseRetriever,
        k=3
):
    query_results = {}
    print(f"---RETRIEVING QUERY: {multi_query.derived_query_1}---")

    query_results[multi_query.derived_query_1] = await retriever.ainvoke(input=multi_query.derived_query_1)
    print(f"---RETRIEVING QUERY: {multi_query.derived_query_2}---")
    query_results[multi_query.derived_query_2] = await retriever.ainvoke(input=multi_query.derived_query_2)
    print(f"---RETRIEVING QUERY: {multi_query.derived_query_3}---")
    query_results[multi_query.derived_query_3] = await retriever.ainvoke(input=multi_query.derived_query_3)

    return query_results
