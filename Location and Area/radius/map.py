import folium
from folium import Circle

def create_circle_map(center_coordinates, radius):
    # Create a map centered at the specified location
    map_object = folium.Map(location=center_coordinates, zoom_start=15)

    # Add a circle to the map with the specified radius
    circle = Circle(location=center_coordinates, radius=radius, color='blue', fill=True).add_to(map_object)

    # Add a popup with information about the circle
    popup_text = f"Circle Center: {center_coordinates}<br>Radius: {radius} meters"
    folium.Popup(popup_text, max_width=300).add_to(circle)

    # Save the map as an HTML file
    map_object.save("circle_map.html")

    print(f"Map saved as 'circle_map.html' with a circle centered at '{center_coordinates}'.")

if __name__ == "__main__":
    # Replace the values with the actual coordinates of the circle center
    circle_center_coordinates = [26.3671055, 77.3176535]
    circle_radius = 150  # Specify the radius of the circle in meters

    create_circle_map(circle_center_coordinates, circle_radius)
