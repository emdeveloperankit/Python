import PyPDF2
import pyttsx3

def pdf_to_audio(pdf_path):
    # Initialize the PDF reader
    try:
        pdf_file = open(pdf_path, 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file)
    except FileNotFoundError:
        print("Error: PDF file not found.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    # Initialize text-to-speech engine
    speaker = pyttsx3.init()
    
    # Optional: Set properties like rate and volume
    speaker.setProperty('rate', 150)  # Speed of speech
    speaker.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

    # Extract text from each page of the PDF
    text_content = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text_content += page.extract_text()

    # Check if the PDF is not empty
    if not text_content.strip():
        print("The PDF is empty or contains non-text elements.")
        pdf_file.close()
        return

    # Convert text to audio
    print("Converting text to speech...")
    speaker.say(text_content)
    speaker.runAndWait()

    # Clean up
    pdf_file.close()
    print("PDF to audio conversion completed successfully.")

# Usage
pdf_path = input("Enter the path to your PDF file: ")
pdf_to_audio(pdf_path)

speaker.save_to_file(text_content, 'output.mp3')
speaker.runAndWait()
