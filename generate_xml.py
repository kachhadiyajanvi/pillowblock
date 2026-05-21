import os
import xml.etree.ElementTree as ET
from xml.dom import minidom

def create_xml():
    root = ET.Element("project")
    
    # Extensions to include
    extensions = ('.html', '.css', '.js', '.py')
    
    for filename in os.listdir('.'):
        if filename.endswith(extensions) and os.path.isfile(filename):
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                file_elem = ET.SubElement(root, "file")
                file_elem.set("name", filename)
                # Using text for content. CDATA is tricky with standard xml.etree, 
                # but standard escaping works fine for XML parsers.
                file_elem.text = content
            except Exception as e:
                print(f"Error reading {filename}: {e}")

    # Convert to string
    xml_str = ET.tostring(root, encoding='utf-8')
    
    # Pretty print
    parsed = minidom.parseString(xml_str)
    pretty_xml = parsed.toprettyxml(indent="  ")
    
    with open('project_code.xml', 'w', encoding='utf-8') as f:
        f.write(pretty_xml)
        
    print("Successfully created project_code.xml")

if __name__ == "__main__":
    create_xml()
