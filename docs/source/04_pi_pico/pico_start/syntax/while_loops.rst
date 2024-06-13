.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Facebook上で、仲間と一緒にRaspberry Pi、Arduino、ESP32をさらに深く探求しましょう。

    **なぜ参加するのか？**

    - **専門的なサポート**：購入後の問題や技術的な課題をコミュニティやチームの助けを借りて解決。
    - **学びと共有**：スキルを向上させるためのヒントやチュートリアルを交換。
    - **限定プレビュー**：新製品発表や予告編に早期アクセス。
    - **特別割引**：最新製品の特別割引を楽しむ。
    - **フェスティブプロモーションとプレゼント**：プレゼントやホリデープロモーションに参加。

    👉 私たちと一緒に探索と創造を始める準備はできましたか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _py_syntax_while:

While ループ
====================

``while`` 文は、プログラムをループで実行するために使用されます。つまり、特定の条件下でプログラムを繰り返し実行し、同じタスクを何度も処理するために使用されます。

その基本的な形式は次のとおりです：

.. code-block:: python

    while test expression:
        Body of while


``while`` ループでは、最初に ``test expression`` を確認します。 ``test expression`` が ``True`` と評価される場合にのみ、while の本体に入ります。1回の反復の後、再び ``test expression`` を確認します。このプロセスは、 ``test expression`` が ``False`` と評価されるまで続きます。

MicroPythonでは、 ``while`` ループの本体はインデントによって決定されます。

本体はインデントで始まり、最初の非インデント行で終了します。

Pythonは任意の非ゼロ値を ``True`` と解釈します。Noneと0は ``False`` と解釈されます。

**while ループフローチャート**

.. image:: img/while_loop.png



.. code-block:: python

    x = 10

    while x > 0:
        print(x)
        x -= 1

>>> %Run -c $EDITOR_CONTENT
10
9
8
7
6
5
4
3
2
1


Break 文
--------------------

break 文を使用すると、while 条件が真であってもループを停止できます。



.. code-block:: python

    x = 10

    while x > 0:
        print(x)
        if x == 6:
            break
        x -= 1

>>> %Run -c $EDITOR_CONTENT
10
9
8
7
6

else を伴う while ループ
---------------------------
``if`` ループと同様に、 ``while`` ループにもオプションの ``else`` ブロックを持つことができます。

``while`` ループの条件が ``False`` と評価された場合、 ``else`` 部分が実行されます。



.. code-block:: python

    x = 10

    while x > 0:
        print(x)
        x -= 1
    else:
        print("Game Over")

>>> %Run -c $EDITOR_CONTENT
10
9
8
7
6
5
4
3
2
1
Game Over