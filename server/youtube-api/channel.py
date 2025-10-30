# -*- coding: utf-8 -*-

# Sample Python code for youtube.channels.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os

import googleapiclient.discovery

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def channelInfo(channelId):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = os.environ["API_KEY"]

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.channels().list(
        part="contentDetails",
        id=channelId,
    )
    
    response = request.execute()
    return response


    '''
    {
    "kind": "youtube#channelListResponse",
    "etag": "msVvk8NQ81Q1mv-7nS7NY0XVosE",
    "pageInfo": {
        "totalResults": 1,
        "resultsPerPage": 5
    },
    "items": [
        {
        "kind": "youtube#channel",
        "etag": "npVPMfQrl4xZp0_u1tYYIy3fx8k",
        "id": "UCsBjURrPoezykLs9EqgamOA",
        "contentDetails": {
            "relatedPlaylists": {
            "likes": "",
            "uploads": "UUsBjURrPoezykLs9EqgamOA"
            }
        }
        }
    ]
    }

    all_videos = items[0].contentDetails.relatedPlaylists.uploads

    '''
