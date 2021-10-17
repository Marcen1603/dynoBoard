# Instruktionen

## 1. Bilder hinzufügen

Um neue Bilder hinzuzufügen, müssen folgende Schritte durchgeführt werden.

1. Bild in 'images' hinzufügen
2. In Qt Designer das Bild zu den Ressourcen hinzufügen
3. Die entsprechende 'qrc' neu exportieren
4. pyside6-rcc logo.qrc -o logo_rc.py
5. pyside6-rcc ui_images.qrc -o ui_images_rc.py
6. Die entstehenden .py Dateien auf die Ebene der main.py ziehen

## 2. Build dynoDash.ui

Um Änderungen in der UI zu übernehmen, muss diese neu exportiert werden. 
Dies geschieht, nachdem die Änderungen in der .ui Datei vollzogen worden 
sind, bspw. mit dem QtDesigner.

Befehl: pyside6-uic dynoDash.ui -o ui_dynoDash.py

## 3. Executable bauen

Um die UI zu einer .exe zu überführen, wird der folgende Befehl ausgeführt.

Befehl: pyinstaller --name="DynoDashboard" i- "images/logo/logo_ico.ico" --windowed main.py

Dieser Befehl wird auf der Ebene der main.py ausgeführt.
