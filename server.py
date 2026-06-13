'''Module for server functions 
'''
from flask import render_template, Flask, request
from EmotionDetection.emotion_detection import emotion_detector


app=Flask("WebApp for Emotion Detection")

@app.route("/emotionDetector")
def emotion_detection_link():
    '''Method for emotion dectection
    '''
    arg = request.args.get("textToAnalyze")
    result = emotion_detector(arg)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return f"""For the given statement, the system response is 'anger': {result['anger']},
     'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']}
      and 'sadness': {result['sadness']}. The dominant emotion 
      is <b>{result['dominant_emotion']}</b>"""

@app.route("/")
def home():
    '''Method for homepage
    '''
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug = True)
