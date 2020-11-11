# README

## このアプリについて

Webサイトから銘柄一覧を取得するアプリです

## 動作環境システム要件

開発環境構築には以下のものが必要です

- Docker
- docker-compose

## 事前準備 

for Amazon Linux2

Install Docker
```
sudo yum install -y docker
sudo systemctl start docker
sudo usermod -a -G docker ec2-user
```

Auto Start
```
sudo systemctl enable docker
```
Install docker-compoese
```
sudo curl -L https://github.com/docker/compose/releases/download/1.26.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

for Mac

Install Docker for Mac.

## 環境構築手順

srcディレクトリ配下に.envを作成し必要なURLと、HTMLのTagを入れてください
(.env_sampleファイルをリネームして活用ください）

その後、以下のコマンドで一通りのサービスが立ち上がります
ローカル開発でも同様です

```
$ docker-compose up --build
```

## 動作確認

以下は、ローカル環境の動作確認方法です
ブラウザに以下を入力し、銘柄名をローマ字で入力すると表示されます

```
http://localhost
```

