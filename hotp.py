import json
import requests

api = "https://webservice.recruit.co.jp/hotpepper/gourmet/v1/"

quary = {
        "key":"[YOUR_API_KEY]",#APIキー（個人情報なのでGit等共有時には非公開）（リクルートにメールアドレス登録で取得できる）
        "middle_area":"Y550",#仙台駅周辺 
        "genre":"G013",#和食(G004),洋食（G005）,イタリアン・フレンチ（G006),中華（G00７）,焼肉（G008）,韓国（G009）,ラーメン（G013）,カフェ（G016）
        "budget":"B010,B001",#ディナー1000円以下
        # "name":"店舗名",
        "count":30,#最大30件取得
        "format":"json"#jsonで返す設定
        }

responce = requests.get(api,quary)#apiにクエリを投げて情報をとってくる
j_load = json.loads(responce.text)["results"]["shop"]#とってきたjsonを読み込み（文字化）
data = []
for shop in j_load:
    data.append({"name":shop["name"],"category":shop["genre"]["name"], "img":shop["photo"]["mobile"]["s"],"opentime":shop["open"], "address":shop["address"], "lat":shop["lat"], "lng":shop["lng"],"budget":shop["budget"]["average"]})
with open('/Users/yuta/Documents/Hackson/ramenfood.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False,indent=4)