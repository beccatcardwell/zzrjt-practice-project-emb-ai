'''Sentiment analysis module'''
import json
import requests


def sentiment_analyzer(text_to_analyze):
    '''Request sentiment analyzer with input text and output label and score as a dictionary'''
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    my_obj =  { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = my_obj, headers=header)
    status_code = response.status_code
    formatted_response = json.loads(response.text)
    if status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    elif status_code == 500:
        label = None
        score = None

    return {"label": label, "score": score}