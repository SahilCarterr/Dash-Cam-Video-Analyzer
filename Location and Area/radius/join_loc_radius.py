from flask import Flask, render_template, request, jsonify
import webbrowser
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('geolocation.html')

@app.route('/process_location', methods=['POST'])
def process_location():
    latitude = request.form.get('latitude')
    longitude = request.form.get('longitude')
    points = findpoints(latitude, longitude)
    for point in points:
       print(f"{point['lat']},{point['lon']}")
    return jsonify({'status': 'success', 'message': 'Location received successfully.'})


def findpoints(lat, lon):
    radius = 0.15
    N = 30 
    circlePoints = []
    for k in range(N):
        angle = math.pi*2*k/N
        dx = radius*math.cos(angle)
        dy = radius*math.sin(angle)
        point = {}
        point['lat']= lat + (180/math.pi)*(dy/6371) #Earth Radius
        point['lon']= lon + (180/math.pi)*(dx/6371)/math.cos(lon*math.pi/180) #Earth Radius
        circlePoints.append(point)
    return circlePoints

if __name__ == '__main__':
    # Open the default web browser to the specified URL when the application starts
    webbrowser.open('http://127.0.0.1:5000')
    
    app.run(debug=True,use_reloader=False)

