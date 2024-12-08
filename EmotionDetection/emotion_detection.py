import requests
import json

def emotion_detector(text_to_analyse):
    """
    A function to detect emotions using the Watson NLP library.
    Handles empty inputs and server errors gracefully.
    :param text_to_analyse: Text to analyze.
    :return: A dictionary with emotions or error response.
    """
    if not text_to_analyse:
        # Return None for all keys if the input is empty
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyse}}

    response = requests.post(url, headers=headers, json=input_json)

    if response.status_code == 200:
        # Parse the response and extract emotion data
        response_dict = json.loads(response.text)
        emotions = response_dict["emotionPredictions"][0]["emotion"]

        relevant_emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness']
        filtered_emotions = {key: emotions.get(key, 0) for key in relevant_emotions}

        # Determine the dominant emotion
        dominant_emotion = max(filtered_emotions, key=filtered_emotions.get)
        filtered_emotions['dominant_emotion'] = dominant_emotion

        return filtered_emotions
    else:
        # Handle server errors by returning None for all values
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
