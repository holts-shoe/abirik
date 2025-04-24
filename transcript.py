from youtube_transcript_api import YouTubeTranscriptApi

def fetch_and_save_transcript(video_id, output_file=None):
    """
    Fetches the transcript for a YouTube video and saves it to a file.
    
    Args:
        video_id (str): The YouTube video ID
        output_file (str, optional): Path to the output file. Defaults to 'foo.txt'.
    
    Returns:
        str: The extracted transcript text
    """
    # Create the API client
    ytt_api = YouTubeTranscriptApi()
    
    # Fetch the transcript
    fetched_transcript = ytt_api.fetch(video_id)
    
    # Extract just the text from each line
    just_text = " ".join([
        line['text']
        for line in fetched_transcript.to_raw_data()
    ])
    
    # Save to file
    if not output_file:
        output_file = video_id
    with open(output_file, 'w') as f:
        f.write(just_text)
    
    return just_text

# Example usage
transcript = fetch_and_save_transcript('PKQo1Q2QkME')
print(f"Transcript saved successfully. First 100 characters: {transcript[:100]}...")