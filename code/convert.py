from llm_handler import LlmHandler
from maximo_handler import MaximoHandler
import re
import os
import json

def process_java_files_in_folder(folder_path):
    """
    Processes all .java files in the specified folder by passing them to the `read_java_file` function.
    
    Args:
        folder_path (str): The path to the folder containing .java files.
    """
    try:
        # Check if the folder exists
        if not os.path.isdir(folder_path):
            raise ValueError("The provided path is not a valid folder.")

        # Create automation_script folder inside the given folder
        output_folder = os.path.join(folder_path, "automation_script")
        os.makedirs(output_folder, exist_ok=True)

        llm_object = LlmHandler()
        maximo_object = MaximoHandler()
        
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            
            if file_name.endswith('.java'):
                print(f"Processing file: {file_name}")
                # Read Java file content
                java_content = read_java_file(file_path)
                
                if java_content:
                    # Pass java file content to extract qualified class name 
                    qualified_class_name  = extract_package_and_class(java_content)

                    #qualified_class_name = "psdi.app.financial.FldPartialGLAccount"

                    #use MAXIMO API to fetch OBJECT NAME and ATTRIBUTE NAME
                    maximo_response = maximo_object.getvalues(classname=qualified_class_name)
                    print("maximo api's response = ",maximo_response)

                    # Parse the string into a Python dictionary
                    maximo_data = json.loads(maximo_response)

                    # Access the 'member' key
                    members = maximo_data.get("member", [])

                    # Initialize a list to hold the extracted attributes
                    extracted_data = []
                    object_name = ""
                    attribute_name = ""

                    for member in members:
                        attribute_name = member.get("attributename")  
                        object_name = member.get("objectname")  
                        print(f"Attribute Name: {attribute_name}, Object Name: {object_name}")
                        if len(members) > 1:      
                            if attribute_name and object_name:
                                extracted_data.append({"attribute_name": attribute_name, "object_name":object_name}) 

                    # Extract 'attribute_name' and 'object_name' if they exist
                    if len(members) > 1:
                        object_string = "#Provided class name is deployed multiple times here is the list of object names and attribute names " + str(extracted_data)
                    else :
                        object_string = "#OBJECTNAME:" + object_name + "\n" + "#ATTRIBUTENAME: " + attribute_name

                    comment_string = """#This automation script has been generated using watsonx.ai.
#The required parameters to create this in Maximo Environment are as follows:
""" + object_string + """
#LAUNCHPOINT: ATTRIBUTE
#EVENTTYPE: RUN ACTION """

                    # Append custom string to define LAUNCH TYPE and EVENTTYPE
                    updated_content = "#Class name :" + qualified_class_name + "\n" +  comment_string + "\n"

                    # Create a .py file with the same name as the Java file
                    python_file_name = os.path.splitext(file_name)[0] + ".py"
                    python_file_path = os.path.join(output_folder, python_file_name)
                    
                    with open(python_file_path, 'w', encoding='utf-8') as python_file:
                        python_file.write(updated_content)

                        #use class content in llm call to generate respective python code
                        llm_response = llm_object.code_generator(java_content)
                        print("llm response for code generation = ",llm_response)

                        output = llm_response['output']
                        cleaned_output = re.sub(r"(?i)output:\n\n", "", output) #Removing string "output from llm response

                        # with open(python_file_path, 'w', encoding='utf-8') as python_file:
                        python_file.write(str(cleaned_output))
                        
                    print(f"Processed content written to: {python_file_path}")
            else:
                print(f"Skipping non-java file: {file_name}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def read_java_file(file_path):
    """
    Reads the content of a .java file and prints it to the console.
    
    Args:
        file_path (str): The path to the .java file.
    
    Returns:
        str: The content of the file as a string.
    """
    try:
        # Check if the file is a .java file
        if not file_path.endswith('.java'):
            raise ValueError("The provided file is not a .java file.")
        
        # Open and read the file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print("File content successfully read.",content)
            return content
    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")




def extract_package_and_class(file_content):
    """
    Extracts the package name and public class name from Java file content.

    Args:
        file_content (str): The content of the Java file as a string.

    Returns:
        tuple: A tuple containing the package name and the class name.
               (package_name, class_name)
    """
    package_name = None
    class_name = None
    qualified_class_name = None

    try:
        # Extract the package name
        package_match = re.search(r'package\s+([\w\.]+)\s*;', file_content)
        if package_match:
            package_name = package_match.group(1)

        # Extract the public class name
        class_match = re.search(r'public\s+class\s+(\w+)', file_content)
        if class_match:
            class_name = class_match.group(1)

        qualified_class_name = package_name + '.' + class_name

    except Exception as e:
        print(f"An error occurred while parsing the file content: {e}")

    return qualified_class_name





# Example usage
folder_path = input("Enter the path to the folder containing custom Java classes: ")

# Process all .java files in the specified folder
process_java_files_in_folder(folder_path)




