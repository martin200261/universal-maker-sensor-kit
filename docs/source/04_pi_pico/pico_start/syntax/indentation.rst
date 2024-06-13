.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Facebook上で、仲間と一緒にRaspberry Pi、Arduino、ESP32をさらに深く探求しましょう。

    **なぜ参加するのか？**

    - **専門的なサポート**：購入後の問題や技術的な課題をコミュニティやチームの助けを借りて解決。
    - **学びと共有**：スキルを向上させるためのヒントやチュートリアルを交換。
    - **限定プレビュー**：新製品発表や予告編に早期アクセス。
    - **特別割引**：最新製品の特別割引を楽しむ。
    - **フェスティブプロモーションとプレゼント**：プレゼントやホリデープロモーションに参加。

    👉 私たちと一緒に探索と創造を始める準備はできましたか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

インデント
=============

インデントとは、コード行の先頭にあるスペースのことを指します。
標準のPythonプログラムと同様に、MicroPythonプログラムも通常は上から下へ実行されます：
各行を順に走査し、インタープリタで実行し、その後次の行へと進みます。
ちょうどシェルで一行ずつ入力するように。
ただし、指示リストを行ごとにブラウズするだけのプログラムはあまり賢くありません。そのためMicroPythonもPythonと同様に、プログラムの実行順序を制御するための独自の方法、つまりインデントを持っています。

print()の前には少なくとも1つのスペースを入れる必要があります。そうしないと、「Invalid syntax（無効な構文）」というエラーメッセージが表示されます。通常は、Tabキーを押してスペースを統一することをお勧めします。

.. code-block:: python

    if 8 > 5:
    print("Eight is greater than Five!")

>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 2
SyntaxError: invalid syntax

同じコードブロック内で同じ数のスペースを使用しなければなりません。そうしないと、Pythonはエラーを返します。

.. code-block:: python

    if 8 > 5:
    print("Eight is greater than Five!")
            print("Eight is greater than Five")
            
>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 2
SyntaxError: invalid syntax
