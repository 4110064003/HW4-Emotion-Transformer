import json

songs = [
  {
    "id": "kpop-001",
    "title": "Spring Day",
    "artist": "BTS",
    "emotions": ["sadness", "loneliness", "longing"],
    "theme": "Missing someone, hope for reunion, seasons of life",
    "genre": "K-pop Ballad",
    "year": 2017,
    "spotify_url": "https://open.spotify.com/track/0jNaRf4IuDVnbVMP29nGBh",
    "youtube_url": "https://www.youtube.com/watch?v=xEeFrLSkMm8",
    "why_it_helps": "溫暖的旋律提醒我們,即使在孤獨中,春天終將到來,再次相見的日子不遠了"
  },
  {
    "id": "kpop-002",
    "title": "Life Goes On",
    "artist": "BTS",
    "emotions": ["sadness", "disappointment", "acceptance"],
    "theme": "Moving forward through hardship, life continues",
    "genre": "K-pop Ballad",
    "year": 2020,
    "spotify_url": "https://open.spotify.com/track/3rWDp3tMwhYRVlcQ52QPiL",
    "youtube_url": "https://www.youtube.com/watch?v=-5q5mZbe3V8",
    "why_it_helps": "溫柔地提醒我們,儘管遇到困難,生活還是會繼續前進"
  },
  {
    "id": "kpop-003",
    "title": "Not Today",
    "artist": "BTS",
    "emotions": ["anger", "frustration", "determination"],
    "theme": "Fighting spirit, resistance, never giving up",
    "genre": "K-pop Hip-hop",
    "year": 2017,
    "spotify_url": "https://open.spotify.com/track/4Iha6BXy6I0LnpfcH1vM1v",
    "youtube_url": "https://www.youtube.com/watch?v=9DwzBICPhdM",
    "why_it_helps": "強烈的節奏和力量感幫助釋放負面情緒,激發戰鬥精神"
  },
  {
    "id": "kpop-004",
    "title": "MIC Drop",
    "artist": "BTS",
    "emotions": ["anger", "confidence", "triumph"],
    "theme": "Overcoming doubters, self-confidence, success",
    "genre": "K-pop Hip-hop",
    "year": 2017,
    "spotify_url": "https://open.spotify.com/track/3dhWxRQwuCWBjvRQn0LNTg",
    "youtube_url": "https://www.youtube.com/watch?v=kTlv5_Bs8aw",
    "why_it_helps": "自信滿滿的態度幫助你找回自我價值,對抗負面聲音"
  },
  {
    "id": "kpop-005",
    "title": "Answer: Love Myself",
    "artist": "BTS",
    "emotions": ["sadness", "loneliness", "self-doubt"],
    "theme": "Self-love, self-acceptance, finding inner peace",
    "genre": "K-pop Ballad",
    "year": 2018,
    "spotify_url": "https://open.spotify.com/track/0FqpMd9W2003dPBjHqTvLG",
    "youtube_url": "https://www.youtube.com/watch?v=o9vNl3SwgW4",
    "why_it_helps": "鼓勵我們學會愛自己,接納自己的不完美,找到內心的平靜"
  },
  {
    "id": "kpop-006",
    "title": "Magic Shop",
    "artist": "BTS",
    "emotions": ["anxiety", "fear", "loneliness"],
    "theme": "Safe space, comfort, you are not alone",
    "genre": "K-pop Ballad",
    "year": 2018,
    "spotify_url": "https://open.spotify.com/track/1GbCW21XRuUqfiMAu6JuKN",
    "youtube_url": "https://www.youtube.com/watch?v=eRkpk2hV94M",
    "why_it_helps": "溫暖的歌詞創造一個安全的空間,提醒你並不孤單"
  },
  {
    "id": "kpop-007",
    "title": "Home",
    "artist": "BTS",
    "emotions": ["loneliness", "longing", "comfort"],
    "theme": "Finding home in people, belonging, comfort",
    "genre": "K-pop R&B",
    "year": 2019,
    "spotify_url": "https://open.spotify.com/track/6aj0vqMMQEGlcXjJVSNViB",
    "youtube_url": "https://www.youtube.com/watch?v=gkPkuUGFCso",
    "why_it_helps": "溫柔的旋律提醒我們,家不只是一個地方,更是與所愛之人在一起的感覺"
  },
  {
    "id": "kpop-008",
    "title": "Permission to Dance",
    "artist": "BTS",
    "emotions": ["sadness", "frustration", "joy"],
    "theme": "Joy, freedom, dancing through difficulties",
    "genre": "K-pop Dance",
    "year": 2021,
    "spotify_url": "https://open.spotify.com/track/6Kw5Smewn1wtMuCHlKgXIY",
    "youtube_url": "https://www.youtube.com/watch?v=CuklIb9d3fI",
    "why_it_helps": "歡快的節奏鼓勵你放下煩惱,給自己跳舞的許可,找回快樂"
  },
  {
    "id": "kpop-009",
    "title": "Good to Me",
    "artist": "SEVENTEEN",
    "emotions": ["joy", "gratitude", "happiness"],
    "theme": "Appreciation, gratitude, cherishing moments",
    "genre": "K-pop Pop",
    "year": 2019,
    "spotify_url": "https://open.spotify.com/track/2X9iANJqYkPKJCFOEwfYLK",
    "youtube_url": "https://www.youtube.com/watch?v=G6RiHvvOW7U",
    "why_it_helps": "輕快的旋律提醒我們珍惜身邊的美好,感恩生活中的小確幸"
  },
  {
    "id": "kpop-010",
    "title": "Don't Wanna Cry",
    "artist": "SEVENTEEN",
    "emotions": ["sadness", "heartbreak", "longing"],
    "theme": "Holding back tears, emotional strength, farewell",
    "genre": "K-pop Ballad",
    "year": 2017,
    "spotify_url": "https://open.spotify.com/track/5SkRRZhwIRieTQq7qL2EbL",
    "youtube_url": "https://www.youtube.com/watch?v=zEkg4GBQumc",
    "why_it_helps": "優美的旋律陪伴你度過傷心時刻,給予情感宣洩的空間"
  }
]

with open('data/songs.json', 'w', encoding='utf-8') as f:
    json.dump(songs, f, ensure_ascii=False, indent=2)

print(f"Created songs.json with {len(songs)} K-pop songs")
