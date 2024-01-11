#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import speech_recognition as sr


def audio_to_text():
    recognizer = sr.Recognizer()

    print("Choose an option:")
    print("1. Real-time audio input")
    print("2. Upload an audio file")
    
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        with sr.Microphone() as source:
            print("Say something...")
            audio_data = recognizer.listen(source)
            print("Processing...")

    elif choice == '2':
        file_path = input("Enter the path of the audio file: ")
        audio_data = sr.AudioFile(file_path)
        with audio_data as source:
            audio_data = recognizer.record(source)

    else:
        print("Invalid choice. Please enter either 1 or 2.")
        return

    try:
        text = recognizer.recognize_google(audio_data)
        print("Text from audio:\n", text)

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")

    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    audio_to_text()

