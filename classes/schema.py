from typing import List

from pydantic import BaseModel


class RequestBody(BaseModel):
    """
    Request body schema for the language detection endpoint.

    Parameters
    ----------
    BaseModel : pydantic.BaseModel
        Base class for Pydantic models.
    """

    text: str


class ResponseBody(BaseModel):
    """
    Response body schema for language detection results for a single language.

    Parameters
    ----------
    BaseModel : pydantic.BaseModel
        Base class for Pydantic models.
    """

    language: str
    accuracy: float


class LanguageDetectionResponse(BaseModel):
    """
    Response body schema with the primary language
    prediction and other language predictions.

    Parameters
    ----------
    BaseModel : pydantic.BaseModel
        Base class for Pydantic models.
    """

    request_text: str
    primary_language: ResponseBody
    other_languages: List[ResponseBody]
