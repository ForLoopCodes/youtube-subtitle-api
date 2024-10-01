from flask import Flask, jsonify, request

# Import the YouTubeTranscriptApi
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route('/', methods=['GET'])
def documentation():
    """Serve documentation for the API."""
    return jsonify({
        "description": "YouTube Transcript API",
        "endpoints": {
            "/transcript": {
                "method": "GET",
                "description": "Retrieve the transcript for a specified YouTube video.",
                "query_parameters": {
                    "video_id": "The ID of the YouTube video (required)"
                },
                "example_request": "/transcript?video_id=VIDEO_ID",
                "example_response": {
                    "video_id": "VIDEO_ID",
                    "transcript": [
                        {"text": "First line of transcript", "start": 0.0, "duration": 4.0},
                        {"text": "Second line of transcript", "start": 4.1, "duration": 3.5}
                    ]
                }
            }
        }
    })

@app.route('/transcript', methods=['GET'])
def get_transcript():
    video_id = request.args.get('video_id')
    
    if not video_id:
        return jsonify({"error": "video_id is required"}), 400

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return jsonify({"video_id": video_id, "transcript": transcript})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
