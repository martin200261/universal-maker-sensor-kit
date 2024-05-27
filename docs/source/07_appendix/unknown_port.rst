.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Facebook上で、仲間と一緒にRaspberry Pi、Arduino、ESP32をさらに深く探求しましょう。

    **なぜ参加するのか？**

    - **専門的なサポート**：購入後の問題や技術的な課題をコミュニティやチームの助けを借りて解決。
    - **学びと共有**：スキルを向上させるためのヒントやチュートリアルを交換。
    - **限定プレビュー**：新製品発表や予告編に早期アクセス。
    - **特別割引**：最新製品の特別割引を楽しむ。
    - **フェスティブプロモーションとプレゼント**：プレゼントやホリデープロモーションに参加。

    👉 私たちと一緒に探索と創造を始める準備はできましたか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _unknown_com_port:

Always displaying "Unknown COMxx"?
======================================

When plugging the ESP32 into the computer, the Arduino IDE often displays ``Unknown COMxx``. Why does this happen?

.. image:: img/unknown_device.png

This is because the USB driver for ESP32 is different from the regular Arduino Boards. The Arduino IDE can't automatically recognize this board. 

In such a scenario, you need to manually select the correct board by following these steps:

#. Click on **"Select the other board and port"**.

    .. image:: img/unknown_select.png

#. In the search, type **"esp32 dev module"**, then select the board that appears. Afterward, select the correct port and click **OK**.

    .. image:: img/unknown_board.png

#. Now, you should be able to see your board and port in this quick view window.

    .. image:: img/unknown_correct.png