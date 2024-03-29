import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {"raw_document": {"text": text_to_analyze}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    try:
        response = requests.post(url, json=myobj, headers=header)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        
        # Parse JSON response
        response_data = json.loads(response.text)
        
        # Extract emotion scores
        emotions = response_data.get('emotionPredictions', [{}])[0].get('emotion', {})
        
        # Extract scores for each emotion
        anger_score = emotions.get('anger', 0)
        disgust_score = emotions.get('disgust', 0)
        fear_score = emotions.get('fear', 0)
        joy_score = emotions.get('joy', 0)
        sadness_score = emotions.get('sadness', 0)
        
        # Find dominant emotion
        emotion_scores = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        
        # Prepare output format
        output = {
            "anger": anger_score,
            "disgust": disgust_score,
            "fear": fear_score,
            "joy": joy_score,
            "sadness": sadness_score,
            "dominant_emotion": dominant_emotion
        }
        
        return output
    
    except requests.exceptions.RequestException as e:
        print("Error: ", e)
        return None  # Return None to indicate failure

# Example usage
print(emotion_detector("i love this"))