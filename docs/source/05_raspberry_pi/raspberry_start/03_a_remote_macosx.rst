.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Communityへようこそ！Facebook上で、仲間と一緒にRaspberry Pi、Arduino、ESP32をさらに深く探求しましょう。

    **なぜ参加するのか？**

    - **専門的なサポート**：購入後の問題や技術的な課題をコミュニティやチームの助けを借りて解決。
    - **学びと共有**：スキルを向上させるためのヒントやチュートリアルを交換。
    - **限定プレビュー**：新製品発表や予告編に早期アクセス。
    - **特別割引**：最新製品の特別割引を楽しむ。
    - **フェスティブプロモーションとプレゼント**：プレゼントやホリデープロモーションに参加。

    👉 私たちと一緒に探索と創造を始める準備はできましたか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _remote_macosx:

Mac OS X user
==========================

For Mac users, accessing the Raspberry Pi desktop directly via VNC is more convenient than from the command line. You can access it via Finder by entering the set account password after enabling VNC on the Raspberry Pi side.

Note that this method does not encrypt communication between the Mac and Raspberry Pi. 
The communication will take place within your home or business network, so even if it's unprotected, it won't be an issue. 
However, if you are concerned about it, you can install a VNC application such as `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_.

Alternatively it would be handy if you could use a temporary monitor (TV), mouse and keyboard to open the Raspberry Pi desktop directly to set up VNC. 
If not, it doesn't matter, you can also use the SSH command to open the Raspberry Pi's Bash shell and then using the command to set up the VNC.


* :ref:`have_temp_monitor`
* :ref:`no_temp_monitor`


.. _have_temp_monitor:

Have Temporarily Monitor (or TV)?
---------------------------------------------------------------------

#. Connect a monitor (or TV), mouse and keyboard to the Raspberry Pi and power it on. Select the menu according to the numbers in the figure.


   .. image:: img/mac_01.png
       :align: center

#. The following screen will be displayed. Set **VNC** to **Enabled** on the **Interfaces** tab, and click **OK**.

   .. image:: img/mac_02.png
       :align: center


#. A VNC icon appears on the upper right of the screen and the VNC server starts.

   .. image:: img/mac_03.png
       :align: center


#. Open the VNC server window by clicking on the **VNC** icon, then click on the **Menu** button in the top right corner and select **Options**.

   .. image:: img/mac_04.png
       :align: center

#. You will be presented with the following screen where you can change the options.

   .. image:: img/mac_05.png
       :align: center

   Set **Encryption** to **Prefer off** and **Authentication** to **VNC password**. 
    
#. When you click the **OK** button, the password input screen is displayed. You can use the same password as the Raspberry pi password or a different password, so enter it and click **OK**. 

   .. image:: img/mac_06.png
       :align: center

   You are now ready to connect from your Mac. It's okay to disconnect the monitor.

**From here, it will be the operation on the Mac side.**

#. Now, select **Connect to Server** from the Finder's menu, which you can open by right-clicking.

   .. image:: img/mac_07.png
       :align: center

#. Type in ``vnc://<username>@<hostname>.local`` (or ``vnc://<username>@<IP address>``). After entering, click **Connect**.

   .. image:: img/mac_08.png
       :align: center


#. You will be asked for a password, so please enter it.

   .. image:: img/mac_09.png
       :align: center

#. The desktop of the Raspberry pi will be displayed, and you will be able to operate it from the Mac as it is.

   .. image:: img/mac_10.png
       :align: center

.. _no_temp_monitor:

Don't Have Temporarily Monitor (or TV)?
---------------------------------------------------------------------------

* You can apply the SSH command to open the Raspberry Pi's Bash shell.
* Bash is the standard default shell for Linux.
* The shell itself is a command (instruction) when the user uses Unix/Linux.
* Most of what you need to do can be done through the shell.
* After setting up the Raspberry pi side, you can access the desktop of the Raspberry Pi using the **Finder** from the Mac.


#. Type ``ssh <username>@<hostname>.local`` to connect to the Raspberry Pi.


   .. code-block:: shell

       ssh pi@raspberrypi.local


   .. image:: img/mac_11.png


#. The following message will be displayed only when you log in for the first time, so enter **yes**.

   .. code-block::

       The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
       ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
       This key is not known by any other names
       Are you sure you want to continue connecting (yes/no/[fingerprint])?


#. Enter the password for the Raspberry pi. The password you enter will not be displayed, so be careful not to make a mistake.

   .. code-block::

       pi@raspberrypi.local's password: 
       Linux raspberrypi 5.15.61-v8+ #1579 SMP PREEMPT Fri Aug 26 11:16:44 BST 2022 aarch64

       The programs included with the Debian GNU/Linux system are free software;
       the exact distribution terms for each program are described in the
       individual files in /usr/share/doc/*/copyright.

       Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
       permitted by applicable law.
       Last login: Thu Sep 22 12:18:22 2022
       pi@raspberrypi:~ $ 


    

#. Set up your Raspberry Pi so that you can log in via VNC from your Mac once you have successfully logged into it. The first step is to update your operating system by running the following commands.

   .. code-block:: shell

       sudo apt update
       sudo apt upgrade


   ``Do you want to continue? [Y/n]``, Enter ``Y`` when prompted.

   It may take some time for the update to finish. (It depends on the amount of updates at that time.)


#. Enter the following command to enable the **VNC Server**.

   .. code-block:: shell

       sudo raspi-config

#. The following screen will be displayed. Select **3 Interface Options** with the arrow keys on the keyboard and press the **Enter** key.

   .. image:: img/mac_12.png
       :align: center

#. Then select **VNC**.

   .. image:: img/mac_13.png
       :align: center

#. Use the arrow keys on the keyboard to select **<Yes>** -> **<OK>** -> **<Finish>** to complete the setup.

   .. image:: img/mac_14.png
       :align: center


#. Now that the VNC server has started, let's change the settings for connecting from a Mac.

   To specify parameters for all programs for all user accounts on the computer, create ``/etc/vnc/config.d/common.custom``.

   .. code-block:: shell

       sudo nano /etc/vnc/config.d/common.custom

   After entering ``Authentication=VncAuthenter``, press ``Ctrl+X`` -> ``Y`` -> ``Enter`` to save and exit.

   .. image:: img/mac_15.png
       :align: center

#. In addition, set a password for logging in via VNC from a Mac. You can use the same password as the Raspberry pi password or a different password. 


   .. code-block:: shell

       sudo vncpasswd -service


#. Once the setup is complete, restart the Raspberry Pi to apply the changes.

   .. code-block:: shell

       sudo sudo reboot

#. Now, select **Connect to Server** from the **Finder**'s menu, which you can open by right-clicking.

   .. image:: img/mac_16.png
       :align: center

#. Type in ``vnc://<username>@<hostname>.local`` (or ``vnc://<username>@<IP address>``). After entering, click **Connect**.

   .. image:: img/mac_17.png
       :align: center


#. You will be asked for a password, so please enter it.

   .. image:: img/mac_18.png
       :align: center

#. The desktop of the Raspberry pi will be displayed, and you will be able to operate it from the Mac as it is.

   .. image:: img/mac_19.png
       :align: center
