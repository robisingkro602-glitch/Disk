from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/process', methods=['POST'])
def process_link():
    data = request.json
    url = data.get('url', '').strip()
    
    if not url or "diskwala.com" not in url:
        return jsonify({"success": False, "message": "Invalid DiskWala link!"})
    
    # Yahan aap apna extraction ya stream resolve karne ka logic likh sakte hain
    # Filhaal yeh link ko as a stream source pass kar raha hai
    return jsonify({
        "success": True,
        "stream_url": url, # Agar direct stream mil jaye toh yahan replace karein
        "title": "DiskWala Video Stream"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
