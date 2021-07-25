from google.cloud import vision # google cloudのvisionを読み込んで

with open('./nuko.jpg', 'rb') as nuko_file: # r(read binary モード)
  content = nuko_file.read() # rbしたものを読み込みcontentに代入

image = vision.Image(content=content) # インスタンス作成(公式) vision APIが扱える画像データにする

annotator_client = vision.ImageAnnotatorClient() # annotation = タグ付けする作業

responce_data = annotator_client.label_detection(image=image) # imageの解析データ
labels = responce_data.label_annotations # 必要な情報を抽出

for label in labels:
  print(label.description, ':', round(label.score * 100), '%')

# Cat : 96 %
# Eye : 94 %
# Felidae : 92 %
# Carnivore : 90 %
# Small to medium-sized cats : 88 %
# Whiskers : 85 %
# Iris : 85 %
# Fawn : 82 %
# Terrestrial animal : 78 %
# Snout : 77 %