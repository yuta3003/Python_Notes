# Python 基礎

## Python 起動方法
### Interactive
対話的にPythonを実行する方法で、すぐにコードを入力し結果を確認できます。

ターミナルやコマンドプロンプトで以下のコマンドを入力することで起動できます。
```sh
python
```
起動後の画面（例）:
```
Python 3.10.0 (default, Oct  4 2021, 14:59:43)
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
`>>> `はPythonのプロンプトを表し、ここにコードを入力すると実行されます。

pythonの対話モードから抜ける場合には`exit()`を実行してください。
```
>>> exit()
```

また、ブラウザ上で実行できる[Google Colab](https://colab.research.google.com/)やJupyter Labなどもあります。

### Non-Interactive
Python スクリプト（.py ファイル）を実行するモード。
スクリプトの内容をすべて書いておき、一気に実行します。

1. 以下コマンドをターミナルで実行し、メモ帳を開きます。
    ```cmd
    notepad script.py
    ```
1. 以下内容を貼り付け、保存します。
    ```Python
    name = "Python"
    print(f"Hello, {name}!")
    ```
1. ターミナルに戻り、pythonを実行します。
    ```
    python script.py
    ```
    実行結果:
    ```
    $ python script.py
    Hello, Python!
    ```


## 参考資料
- [東京大学Python入門](https://utokyo-ipp.github.io/)
- [Python公式チュートリアル](https://docs.python.org/ja/3/tutorial/index.html)
