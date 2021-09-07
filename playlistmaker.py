#!/usr/bin/python

import httplib2
import os
import sys

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow
import datetime
import yt_search
import search


def getSongs():
    songs = []
    songs_links = []

    with open('songs.txt', encoding='utf-8') as f:
        for line in f:
            line = line.replace('\n', "")
            if line != "":
                songs.append(line)
    print('Search Started')

    for i in songs:
        title = i # using yt_search.py (without Youtube API)
        id = yt_search.yt_search(title)
        songs_links.append(yt_search.yt_search(title))
        print(i + ' is included!, id : ' + id)
        # title = i # using search.py (Youtube API)
        # songs_links.append(search.youtube_search(title))

    print('Search finsished!')

    return songs_links


# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret. You can acquire an OAuth 2.0 client ID and client secret from
# the Google API Console at
# https://console.developers.google.com/.
# Please ensure that you have enabled the YouTube Data API for your project.
# For more information about using OAuth2 to access the YouTube Data API, see:
#   https://developers.google.com/youtube/v3/guides/authentication
# For more information about the client_secrets.json file format, see:
#   https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
def makeplaylist():
    CLIENT_SECRETS_FILE = 'client_secret_file.json'

    # This variable defines a message to display if the CLIENT_SECRETS_FILE is
    # missing.
    MISSING_CLIENT_SECRETS_MESSAGE = """
  WARNING: Please configure OAuth 2.0

  To make this sample run you will need to populate the client_secrets.json file
  found at:

     %s

  with information from the API Console
  https://console.developers.google.com/

  For more information about the client_secrets.json file format, please visit:
  https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
  """ % os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     CLIENT_SECRETS_FILE))

    # This OAuth 2.0 access scope allows for full read/write access to the
    # authenticated user's account.
    YOUTUBE_READ_WRITE_SCOPE = "https://www.googleapis.com/auth/youtube"
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"

    flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE,
                                   message=MISSING_CLIENT_SECRETS_MESSAGE,
                                   scope=YOUTUBE_READ_WRITE_SCOPE)

    storage = Storage("%s-oauth2.json" % sys.argv[0])
    credentials = storage.get()

    if credentials is None or credentials.invalid:
        flags = argparser.parse_args()
        credentials = run_flow(flow, storage, flags)

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    http=credentials.authorize(httplib2.Http()))

    playlist_title = (datetime.datetime.now()).strftime('%Y %m %d')

    # This code creates a new, private playlist in the authorized user's channel.
    playlists_insert_response = youtube.playlists().insert(
        part="snippet,status",
        body=dict(
            snippet=dict(
                title=(str(playlist_title) + ' M'),
                description=str("%s 플레이리스트" % playlist_title)
            ),
            status=dict(
                privacyStatus="private"  # public, unlisted, private
            )
        )
    ).execute()

    print("New playlist id: %s" % playlists_insert_response["id"])

    song_id = getSongs()
    print(song_id)

    for videoIds in song_id:
        print(videoIds)
        add_video_response = youtube.playlistItems().insert(
            part="snippet",
            body=dict(
                snippet=dict(
                    playlistId=playlists_insert_response["id"],
                    resourceId=dict(
                        kind="youtube#video",
                        videoId=videoIds
                    )
                )
            )
        ).execute()

        try:
            success = add_video_response['kind'] == 'youtube#playlistItem'
        except Exception as e:
            success = False

        print('Added' if success else 'Error', videoIds)

    return playlists_insert_response["id"]


makeplaylist()