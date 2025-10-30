# -*- coding: utf-8 -*-

# Sample Python code for youtube.playlistItems.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os

import googleapiclient.discovery

def playlist():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = os.environ["API_KEY"]

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.playlistItems().list(
        part="contentDetails",
        playlistId="UUsBjURrPoezykLs9EqgamOA"
    )
    response = request.execute()

    print(response)

    '''
    items[x]

    {
    "kind": "youtube#playlistItemListResponse",
    "etag": "CAOC1wV5Safp71dMu66qKdU1lHw",
    "nextPageToken": "EAAaHlBUOkNBVWlFRFE0UkRVeU5ERTFRa1JDTUVOQk0wWQ",
    "items": [
        {
        "kind": "youtube#playlistItem",
        "etag": "LKY5f429bulVwRRZieJPyc6Drzg",
        "id": "VVVzQmpVUnJQb2V6eWtMczlFcWdhbU9BLnEyY3pKTFBKNG5B",
        "contentDetails": {
            "videoId": "q2czJLPJ4nA",
            "videoPublishedAt": "2025-10-29T18:10:55Z"
        }
        },
        {
        "kind": "youtube#playlistItem",
        "etag": "iD4wzZ640UC6TpB4O3HxZGmQ-os",
        "id": "VVVzQmpVUnJQb2V6eWtMczlFcWdhbU9BLjV1U2JvYW40NVpn",
        "contentDetails": {
            "videoId": "5uSboan45Zg",
            "videoPublishedAt": "2025-10-22T19:04:20Z"
        }
        },
        {
        "kind": "youtube#playlistItem",
        "etag": "1Sjje_o_FDMe08rl7hlAy5_KfqM",
        "id": "VVVzQmpVUnJQb2V6eWtMczlFcWdhbU9BLkhxTDB4aHdEejlz",
        "contentDetails": {
            "videoId": "HqL0xhwDz9s",
            "videoPublishedAt": "2025-10-21T16:54:32Z"
        }
        },
        {
        "kind": "youtube#playlistItem",
        "etag": "umg01B1CJVAnrRWozo-pGO54gtY",
        "id": "VVVzQmpVUnJQb2V6eWtMczlFcWdhbU9BLnlsMFlXQTJLMkIw",
        "contentDetails": {
            "videoId": "yl0YWA2K2B0",
            "videoPublishedAt": "2025-10-17T19:32:39Z"
        }
        },
        {
        "kind": "youtube#playlistItem",
        "etag": "_XM6xYakWVjyjPhjo7DE4bkE9pU",
        "id": "VVVzQmpVUnJQb2V6eWtMczlFcWdhbU9BLnFKbGU2QmtpNE9n",
        "contentDetails": {
            "videoId": "qJle6Bki4Og",
            "videoPublishedAt": "2025-10-16T17:32:29Z"
        }
        }
    ],
    "pageInfo": {
        "totalResults": 770,
        "resultsPerPage": 5
    }
    }

    '''

if __name__ == "__playlist__":
    playlist()