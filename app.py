from flask import Flask, render_template, request, jsonify
import os
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
    try:
        ydl_opts = {'format': 'best', 'extract_flat': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            video_title = info.get('title', 'Sample Video')
        mock_clips = [
            {"title": f"Highlight 1: {video_title[:30]}...", "score": "98%", "duration": "45s", "time": "01:23 - 02:08"},
            {"title": f"Highlight 2: Best Moment", "score": "93%", "duration": "50s", "time": "05:10 - 06:00"}
        ]
        return jsonify({'success': True, 'title': video_title, 'clips': mock_clips})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
