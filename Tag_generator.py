from moviepy.editor import VideoFileClip
import speech_recognition as sr

def extract_text_from_audio(audio_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_path) as source:
        audio_text = recognizer.record(source)

    return recognizer.recognize_google(audio_text)

def extract_content_from_video(video_path):
    video_clip = VideoFileClip(video_path)

    # Extract audio from the video
    audio_path = "temp_audio.wav"
    video_clip.audio.write_audiofile(audio_path)

    # Get text from the audio
    audio_text = extract_text_from_audio(audio_path)

    # Analyze video content (add your own video analysis logic here)

    # Clean up temporary audio file
    video_clip.audio.reader.close_proc()
    video_clip.audio = None

    return audio_text

# Example Usage
video_path = "example_video.mp4"
result = extract_content_from_video(video_path)
print("Extracted Content:", result)
