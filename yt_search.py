from youtube_search import YoutubeSearch

def yt_search(title):

    results = YoutubeSearch(title, max_results=2).to_dict()

    return results[0]['id']