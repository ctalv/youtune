from search import  search
from channel import  channelInfo
from playlist import  playlist
# playlists, channelInfo
# search
test = "Fireship"

channelSearch = search(test)
channelId = channelSearch['items'][0]['id']['channelId']
channel = channelInfo(channelId)
channelAllVideos = channel['items'][0]['contentDetails']['relatedPlaylists']['uploads']
allVideoItems = playlist(channelAllVideos)

for item in allVideoItems['items']:
    videoId = item['snippet']['resourceId']['videoId']
    url = f'https://www.youtube.com/watch?v={videoId}'
    print(url)



"""
{
  "kind": "youtube#searchListResponse",
  "etag": "4V-bPRaFYGqYMymXQYmYAZbG_sM",
  "nextPageToken": "CDIQAA",
  "regionCode": "US",
  "pageInfo": {
    "totalResults": 509,
    "resultsPerPage": 50
  },
  "items": [
    {
      "kind": "youtube#searchResult",
      "etag": "QoeTa1n8TPxsEW_-FRj9r0eTCKM",
      "id": {
        "kind": "youtube#video",
        "videoId": "q2czJLPJ4nA"
      },
      "snippet": {
        "publishedAt": "2025-10-29T18:10:55Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "The humanoid-robot dystopia arrived early...",
        "description": "Get up to 67% off VPS during Hostinger's Black Friday sale. Use code FIRESHIP for an extra discount at ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/q2czJLPJ4nA/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/q2czJLPJ4nA/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/q2czJLPJ4nA/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-10-29T18:10:55Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "MxgjwAhAeQMZgc3BZ-nDAg4b0gU",
      "id": {
        "kind": "youtube#video",
        "videoId": "5uSboan45Zg"
      },
      "snippet": {
        "publishedAt": "2025-10-22T19:04:20Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "OpenAI’s new browser feels familiar…",
        "description": "Try the search engine with the best DX and get 2 months free with code FIRESHIP – https://www.meilisearch.com/cloud OpenAI ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/5uSboan45Zg/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/5uSboan45Zg/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/5uSboan45Zg/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-10-22T19:04:20Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "spFgTt1V8gerKw8Kbns6j8PwcI4",
      "id": {
        "kind": "youtube#video",
        "videoId": "HqL0xhwDz9s"
      },
      "snippet": {
        "publishedAt": "2025-10-21T16:54:32Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "US-EAST-1 is humanity’s weakest link…",
        "description": "Traycer's orchestration tool makes your coding agents smarter. Try it - https://traycer.ai Yesterday, over 2500 internet services got ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/HqL0xhwDz9s/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/HqL0xhwDz9s/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/HqL0xhwDz9s/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-10-21T16:54:32Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "9MV1x8JFA9XDvwg0JO8tJzjt8os",
      "id": {
        "kind": "youtube#video",
        "videoId": "PLKrSVuT-Dg"
      },
      "snippet": {
        "publishedAt": "2025-10-14T18:34:41Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "How to make vibe coding not suck…",
        "description": "Deploy your app the easy way with Sevalla and get $50 in free credits - https://sevalla.com/fireship AI coding may be overhyped ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/PLKrSVuT-Dg/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/PLKrSVuT-Dg/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/PLKrSVuT-Dg/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-10-14T18:34:41Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "syb1ExGbPMRTfRI3XsIAY8oLqEA",
      "id": {
        "kind": "youtube#video",
        "videoId": "91aH8jsG4cc"
      },
      "snippet": {
        "publishedAt": "2025-10-07T19:10:52Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "OpenAI just made your entire tech stack obsolete...",
        "description": "Try out the Junie coding agent in your JetBrains IDE - https://jb.gg/Fireship-Junie-AI At OpenAI DevDay 2025, Sam Altman ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/91aH8jsG4cc/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/91aH8jsG4cc/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/91aH8jsG4cc/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-10-07T19:10:52Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "HKaKJN2eWbfwdfABOG3UR9abG6o",
      "id": {
        "kind": "youtube#video",
        "videoId": "SquU4Bpc73Y"
      },
      "snippet": {
        "publishedAt": "2025-10-03T16:02:28Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "Alibaba is going all in on Qwen…",
        "description": "Try Brilliant for free - https://brilliant.org/fireship and get 20% off a premium annual subscription. Alibaba just announced a $52 ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/SquU4Bpc73Y/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/SquU4Bpc73Y/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/SquU4Bpc73Y/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-10-03T16:02:28Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "fHNxjgf9ZWe_PpiL_KD1fF1kMkk",
      "id": {
        "kind": "youtube#video",
        "videoId": "hkSj-QapfZo"
      },
      "snippet": {
        "publishedAt": "2025-10-01T18:38:26Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "OpenAI’s new slop machine is open for business…",
        "description": "Try out Blitzy's codegen platform for enterprise codebases for free - https://blitzy.com OpenAI's new Sora 2 model is the most ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/hkSj-QapfZo/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/hkSj-QapfZo/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/hkSj-QapfZo/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-10-01T18:38:26Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "hUrGPPdw08Jwk2YdSpv2uUS2pKg",
      "id": {
        "kind": "youtube#video",
        "videoId": "bS9R6aCVEzw"
      },
      "snippet": {
        "publishedAt": "2025-09-29T18:11:47Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "n8n will change your life as a developer...",
        "description": "Get up to 67% off VPS at Hostinger to self-host your own automations. Use code FIRESHIP for an extra discount at ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/bS9R6aCVEzw/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/bS9R6aCVEzw/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/bS9R6aCVEzw/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-09-29T18:11:47Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "WDkxvm57KTA5BhTN8NBS4a6AiEY",
      "id": {
        "kind": "youtube#video",
        "videoId": "DC2p3kFjcK0"
      },
      "snippet": {
        "publishedAt": "2025-09-24T18:52:15Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "There&#39;s a new Linux distro in town for developers...",
        "description": "Install CodeRabbit CLI for free to catch all your AI slop code - https://coderabbit.link/fireship-cli Omarchy is a new omakase distro ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/DC2p3kFjcK0/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/DC2p3kFjcK0/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/DC2p3kFjcK0/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-09-24T18:52:15Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "aQYyIYDLecXd6Zq6Y1pVkYcHIe0",
      "id": {
        "kind": "youtube#video",
        "videoId": "OfOPrmnHRxw"
      },
      "snippet": {
        "publishedAt": "2025-09-17T16:40:13Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "AI companions are taking over… let’s build one",
        "description": "Get $50 in free Vapi credits to build your own voice agent - https://vapi.ai/fireship The richest man in the world has given up on the ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/OfOPrmnHRxw/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/OfOPrmnHRxw/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/OfOPrmnHRxw/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-09-17T16:40:13Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "z-J5RRtYrRUUMizvUcMqdKXijpw",
      "id": {
        "kind": "youtube#video",
        "videoId": "QVqIx-Y8s-s"
      },
      "snippet": {
        "publishedAt": "2025-09-09T17:06:26Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "The largest supply-chain attack ever…",
        "description": "Get 20% off Mobbin Pro to make your apps not ugly - https://mobbin.com/fireship Yesterday, npm got rocked by a record-breaking ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/QVqIx-Y8s-s/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/QVqIx-Y8s-s/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/QVqIx-Y8s-s/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-09-09T17:06:26Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "6woNHmfbPGTcaAJJ3c5tu3BaDpc",
      "id": {
        "kind": "youtube#video",
        "videoId": "XGmZFNG-qQQ"
      },
      "snippet": {
        "publishedAt": "2025-09-04T16:40:15Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "Google won at Monopoly...",
        "description": "Download Warp free at https://go.warp.dev/moofireship - and use code MOO at checkout to get your first month of Warp Pro for just ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/XGmZFNG-qQQ/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/XGmZFNG-qQQ/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/XGmZFNG-qQQ/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-09-04T16:40:15Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "2WfOL1x7eHa_kLVeYIOHfAq48Do",
      "id": {
        "kind": "youtube#video",
        "videoId": "8_GgeASwHwQ"
      },
      "snippet": {
        "publishedAt": "2025-08-29T16:27:32Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "Google’s nano banana just killed Photoshop... let’s run it",
        "description": "Try Brilliant for free - https://brilliant.org/fireship and get 20% off a premium annual subscription. A few days ago, image editing ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/8_GgeASwHwQ/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/8_GgeASwHwQ/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/8_GgeASwHwQ/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-08-29T16:27:32Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "M8v5k6ZKJ1Rz6Q1O2LRmnq1u3vI",
      "id": {
        "kind": "youtube#video",
        "videoId": "pOF11EDprxc"
      },
      "snippet": {
        "publishedAt": "2025-08-27T16:40:59Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "Deno vs Oracle: The ugly custody battle for JavaScript…",
        "description": "Try out Atlassian's Rovo Dev CLI for free - https://fnf.dev/fireship The actual owner of the JavaScript trademark didn't create it, ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/pOF11EDprxc/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/pOF11EDprxc/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/pOF11EDprxc/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-08-27T16:40:59Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "ZoezO-mxLFZxUX45PLVhQDFIYzY",
      "id": {
        "kind": "youtube#video",
        "videoId": "ly6YKz9UfQ4"
      },
      "snippet": {
        "publishedAt": "2025-08-25T17:36:26Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "New MIT study says most AI projects are doomed...",
        "description": "Get the best pair programming app for remote teams - https://tuple.app/fireship - Use code FIRESHIP for a discount A new MIT ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/ly6YKz9UfQ4/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/ly6YKz9UfQ4/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/ly6YKz9UfQ4/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-08-25T17:36:26Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "Sl48Q_tw3yEVzpxBtRsANUkrsac",
      "id": {
        "kind": "youtube#video",
        "videoId": "uHm6FEb2Re4"
      },
      "snippet": {
        "publishedAt": "2025-08-14T18:23:22Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "DuckDB in 100 Seconds",
        "description": "Learn the basics of DuckDB - an in-process, analytical database optimized for OLAP workloads. It's lightweight, portable and ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/uHm6FEb2Re4/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/uHm6FEb2Re4/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/uHm6FEb2Re4/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-08-14T18:23:22Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "TrM4cb6QED0fFcHLVacAv8nEB7Q",
      "id": {
        "kind": "youtube#video",
        "videoId": "8tx2viHpgA8"
      },
      "snippet": {
        "publishedAt": "2025-08-08T16:23:54Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "GPT-5 is here... Can it win back programmers?",
        "description": "Build cross-platform apps in your browser for free - https://dreamflow.app Sama and the boys say that GPT-5 has \"PhD-level\" ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/8tx2viHpgA8/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/8tx2viHpgA8/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/8tx2viHpgA8/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-08-08T16:23:54Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "9YP6Pm2J0d5IQuvs5SEWg0t8JNY",
      "id": {
        "kind": "youtube#video",
        "videoId": "0XvOOi6g5Ok"
      },
      "snippet": {
        "publishedAt": "2025-08-06T15:44:48Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "Google’s Genie model makes realistic worlds in realtime…",
        "description": "Get Warp Pro for only $1 using the code: TOPAGENT at https://go.warp.dev/fireship DeepMind's Genie 3 can create controllable ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/0XvOOi6g5Ok/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/0XvOOi6g5Ok/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/0XvOOi6g5Ok/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-08-06T15:44:48Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "32Ch6KxpQrHFSF6EhuTus9mwwFI",
      "id": {
        "kind": "youtube#video",
        "videoId": "miTpJmMt7uo"
      },
      "snippet": {
        "publishedAt": "2025-07-30T14:56:15Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "The dating app that doxxed 72,000 women...",
        "description": "Get up to 67% off VPS at Hostinger. Use code FIRESHIP for an extra discount at https://hostinger.com/fireship In today's video, ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/miTpJmMt7uo/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/miTpJmMt7uo/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/miTpJmMt7uo/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-07-30T14:56:15Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "E4xNu8twuR1FqvrvQtzIVtGtr9k",
      "id": {
        "kind": "youtube#video",
        "videoId": "-w53i6Ae-YM"
      },
      "snippet": {
        "publishedAt": "2025-07-23T16:29:05Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "Alibaba is coming for Claude...",
        "description": "Try out the awesome new CodeRabbit VS code extension for free https://coderabbit.link/fireship-vscode Qwen3-Coder just ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/-w53i6Ae-YM/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/-w53i6Ae-YM/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/-w53i6Ae-YM/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-07-23T16:29:05Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "X2Lx1HbAJU-F9r-oUGfiTx_8kSc",
      "id": {
        "kind": "youtube#video",
        "videoId": "gA6r7iVzP6M"
      },
      "snippet": {
        "publishedAt": "2025-07-16T15:16:58Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "AWS just released its Cursor killer…",
        "description": "Try Brilliant free for 30 days https://brilliant.org/fireship and get 20% off a premium subscription Out of nowhere, Amazon just ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/gA6r7iVzP6M/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/gA6r7iVzP6M/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/gA6r7iVzP6M/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-07-16T15:16:58Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "hgxHRch4BHFZOvo-sMy2OXe5pNQ",
      "id": {
        "kind": "youtube#video",
        "videoId": "2USUfv7klr8"
      },
      "snippet": {
        "publishedAt": "2025-07-11T15:22:08Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "Grok 4 pushes humanity closer to AGI… but there’s a problem",
        "description": "Get 3 months of Sentry's team plan free: https://sentry.io/fireship Elon Musk has the 'trust me bro' benchmarks to prove that Grok 4 ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/2USUfv7klr8/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/2USUfv7klr8/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/2USUfv7klr8/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-07-11T15:22:08Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "rr1kWeXGQKlb2FHdGB4HNQgnPdI",
      "id": {
        "kind": "youtube#video",
        "videoId": "qqP1ucSiVkE"
      },
      "snippet": {
        "publishedAt": "2025-06-30T16:23:32Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "Google’s new CLI tool hits different…",
        "description": "Try the best video API for developers (and get $50 in free credits) - https://mux.com/fireship Google has finally put Gemini in the ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/qqP1ucSiVkE/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/qqP1ucSiVkE/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/qqP1ucSiVkE/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-06-30T16:23:32Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "sh4_G1squUaJhsP4KyxXdTW-6ag",
      "id": {
        "kind": "youtube#video",
        "videoId": "nFoXCLi8FCc"
      },
      "snippet": {
        "publishedAt": "2025-06-24T16:33:49Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "OpenAI is ruthless...",
        "description": "Use the code: FIRESHIP for 2 months free on Warp Pro at https://go.warp.dev/fireship AI-hardware startup, iyO is suing Jony Ive's ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/nFoXCLi8FCc/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/nFoXCLi8FCc/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/nFoXCLi8FCc/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-06-24T16:33:49Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "Vlq7z_UuIWnavz7c7J8MKfM56nQ",
      "id": {
        "kind": "youtube#video",
        "videoId": "rUCOwCJDh8o"
      },
      "snippet": {
        "publishedAt": "2025-06-16T16:51:11Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "That time Google Cloud Platform bricked the Internet…",
        "description": "Build better apps with PostHog https://posthog.com/fireship Last week, Google Cloud Platform managed to take down a large ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/rUCOwCJDh8o/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/rUCOwCJDh8o/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/rUCOwCJDh8o/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-06-16T16:51:11Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "G5rMlZhKCr4PhJ5HAtrtMxezOd4",
      "id": {
        "kind": "youtube#video",
        "videoId": "Q57_iaGrxLg"
      },
      "snippet": {
        "publishedAt": "2025-06-11T15:01:40Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "Apple redefines reality (again) at WWDC25…",
        "description": "Get 20% off Mobbin Pro to make your apps not ugly: https://mobbin.com/fireship Apple Intelligence was nowhere to be seen at ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/Q57_iaGrxLg/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/Q57_iaGrxLg/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/Q57_iaGrxLg/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-06-11T15:01:40Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "j9OuoRKwpVY-KfMy11Iwfi2-Caw",
      "id": {
        "kind": "youtube#video",
        "videoId": "Sd6F2pfKJmk"
      },
      "snippet": {
        "publishedAt": "2025-06-03T15:00:46Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "This Microsoft-backed AI startup just collapsed… why?",
        "description": "Try Brilliant free for 30 days https://brilliant.org/fireship You'll also get 20% off an annual premium subscription. Builder.ai, a ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/Sd6F2pfKJmk/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/Sd6F2pfKJmk/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/Sd6F2pfKJmk/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-06-03T15:00:46Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "kaBhuiQxwBnW1VTplaTzRk8RaHs",
      "id": {
        "kind": "youtube#video",
        "videoId": "NIgrGqmoeHs"
      },
      "snippet": {
        "publishedAt": "2025-05-20T15:04:55Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "Microsoft just opened the flood gates…",
        "description": "Get the free 80000 hours career guide https://80000hours.org/fireship Microsoft just made GitHub Copilot free and open source ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/NIgrGqmoeHs/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/NIgrGqmoeHs/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/NIgrGqmoeHs/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-05-20T15:04:55Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "76tpW4sJxFNJoiDQWFge123zF6E",
      "id": {
        "kind": "youtube#video",
        "videoId": "jCTvblRXnzg"
      },
      "snippet": {
        "publishedAt": "2025-05-16T14:36:26Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "Google’s AlphaEvolve is making new discoveries in math…",
        "description": "Learn cyber security for FREE with TryHackMe https://tryhackme.com/fireship You'll also get 20% off an annual premium ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/jCTvblRXnzg/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/jCTvblRXnzg/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/jCTvblRXnzg/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-05-16T14:36:26Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "aRu1mHM0JAmyYwkCI51XqG-vE_E",
      "id": {
        "kind": "youtube#video",
        "videoId": "6fnmXX8RK0s"
      },
      "snippet": {
        "publishedAt": "2025-05-15T17:00:16Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "5 wild data structures every developer should know",
        "description": "Try out the awesome new CodeRabbit VS code extension for free https://coderabbit.link/fireship-vscode Let's look at five weird ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/6fnmXX8RK0s/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/6fnmXX8RK0s/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/6fnmXX8RK0s/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-05-15T17:00:16Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "YsjC1GrbLvzDkGOcLUy4g5YISS8",
      "id": {
        "kind": "youtube#video",
        "videoId": "59wV96Kc3dQ"
      },
      "snippet": {
        "publishedAt": "2025-05-07T16:16:07Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "Google must be cooking up something big...",
        "description": "Deploy your app without complexity using Sevalla https://sevalla.com/fireship Let's take a look at the new and improved Gemini ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/59wV96Kc3dQ/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/59wV96Kc3dQ/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/59wV96Kc3dQ/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-05-07T16:16:07Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "3cI7-Tm5HeD2n-hldY5My4kFyHI",
      "id": {
        "kind": "youtube#video",
        "videoId": "lLJbHHeFSsE"
      },
      "snippet": {
        "publishedAt": "2025-05-05T17:38:30Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "The growing divide among React developers…",
        "description": "react.gg is an interactive, challenge-based learning experience that will get you shipping modern React apps like a pro. Get 30% ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/lLJbHHeFSsE/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/lLJbHHeFSsE/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/lLJbHHeFSsE/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-05-05T17:38:30Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "EPPqfU1xPbYG2y1pUQiPTC03gF8",
      "id": {
        "kind": "youtube#video",
        "videoId": "5aN4Xg0VvCs"
      },
      "snippet": {
        "publishedAt": "2025-04-30T15:01:00Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "Redditors shocked to learn they’re arguing with AI bots",
        "description": "Sign up for CodeRabbit using code FIRESHIP to get get 1-month free https://coderabbit.ai/fireship Redditors are being ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/5aN4Xg0VvCs/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/5aN4Xg0VvCs/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/5aN4Xg0VvCs/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-04-30T15:01:00Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "fpWEozoSoA9cCdq7Wdwr0M6ohEw",
      "id": {
        "kind": "youtube#video",
        "videoId": "niWpfRyvs2U"
      },
      "snippet": {
        "publishedAt": "2025-04-29T15:02:16Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "7 Programming myths that waste your time",
        "description": "Try Brilliant free for 30 days https://brilliant.org/fireship You'll also get 20% off an annual premium subscription. In today's video ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/niWpfRyvs2U/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/niWpfRyvs2U/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/niWpfRyvs2U/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-04-29T15:02:16Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "WMRYey1nQQAK_PC7ES6QBeqyESc",
      "id": {
        "kind": "youtube#video",
        "videoId": "XNratwOrSiY"
      },
      "snippet": {
        "publishedAt": "2025-04-16T18:25:47Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "4chan penetrated by a gang of soyjaks…",
        "description": "Timescale makes Postgres unbelievably fast https://rtabench.com/ Today we're diving into the muck of the internet to find out how ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/XNratwOrSiY/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/XNratwOrSiY/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/XNratwOrSiY/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-04-16T18:25:47Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "0jL7fBallyJ_SCbRvpJW7Tq5SIQ",
      "id": {
        "kind": "youtube#video",
        "videoId": "LjbNtw14TwI"
      },
      "snippet": {
        "publishedAt": "2025-04-02T19:43:08Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "The hunt for America&#39;s most wanted computer scientist...",
        "description": "Learn cyber security for FREE with TryHackMe https://tryhackme.com/fireship You'll also get 20% off an annual premium ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/LjbNtw14TwI/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/LjbNtw14TwI/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/LjbNtw14TwI/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-04-02T19:43:08Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "iiEuXgFgwk5L7MMPBwNkTS6R9WA",
      "id": {
        "kind": "youtube#video",
        "videoId": "HyzlYwjoXOQ"
      },
      "snippet": {
        "publishedAt": "2025-03-31T15:00:31Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "Claude&#39;s Model Context Protocol is here... Let&#39;s test it",
        "description": "Deploy your app without complexity and $50 in free credits on Sevalla https://sevalla.com/fireship Learn the fundamentals of ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/HyzlYwjoXOQ/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/HyzlYwjoXOQ/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/HyzlYwjoXOQ/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-03-31T15:00:31Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "sIph33Au4HUc_J5sOf-cJpBKQpU",
      "id": {
        "kind": "youtube#video",
        "videoId": "AwZ8PtoqCeU"
      },
      "snippet": {
        "publishedAt": "2025-03-27T18:47:45Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "21-year old dev destroys LeetCode, gets kicked out of school...",
        "description": "Try Brilliant free for 30 days https://brilliant.org/fireship You'll also get 20% off an annual premium subscription. A 21-year old ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/AwZ8PtoqCeU/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/AwZ8PtoqCeU/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/AwZ8PtoqCeU/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-03-27T18:47:45Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "0cPX2tWof751vW8ErB5c_ENWm-Y",
      "id": {
        "kind": "youtube#video",
        "videoId": "Tw18-4U7mts"
      },
      "snippet": {
        "publishedAt": "2025-03-26T17:56:31Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "The &quot;vibe coding&quot; mind virus explained…",
        "description": "Sign up and download Grammarly for FREE: http://grammarly.com/fireship Let's take a look at the latest craze in the programming ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/Tw18-4U7mts/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/Tw18-4U7mts/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/Tw18-4U7mts/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-03-26T17:56:31Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "t-Vymhi34V3rZscfkKLnEHD5Ca4",
      "id": {
        "kind": "youtube#video",
        "videoId": "PQ2WjtaPfXU"
      },
      "snippet": {
        "publishedAt": "2025-03-12T19:10:12Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "Microsoft goes nuclear on TypeScript codebase…",
        "description": "Get 3 months of Sentry's team plan free https://bit.ly/3Fs19Oj Let's take a first look at the new TypeScript 7 compiler, which is being ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/PQ2WjtaPfXU/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/PQ2WjtaPfXU/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/PQ2WjtaPfXU/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-03-12T19:10:12Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "fDKVkZSNEPVrdP9FRfvwbuNe9pk",
      "id": {
        "kind": "youtube#video",
        "videoId": "UIVADiGfwWc"
      },
      "snippet": {
        "publishedAt": "2025-03-10T16:57:52Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "Our AI girlfriends just leveled up big time…",
        "description": "Build awesome chat, video, and activity feeds for free with Stream https://bit.ly/3XGCXOi Let's take a look at the latest ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/UIVADiGfwWc/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/UIVADiGfwWc/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/UIVADiGfwWc/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-03-10T16:57:52Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "vflwk6EifmQspzb0efPMLyOTIUY",
      "id": {
        "kind": "youtube#video",
        "videoId": "-qjE8JkIVoQ"
      },
      "snippet": {
        "publishedAt": "2025-03-06T17:24:22Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "TikTok just released its React Native killer…",
        "description": "Sign up for CodeRabbit using code FIRESHIP to get get 1-month free https://bit.ly/41rLUxm Let's take a first look at Lynx, an ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/-qjE8JkIVoQ/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/-qjE8JkIVoQ/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/-qjE8JkIVoQ/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-03-06T17:24:22Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "8CcJ3YvGEyNa9CkPOENvP2WnKYc",
      "id": {
        "kind": "youtube#video",
        "videoId": "x2WtHZciC74"
      },
      "snippet": {
        "publishedAt": "2025-02-25T18:27:50Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "Claude 3.7 goes hard for programmers…",
        "description": "Try Convex for free, the only database designed to be generated https://convex.link/fireship Anthropic released an impressive new ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/x2WtHZciC74/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/x2WtHZciC74/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/x2WtHZciC74/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-02-25T18:27:50Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "EgSL97zSoxNjJN2Vik6ZNxJd7hc",
      "id": {
        "kind": "youtube#video",
        "videoId": "jwnez8HdN7E"
      },
      "snippet": {
        "publishedAt": "2025-02-21T18:24:14Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "Microsoft’s new chip looks like science fiction…",
        "description": "Sign up for CodeRabbit using FIRESHIP code, and get free CodeRabbit for 1-month https://bit.ly/41rLUxm Microsoft just ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/jwnez8HdN7E/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/jwnez8HdN7E/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/jwnez8HdN7E/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-02-21T18:24:14Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "WpQCAtwg-5J4TS1hZ4e9XfZ67a8",
      "id": {
        "kind": "youtube#video",
        "videoId": "b0XI-cbel1U"
      },
      "snippet": {
        "publishedAt": "2025-02-18T18:58:55Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "Is Elon’s Grok 3 the new AI king?",
        "description": "Try Brilliant free for 30 days https://brilliant.org/fireship You'll also get 20% off an annual premium subscription. Take a first look at ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/b0XI-cbel1U/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/b0XI-cbel1U/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/b0XI-cbel1U/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-02-18T18:58:55Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "FK5O_6kYP3Q0tX4P-njBPBAQwnY",
      "id": {
        "kind": "youtube#video",
        "videoId": "ozkg_iW9mNU"
      },
      "snippet": {
        "publishedAt": "2025-02-07T20:20:21Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "UK demands backdoor for encrypted Apple user data...",
        "description": "Try Brilliant free for 30 days https://brilliant.org/fireship You'll also get 20% off an annual premium subscription. The United ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/ozkg_iW9mNU/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/ozkg_iW9mNU/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/ozkg_iW9mNU/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-02-07T20:20:21Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "4JBqc6XwtzXJnHhkbmzyxYxxg4Q",
      "id": {
        "kind": "youtube#video",
        "videoId": "Nl7aCUsWykg"
      },
      "snippet": {
        "publishedAt": "2025-01-27T19:27:11Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "Big Tech in panic mode... Did DeepSeek R1 just pop the AI bubble?",
        "description": "Chip stocks like Nvidia are in trouble after the DeepSeek R1 AI model has proven that it is possible to train and run state-of-the-art ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/Nl7aCUsWykg/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/Nl7aCUsWykg/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/Nl7aCUsWykg/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-01-27T19:27:11Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "hO0RoN6yKbC-hPET4m_6jUcrtWg",
      "id": {
        "kind": "youtube#video",
        "videoId": "YrHsw4Oja7w"
      },
      "snippet": {
        "publishedAt": "2025-01-23T18:55:27Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "The Stargate situation is crazy... Elon vs Altman beef intensifies",
        "description": "What is the new Startgate project just announced by OpenAI and why is Elon Musk calling it fake? Learn how the new Stargate ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/YrHsw4Oja7w/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/YrHsw4Oja7w/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/YrHsw4Oja7w/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-01-23T18:55:27Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "NIvta40UnubysJiGJJzsdQSgDxs",
      "id": {
        "kind": "youtube#video",
        "videoId": "gi-wuoIDdjw"
      },
      "snippet": {
        "publishedAt": "2025-01-22T20:04:42Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "Dark web PHP dev Ross Ulbricht released from prison…",
        "description": "Ross Ulbricht received a presidential pardon for his crimes related to the Silk Road. Let's take a look at the tech stack behind the ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/gi-wuoIDdjw/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/gi-wuoIDdjw/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/gi-wuoIDdjw/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-01-22T20:04:42Z"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "LwurSKjIZTXpCWNXxmuu_YgDqZA",
      "id": {
        "kind": "youtube#video",
        "videoId": "-2k1rcRzsLA"
      },
      "snippet": {
        "publishedAt": "2025-01-21T19:18:57Z",
        "channelId": "UCsBjURrPoezykLs9EqgamOA",
        "title": "This free Chinese AI just crushed OpenAI&#39;s $200 o1 model...",
        "description": "Try Brilliant free for 30 days https://brilliant.org/fireship You'll also get 20% off an annual premium subscription. Let's take a look at ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/-2k1rcRzsLA/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/-2k1rcRzsLA/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/-2k1rcRzsLA/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Fireship",
        "liveBroadcastContent": "none",
        "publishTime": "2025-01-21T19:18:57Z"
      }
    }
  ]
}

"""