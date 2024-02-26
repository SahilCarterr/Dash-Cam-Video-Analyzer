from flask import Flask, render_template, request, jsonify
import webbrowser
import math
import folium
from folium import Circle
import threading
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('geolocation.html')

@app.route('/process_location', methods=['POST'])
def process_location():
    latitude = float(request.form.get('latitude'))
    longitude = float(request.form.get('longitude'))
    a=latitude
    b=longitude 
    
    import csv

    # Data
    data = [29.992621742025566, 77.56198705768541]

    # File path
    file_path = "data.csv"

    # Writing data to CSV file
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Latitude", "Longitude"])  # Writing header
        writer.writerow(data)  # Writing data



    circle_center_coordinates = [a,b]
    circle_radius = 150  # Specify the radius of the circle in meters

    
    create_circle_map(circle_center_coordinates, circle_radius)
    points=findpoints(a,b)
    formatted_points = [
    f"{point['lat']},{point['lon']}"
    for point in points]
    polygon_points =formatted_points
    create_alert_file("alert.txt", polygon_points) 
    stop_server()
    return jsonify({'status': 'success', 'message': 'Location received successfully.'})

def create_circle_map(center_coordinates, radius):
    map_object = folium.Map(location=center_coordinates, zoom_start=15)
    circle = Circle(location=center_coordinates, radius=radius, color='blue', fill=True).add_to(map_object)
    popup_text = f"Circle Center: {center_coordinates}<br>Radius: {radius} meters"
    folium.Popup(popup_text, max_width=300).add_to(circle)
    map_object.save("circle_map.html")
    print(f"Map saved as 'circle_map.html' with a circle centered at '{center_coordinates}'.")
def run_server():
    app.run(debug=True, use_reloader=False)    
def stop_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is not None:
        func()

def findpoints(lat, lon):
    radius = 0.15
    N = 30 
    circlePoints = []
    count=0
    for k in range(N):
        angle = math.pi*2*k/N
        dx = radius*math.cos(angle)
        dy = radius*math.sin(angle)
        point = {}
        point['lat']= lat + (180/math.pi)*(dy/6371) #Earth Radius
        point['lon']= lon + (180/math.pi)*(dx/6371)/math.cos(lon*math.pi/180) #Earth Radius
        circlePoints.append(point)
        if(count==0):
            a=point
        count=count+1
    circlePoints.append(a)
    return circlePoints

def create_alert_file(file_path, polygon_points):
    # Create the root element
    alert = ET.Element("alert", xmlns="urn:oasis:names:tc:emergency:cap:1.1")

    # Create sub-elements
    identifier = ET.SubElement(alert, "identifier")
    identifier.text = "AL20110412020900AnimalWarning"

    sender = ET.SubElement(alert, "sender")
    sender.text = "w-nws.webmaster@noaa.gov"

    sent = ET.SubElement(alert, "sent")
    sent.text = "2024-01-17T21:18:07-05:00"

    status = ET.SubElement(alert, "status")
    status.text = "Actual"

    msgType = ET.SubElement(alert, "msgType")
    msgType.text = "Alert"

    scope = ET.SubElement(alert, "scope")
    scope.text = "Public"

    info = ET.SubElement(alert, "info")

    language = ET.SubElement(info, "language")
    language.text = "en-US"

    category = ET.SubElement(info, "category")
    category.text = "Met"

    event = ET.SubElement(info, "event")
    event.text = "Animal Warning"

    urgency = ET.SubElement(info, "urgency")
    urgency.text = "Immediate"

    severity = ET.SubElement(info, "severity")
    severity.text = "Extreme"

    certainty = ET.SubElement(info, "certainty")
    certainty.text = "Observed"

    effective = ET.SubElement(info, "effective")
    effective.text = "2024-01-17T21:09:00-05:00"

    expires = ET.SubElement(info, "expires")
    expires.text = "2024-01-17T21:30:00-05:00"

    headline = ET.SubElement(info, "headline")
    headline.text = "Animal Warning issued"

    instruction = ET.SubElement(info, "instruction")
    instruction.text = "There is an animal near you, be safe and drive slow."

    area = ET.SubElement(info, "area")

    areaDesc = ET.SubElement(area, "areaDesc")
    areaDesc.text = "Haryana"

    polygon = ET.SubElement(area, "polygon")
    polygon.text = "\n".join(f"                    {point}" for point in polygon_points)

    # Create the ElementTree
    tree = ET.ElementTree(alert)

    # Convert the ElementTree to a string with indentation
    xml_content = ET.tostring(alert, encoding="utf-8").decode("utf-8").replace('><', '>\n<')

    # Write to the text file
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(xml_content)
if __name__ == '__main__':
    server_thread = threading.Thread(target=run_server)
    server_thread.start()
    # webbrowser.open('http://127.0.0.1:5000')
    # app.run(debug=True,use_reloader=False)
    webbrowser.open('C:\\Users\\Mohd Sahil\\Downloads\\Today_Work\\Today_Work_html\\circle_map.html') 
    webbrowser.open('http://127.0.0.1:5000') 
    server_thread.join()



