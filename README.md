# Twitter API Tutorial

## Introduction

url

```
curl \
-H "Authorization: Bearer $TOKEN" \
"https://api.twitter.com/2/tweets/search/recent?query=ekusiadadus -is:retweet"
```

```
{
  "data": [
    {
      "edit_history_tweet_ids": [
        "1586363172692594690"
      ],
      "id": "1586363172692594690",
      "text": "山手線Netflix になってた https://t.co/araQzC3ovp"
    },
    {
      "edit_history_tweet_ids": [
        "1585948467641618434"
      ],
      "id": "1585948467641618434",
      "text": "綺麗\n\n将棋ウォーズ棋譜(ekusiadadus:三段 vs piropiro99:二段) #shogiwars #棋神解析\nhttps://t.co/VyfPoaPIGR https://t.co/yYvoJOyORL"
    },
    {
      "edit_history_tweet_ids": [
        "1585801746714349568"
      ],
      "id": "1585801746714349568",
      "text": "@ekusiadadus @Goemon_ryugi それにあった生産性高めるのが後手後手だからね。今ごろ農業AT化とか間に合わん。じっちゃんばっちゃんの生産性の低い農業守りすぎた。ほとんどの業種にも言える事。"
    },
    {
      "edit_history_tweet_ids": [
        "1585685497581817856"
      ],
      "id": "1585685497581817856",
      "text": "@ekusiadadus なぜでしょう？"
    },
    {
      "edit_history_tweet_ids": [
        "1585631297489494016"
      ],
      "id": "1585631297489494016",
      "text": "歓迎会兼飲み会 https://t.co/4jfdideByZ"
    },
    {
      "edit_history_tweet_ids": [
        "1585571070387818501"
      ],
      "id": "1585571070387818501",
      "text": "早めのハロウィンがあった https://t.co/zigHaUWA0U"
    },
    {
      "edit_history_tweet_ids": [
        "1585496238597627906"
      ],
      "id": "1585496238597627906",
      "text": "衝撃的なQRコード https://t.co/Z9OXRCOaam"
    },
    {
      "edit_history_tweet_ids": [
        "1585490375967666176"
      ],
      "id": "1585490375967666176",
      "text": "@ekusiadadus オッサンやジジイは物覚えが悪いですからね。😰"
    },
    {
      "edit_history_tweet_ids": [
        "1585308783894753281"
      ],
      "id": "1585308783894753281",
      "text": "ん？ https://t.co/dkscBWoeUg"
    },
    {
      "edit_history_tweet_ids": [
        "1585291272482590721"
      ],
      "id": "1585291272482590721",
      "text": "やっぱり、iPhone のカメラ優秀過ぎるな https://t.co/GvzP0OBMey"
    }
  ],
  "meta": {
    "newest_id": "1586363172692594690",
    "next_token": "b26v89c19zqg8o3fpzeljmw0ly8vonaqxoek1rd0v2zy5",
    "oldest_id": "1585291272482590721",
    "result_count": 10
  }
}
```
