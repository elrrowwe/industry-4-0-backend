from mixedbread_ai.client import MixedbreadAI
from application.credentials.credentials import MXBAI_API_KEY


class EmbedderService():
    def __init__(self,
                 api_key: str = MXBAI_API_KEY):
        self.embedder = MixedbreadAI(api_key=api_key)

    def embed_query(self,
                     text: str) -> list[float]:
        """
        Get the embedding of a text.

        :param text: the text to get the embedding for;
        :return: the embedding of the text.
        """

        embedding = self.embedder.embeddings(
            model='mixedbread-ai/mxbai-embed-large-v1',
            input=[text],
            normalized=True,
            encoding_format='float',
            truncation_strategy='end'
        )

        return embedding.data[0].embedding
