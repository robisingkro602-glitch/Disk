from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/process', methods=['POST'])
def process_link():
    data = request.json
    url = data.get('url', '').strip()
    
    if not url or "diskwala.com" not in url:
        return jsonify({"success": False, "message": "Kripya valid DiskWala link daalein!"})
    
    try:
        # Browser ki tarah headers bhejna zaroori hai taaki site block na kare
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            # Agar direct stream link milta hai toh yahan extract hoga
            return jsonify({
                "success": True,
                "stream_url": url, 
                "title": "DiskWala Video Stream"
            })
        else:
            return jsonify({"success": False, "message": "Link fetch karne mein samasya aayi!"})
            
    except Exception as e:
        return jsonify({"success": False, "message": "Connection timeout ya error aa gaya."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
