# イメージを選択
FROM python:3.9.5-alpine

# バイナリレイヤ下での標準出力とエラー出力を抑制
ENV PYTHONUNBUFFERED 1

# 開始ディレクトリ位置
WORKDIR /usr/src/pokemonsizegame/api

# 必要なものをインストール
# 今回はalpineなのでapkを使用する。
RUN apk update

# ADDかCOPYを使うなら.dockerignoreを書いておく。
ADD . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt