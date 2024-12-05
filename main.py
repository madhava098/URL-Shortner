from flask import Flask, request, render_template
import pyshorteners

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    shortened_url = None
    url = request.args.get('name')  # Safely get the URL from query parameters
    if url:
        try:
            s = pyshorteners.Shortener()
            shortened_url = s.tinyurl.short(url)  # Shorten the URL
        except Exception as e:
            return f"Error: {e}", 400

    return render_template('home.html', shortened_url=shortened_url)

if __name__ == '__main__':
    app.run(debug=True)
