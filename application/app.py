from application.interfaces import (
    RequestPostGetRecommendations,
    ResponsePostGetRecommendations
)

from services import (
    EmbedderService,
    VectorstoreService
)

from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.post("/get_recommendations",
          response_model=ResponsePostGetRecommendations,

          summary="Get laptop recommendations for a customer.",
          description="This endpoint returns a list of laptop recommendations for a customer based on the customer's preferences.",

          response_model_exclude_none=True,
          )
async def get_recommendations(request: RequestPostGetRecommendations):
    """
    Get laptop recommendations for a customer.

    :param request: the request model containing the customer's preferences;
    :return: a list of laptop recommendations for the customer.
    """

    vectorstore_service = VectorstoreService(
        embedder_service=EmbedderService()
    )

    recommendations = vectorstore_service.similarity_search(
        query=request.laptop_description,
        laptop_brands=request.laptop_brands,
        laptop_price_range=request.laptop_price_range
    )

    return recommendations

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.0", port=8000)