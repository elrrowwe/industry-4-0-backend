from qdrant_client import (
    models,
    QdrantClient
)
from application.services import EmbedderService
from application.interfaces import ResponsePostGetRecommendations
from application.credentials import (
    QDRANT_URL,
    QDRANT_API_KEY
)


class VectorstoreService():
    def __init__(self,
                 embedder_service: EmbedderService):
        self.embedder_service = embedder_service

        self.vectorstore = QdrantClient(
            url=QDRANT_URL,
            api_key=QDRANT_API_KEY
        )

    def get_embedding(self,
                      text: str):
        """
        Get the embedding of a text.

        :param text: the text to get the embedding for;
        :return: the embedding of the text.
        """

        embedding = self.embedder_service.embed_query(text)

        return embedding

    def similarity_search(self,
                          query: str,
                          laptop_brands: list[str] = None,
                          laptop_price_range: list[int] = None):
        """
        Search for laptops similar to the description provided by the customer.

        :param query: the description of the laptop the customer is looking for;
        :param laptop_brands: a list of laptop brands the customer prefers;
        :param laptop_price_range: the price range the customer is willing to pay for a laptop. The first element is the minimum price and the second element is the maximum price.
        :return: a list of laptop recommendations for the customer.
        """

        query_embedding = self.get_embedding(query)

        if laptop_brands:
            laptop_brands_filter = models.Filter(
                must=[
                    models.FieldCondition(
                        key="brand",
                        match=models.MatchAny(any=laptop_brands)
                    )
                ]
            )

            must_filters = [laptop_brands_filter]

        else:
            must_filters = []

        if laptop_price_range:
            min_price = laptop_price_range[0]
            max_price = laptop_price_range[1]

            laptop_price_range_filter = models.Filter(
                must=[
                    models.FieldCondition(
                        key="price",
                        range=models.Range(
                            gte=min_price,
                            lte=max_price
                        )
                    )
                ]
            )

            must_filters.append(laptop_price_range_filter)

        results = self.vectorstore.search(
            collection_name="industry4_0",
            query_vector=query_embedding,
            query_filter=models.Filter(must=must_filters),
            with_payload=True
        )

        results_clean = []

        for result in results:
            payload = result.payload

            result_clean = {
                "score": result.score * 100,
                "model_name": payload["model_name"],
                "brand": payload["brand"],
                "price": payload["price"],
                "resolution_pixels": payload["resolution (pixels)"],
                "screen_size": payload["screen_size"],
                "graphics": payload["graphics"],
                "operating_system": payload["Operating System"],
                "ssd_gb": payload["ssd(GB)"],
                "hdd_gb": payload["Hard Disk(GB)"],
                "ram_gb": payload["ram(GB)"],
                "processor_name": payload["processor_name"],
            }

            results_clean.append(result_clean)

        return ResponsePostGetRecommendations(
            recommendations=results_clean
        )
