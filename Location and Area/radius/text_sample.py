import xml.etree.ElementTree as ET

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

# Example usage with some polygon points
polygon_points =[]
create_alert_file("alert.txt", polygon_points)
