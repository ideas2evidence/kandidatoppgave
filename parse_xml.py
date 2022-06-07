
import xml.etree.ElementTree as ET

file = 'resources/p828932869599.xml'

tree =  ET.parse(file)

root = tree.getroot()


def get_questions(root):

    # For all nodes in questionnaire
    for node in root.findall(".//Questionnaire/Routing/Nodes/"):
        # Pick out relevant nodes
        if node.tag in ["Single", "Multi", "Open", "Grid"]:
            # Print information
            print(f'{node.find("Name").text} ({node.tag}): {node}')
            # Find question text and print
            text = node.find('.//Text')
            if text is not None:
                print(text.text)

get_questions(root)

def get_alternatives(root):

    # For each question node
    for node in root.findall("./Questionnaire/Routing/Nodes/"):
        # Only relevant for question nodes with answer alternatives
        if node.tag in ["Single", "Multi", "Grid"]:
            qname = node.find("Name").text
            # For each answer alternative, print value and label
            for answer in node.findall(answerpath(node.tag)):
                value = answer.attrib['Precode'] # i.e. "1"
                label = answer.find('.//Text').text # i.e. "Male"

                print(f'{qname}: {value} - {label}')

get_alternatives(root)