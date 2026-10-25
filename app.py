from flask import Flask, render_template, request, jsonify
import yt_dlp

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/process', methods=['POST'])
def process_video():
    data = request.json
    video_url = data.get('url')
    if not video_url:
        return jsonify({'error': 'URL is required'}), 400
    
    video_title = "YouTube Video Highlight"
    try:
        ydl_opts = {
            'format': 'best',
            'quiet': True,
            'no_warnings': True,
            'extractor_args': {'youtube': {'player_client': ['android', 'web']}}
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            video_title = info.get('title', 'YouTube Video')
    except Exception as e:
        video_title = "Viral Masterpiece Video"

    mock_clips = [
        {"title": f"Viral Peak: {video_title[:25]}...", "score": "98%", "duration": "45s", "time": "00:15 - 01:00"},
        {"title": f"Key Moment & Reaction", "score": "94%", "duration": "30s", "time": "02:30 - 03:00"},
        {"title": f"Best Climax Ending", "score": "91%", "duration": "40s", "time": "05:10 - 05:50"}
    ]
    return jsonify({'success': True, 'title': video_title, 'clips': mock_clips})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
