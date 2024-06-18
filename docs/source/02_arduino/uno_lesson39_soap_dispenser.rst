.. note::

   Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

   **Warum beitreten?**

   - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
   - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
   - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
   - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
   - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

   👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _uno_lesson39_soap_dispenser:

Lektion 39: Automatischer Seifenspender
============================================

Das Projekt „Automatischer Seifenspender“ verwendet ein Arduino Uno Board zusammen mit einem Infrarot-Hindernisvermeidungssensor und einer Wasserpumpe. Der Sensor erkennt die Anwesenheit eines Objekts wie einer Hand, wodurch die Wasserpumpe aktiviert wird, um Seife zu spenden.

Benötigte Komponenten
--------------------------

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist definitiv praktisch, ein ganzes Kit zu kaufen, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ITEMS IN THIS KIT
        - LINK
    *   - Universal Maker Sensor Kit
        - 94
        - |link_umsk|

Sie können sie auch separat über die untenstehenden Links kaufen.

.. list-table::
    :widths: 30 20
    :header-rows: 1

    *   - Component Introduction
        - Purchase Link

    *   - Arduino UNO R3 or R4
        - |link_Uno_R3_buy|
    *   - :ref:`cpn_ir_obstacle`
        - |link_obstacle_avoidance_module_buy|
    *   - :ref:`cpn_pump`
        - \-
    *   - :ref:`cpn_l9110`
        - \-
    *   - :ref:`cpn_power_module`
        - \-
    *   - :ref:`cpn_breadboard`
        - |link_breadboard_buy|
        

Verkabelung
---------------------------

.. image:: img/Lesson_39_Automatic_soap_dispenser_uno_bb.png
    :width: 100%


Code
---------------------------

.. raw:: html

    <iframe src=https://create.arduino.cc/editor/sunfounder01/47ef3a59-afe1-40a8-9b36-1ff5db59af15/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Code-Analyse
---------------------------

Die Hauptidee dieses Projekts besteht darin, ein berührungsloses Seifenspender-System zu erstellen. Der Infrarot-Hindernisvermeidungssensor erkennt, wenn sich ein Objekt (wie eine Hand) nähert. Beim Erkennen eines Objekts sendet der Sensor ein Signal an das Arduino, das wiederum die Wasserpumpe aktiviert, um Seife auszugeben. Die Pumpe bleibt für eine kurze Zeit aktiv, gibt Seife ab und schaltet sich dann wieder aus.

#. **Definition der Pins für den Sensor und die Pumpe**

   In diesem Code-Schnipsel definieren wir die Arduino-Pins, die mit dem Sensor und der Pumpe verbunden sind. Wir definieren Pin 7 als Sensor-Pin und verwenden die Variable ``sensorValue``, um die vom Sensor gelesenen Daten zu speichern. Für die Wasserpumpe verwenden wir zwei Pins, 9 und 10.
   
   .. code-block:: arduino
   
      const int sensorPin = 7;
      int sensorValue;
      const int pump1A = 9;
      const int pump1B = 10;

#. **Einrichtung des Sensors und der Pumpe**

   In der ``setup()``-Funktion definieren wir die Modi der verwendeten Pins. Der Sensor-Pin wird auf ``INPUT`` gesetzt, da er zur Datenempfangung vom Sensor verwendet wird. Die Pumpen-Pins werden auf ``OUTPUT`` gesetzt, da sie Befehle an die Pumpe senden. Wir stellen sicher, dass der Pin ``pump1B`` im ``LOW``-Zustand (ausgeschaltet) startet, und beginnen die serielle Kommunikation mit einer Baudrate von 9600.

   .. code-block:: arduino
   
      void setup() {
        pinMode(sensorPin, INPUT);
        pinMode(pump1A, OUTPUT);    
        pinMode(pump1B, OUTPUT);    
        digitalWrite(pump1B, LOW);  
        Serial.begin(9600);
      }

#. **Kontinuierliche Überprüfung des Sensors und Steuerung der Pumpe**

   In der ``loop()``-Funktion liest das Arduino ständig den Wert vom Sensor mit ``digitalRead()`` und weist ihn ``sensorValue()`` zu. Es druckt diesen Wert dann zur Fehlersuche auf den seriellen Monitor. Wenn der Sensor ein Objekt erkennt, ist ``sensorValue()`` 0. In diesem Fall wird ``pump1A`` auf ``HIGH`` gesetzt, wodurch die Pumpe aktiviert wird, und eine Verzögerung von 700 Millisekunden ermöglicht der Pumpe, Seife abzugeben. Die Pumpe wird dann durch Setzen von ``pump1A`` auf ``LOW`` deaktiviert, und eine Verzögerung von 1 Sekunde gibt dem Benutzer Zeit, seine Hand zu entfernen, bevor der Zyklus erneut beginnt.

   .. note:: 
   
      Wenn der Sensor nicht richtig funktioniert, stellen Sie den IR-Sender und -Empfänger parallel ein. Außerdem können Sie die Erfassungsreichweite mit dem eingebauten Potentiometer anpassen.

   .. code-block:: arduino
   
      void loop() {
        sensorValue = digitalRead(sensorPin);
        Serial.println(sensorValue);
        if (sensorValue == 0) {  
          digitalWrite(pump1A, HIGH);
          delay(700);
          digitalWrite(pump1A, LOW);
          delay(1000);
        }
      }
