import json

with open('data/songs.json', 'r', encoding='utf-8') as f:
    songs = json.load(f)

print("Checking first 10 YouTube URLs:")
print("-" * 80)
for song in songs[:10]:
    print(f"{song['id']} - {song['title']} by {song['artist']}")
    print(f"   URL: {song['youtube_url']}")
    print()
