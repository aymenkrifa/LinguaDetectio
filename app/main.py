import fasttext
import numpy as np
from fastapi import FastAPI

from classes import LanguageDetectionResponse
from classes import RequestBody
from classes import ResponseBody

# Specify the number of other languages to detect
NUM_OTHER_LANGUAGES = 3


fasttext.FastText.eprint = lambda x: None
# Load the FastText model
model_path = "models/lid.176.bin"
model = fasttext.load_model(model_path)

app = FastAPI()


# Handler function for language detection
@app.post("/detect")
async def detect_language(payload: RequestBody):
    # Perform language detection using the pre-loaded FastText model
    predictions = model.predict(payload.text, k=NUM_OTHER_LANGUAGES)

    if predictions:
        # Extract the primary language prediction
        primary_predictions = predictions[0]
        primary_probabilities = predictions[1]

        # Clean language labels
        primary_predictions = [
            pred.replace("__label__", "") for pred in primary_predictions
        ]

        # Sort the primary predictions and probabilities
        sorted_indices = np.argsort(primary_probabilities)[::-1]
        primary_predictions = np.array(primary_predictions)[sorted_indices]
        primary_probabilities = primary_probabilities[sorted_indices]

        # Extract the top prediction
        primary_prediction = primary_predictions[0]
        primary_prediction_probability = primary_probabilities[0]

        # Extract the other predictions
        other_languages = [
            ResponseBody(language=pred, accuracy=prob)
            for pred, prob in zip(
                primary_predictions[: NUM_OTHER_LANGUAGES + 1],
                primary_probabilities[: NUM_OTHER_LANGUAGES + 1],
            )
        ]

        # Construct the response with language detection results
        response = LanguageDetectionResponse(
            request_text=payload.text,
            primary_language=ResponseBody(
                language=primary_prediction, accuracy=primary_prediction_probability
            ),
            other_languages=other_languages,
        )

        # Return a successful response with the language detection results
        return response
    else:
        # Return an internal server error if language detection fails
        return {"error": "Failed to detect language"}
