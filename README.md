# YoutubePlaylistMaker

song.txt 파일에 '제목 - 가수'(원하는 검색어)와 같이 저장해두고 playlistmaker.py를 실행하면 됩니다.

## search.py
현재 다운로드 받게 되면 yt_search.py를 사용하도록 되어 있습니다.
이는 Youtube Data API를 사용시 검색만으로 무료 사용량을 너무 많이 잡아먹게 되어 검색은 Youtube API를 사용하지 않는 방향으로 작성하였습니다.
만약 이를 원하지 않고 Youtube Data API의 사용을 원하신다면 
  ```python
  for i in songs:
        title = i # using yt_search.py (without Youtube API)
        id = yt_search.yt_search(title)
        songs_links.append(yt_search.yt_search(title))
        print(i + ' is included!, id : ' + id)
        # title = i # using search.py (Youtube API)
        # songs_links.append(search.youtube_search(title))
  ```      
이 부분을 아래와 같이 바꾸어야 합니다.      
  
  ```python
  for i in songs:
        title = i # using search.py (Youtube API)
        songs_links.append(search.youtube_search(title))
        songs_links.append(yt_search.yt_search(title))
        print(i + ' is included!, id : ' + id)
   ```
 또한,
 ```python
   122  videoId=videoIds
   133  print('Added' if success else 'Error', videoIds)
 ```
 위의 videoIds -> videoIds[0] 로 비꿔서 사용해야합니다.

## client_secret_file.json
 사용시 다른 .py와 같은 저장경로에 client_secret_file.json 가 있어야합니다. 
 이 파일은 console.cloud.google.com/apis/ 의 주소에서 Youtube Data API의 "API 및 서비스", "OAuth 2.0 클라이언트 ID"에서 받을 수 있습니다.
 이 파일의 이름을 'client_secret_file.json'으로 해주시기 바랍니다.

## API 
기본적으로 Youtube Data API를 사용하고 있으며, 검색시 youtube-search 2.1.0을 사용합니다.
```
pip install youtube-search
```
로 설치하실 수 있습니다.
