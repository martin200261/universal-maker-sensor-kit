.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Facebook上で、仲間と一緒にRaspberry Pi、Arduino、ESP32をさらに深く探求しましょう。

    **なぜ参加するのか？**

    - **専門的なサポート**：購入後の問題や技術的な課題をコミュニティやチームの助けを借りて解決。
    - **学びと共有**：スキルを向上させるためのヒントやチュートリアルを交換。
    - **限定プレビュー**：新製品発表や予告編に早期アクセス。
    - **特別割引**：最新製品の特別割引を楽しむ。
    - **フェスティブプロモーションとプレゼント**：プレゼントやホリデープロモーションに参加。

    👉 私たちと一緒に探索と創造を始める準備はできましたか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _pi_lesson31_pump:

Lesson 31: Centrifugal Pump
==================================

In this lesson, you will learn how to control a pump using a Raspberry Pi. You'll learn how to write a Python script to activate the pump, control its speed, and then stop it after a set period. This project provides a basic understanding of pump control through GPIO interfacing and Python programming, making it a suitable starting point for beginners interested in Raspberry Pi and simple pump applications.

Required Components
--------------------------

In this project, we need the following components. 

It's definitely convenient to buy a whole kit, here's the link: 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ITEMS IN THIS KIT
        - LINK
    *   - Universal Maker Sensor Kit
        - 94
        - |link_umsk|

You can also buy them separately from the links below.

.. list-table::
    :widths: 30 20
    :header-rows: 1

    *   - Component Introduction
        - Purchase Link

    *   - Raspberry Pi 5
        - \-
    *   - :ref:`cpn_pump`
        - \-
    *   - :ref:`cpn_l9110`
        - \-


Wiring
---------------------------

.. image:: img/Lesson_31_Pump_Pi_bb.png
    :width: 100%


Code
---------------------------

.. code-block:: python

   from gpiozero import Motor
   from time import sleep
   
   # Define pump pins
   pump = Motor(forward=17, backward=27)  # Using Raspberry Pi GPIO pin numbers
   
   # Activate the pump
   pump.forward(speed=1)  # Set pump speed, range is 0 to 1
   sleep(5)               # Run the pump for 5 seconds
   
   # Deactivate the pump
   pump.stop()            # Stop the pump



Code Analysis
---------------------------

#. Import Libraries
   
   The ``gpiozero`` library is used for controlling the motor, and the ``time`` library's ``sleep`` function is for delays.

   .. code-block:: python

      from gpiozero import Motor
      from time import sleep

#. Define Pump Pins
   
   A ``Motor`` object is created with two GPIO pins: one for forward and one for backward operation. In this case, GPIO 17 and 27 are used.

   .. code-block:: python

      pump = Motor(forward=17, backward=27)

#. Activate the pump
   
   The motor is activated in the forward direction with a specified speed using ``pump.forward(speed=1)``. The speed parameter ranges from 0 (stopped) to 1 (full speed). The motor runs for 5 seconds, as defined by ``sleep(5)``.

   .. code-block:: python

      pump.forward(speed=1)
      sleep(5)

#. Deactivate the pump
   
   The motor is stopped using ``pump.stop()``. This is essential for safely halting the motor's operation after the required duration.

   .. code-block:: python

      pump.stop()