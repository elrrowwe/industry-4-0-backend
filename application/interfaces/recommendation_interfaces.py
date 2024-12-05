from typing import (
    List,
    Optional
)

from pydantic import (
    BaseModel,
    Field
)

"""
This file contains the request/response models for the recommendation service. 
"""

class RequestPostGetRecommendations(BaseModel):
    """
    Request model for the POST /recommendations endpoint.
    """

    laptop_description: str = Field(
        ...,
        description="A description of the laptop the customer is looking for."
    )

    laptop_brands: Optional[List[str]] = Field(
        None,
        description="A list of laptop brands the customer prefers."
    )

    laptop_price_range: Optional[List[int]] = Field(
        None,
        description="The price range the customer is willing to pay for a laptop. The first element is the minimum price and the second element is the maximum price."
    )


class ResponsePostGetRecommendations(BaseModel):
    """
    Response model for the POST /recommendations endpoint.
    """

    recommendations: List[dict]
