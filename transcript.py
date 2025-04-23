from youtube_transcript_api import YouTubeTranscriptApi
import json

ytt_api = YouTubeTranscriptApi()
video_id = 'J7yn4tJEmJU'
fetched_transcript = ytt_api.fetch(video_id)

with open('foo.txt', 'w') as f:
    f.write(json.dumps(fetched_transcript.to_raw_data()))
