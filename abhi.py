from youtube_transcript_api import YouTubeTranscriptApi

ytt_api = YouTubeTranscriptApi()
video_id = 'J7yn4tJEmJU'
fetched_transcript = ytt_api.fetch(video_id)

with open('foo.txt', 'w') as f:
    just_text = " ".join([
        line['text']
        for line in fetched_transcript.to_raw_data()
    ])
    f.write(just_text)
