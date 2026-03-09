from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    data = request.get_json()
    name = data.get('name', '')
    email = data.get('email', '')
    message = data.get('message', '')
    
    if not name or not email or not message:
        return jsonify({'success': False, 'message': 'Alle velden zijn verplicht.'}), 400
    
    return jsonify({'success': True, 'message': 'Bedankt voor uw bericht! We nemen zo snel mogelijk contact met u op.'})

if __name__ == '__main__':
    debug = os.environ.get('FLASK_DEBUG', 'false').lower() == 'true'
    app.run(host='0.0.0.0', port=5000, debug=debug)
