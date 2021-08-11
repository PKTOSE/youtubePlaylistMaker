
from googleapiclient.discovery import build

DEVELOPER_KEY = "your youtube api key"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(title):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  search_response = youtube.search().list(
    q=title,
    part="id,snippet",
    maxResults=2
  ).execute()

  videos = []
  videolinks = []
  links = []



  for search_result in search_response.get("items",[]):
      if search_result["id"]["kind"] == "youtube#video":
          videos.append("%s (%s)" % (search_result["snippet"]["title"],
                                     search_result["id"]["videoId"]))
          videolinks.append("https://www.youtube.com/watch?v=" + search_result["id"]["videoId"])
          links.append(search_result["id"]["videoId"])


  #print(videos,links)
  return links

