# YoutubePlaylistMaker 유튜브 플레이리스트 | 재생목록 자동으로 만들기
자신의 유튜브 계정에 재생목록을 자동으로 만들어줍니다. 텍스트 파일에 있는 검색어를 줄단위로 받아서 검색시 최상단의 영상을 재생목록에 추가합니다.
텍스트로 되어있는 노래목록을 유튜브 재생목록으로 만들기 위해서 만들었습니다.
song.txt 파일에 '제목 - 가수'(원하는 검색어)와 같이 저장해두고 playlistmaker.py를 실행하면 됩니다.

## search.py
현재 기본으로 yt_search.py를 사용하도록 되어 있습니다.
이는 Youtube Data API를 사용시 검색만으로 무료 사용량을 너무 많이 차지하여 검색은 Youtube API를 사용하지 않는 방향으로 작성하였습니다.
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
        print(i + ' is included!, id : ' + id)
   ```
 또한,
 ```python
   122  videoId=videoIds
   133  print('Added' if success else 'Error', videoIds)
 ```
 위의 videoIds -> videoIds[0] 로 바꿔서 사용해야합니다.

## client_secret_file.json
 사용시 다른 .py와 같은 저장경로에 client_secret_file.json 가 있어야합니다. 
 이 파일은 https://console.cloud.google.com/apis/dashboard 에서 Youtube Data API의 "API 및 서비스", "OAuth 2.0 클라이언트 ID"에서 받을 수 있습니다.
 이 파일의 이름을 'client_secret_file.json'으로 해주시기 바랍니다.

## API 
기본적으로 Youtube Data API를 사용하고 있으며, 검색시 youtube-search 2.1.0을 사용합니다.
```
pip install youtube-search
```
로 설치하실 수 있습니다.

## pip install 
```
pip install -r requirements.txt
```
위의 명령어를 통해 필요한 패키지들을 한번에 설치할 수 있습니다.

### Youtube Data API (v3) cost
[비용계산](https://developers.google.com/youtube/v3/determine_quota_cost?hl=en)

### Python Ver
python 3.9.4를 기준으로 작성되었습니다.
