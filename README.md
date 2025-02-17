# deepimfam

Markdownで記述されているので，ビジュアルモードでの閲覧を推奨 

## 環境設定
- uv 0.5.18
- Python 3.12

## uvの使い方
- pythonのバージョン変更
    ```bash:
    uv python pin 3.*.*
    ```

- ライブラリの追加
    ```bash:
    uv add *
    ```

- ライブラリの削除
    ```bash:
    uv remove *
    ```

- プログラムの実行
    ```bash:
    uv run *
    ```

## 各自設定（config.yaml）
- train_data_fname: 学習用の配列データのファイルパス
- test_data_fname: 検証用の配列データのファイルパス