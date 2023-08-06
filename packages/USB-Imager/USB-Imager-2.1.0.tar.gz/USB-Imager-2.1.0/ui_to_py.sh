#!/usr/bin/env bash

### DESCRIPTION ###
# Generate python file from .ui file

SOURCE_PATH="usb_imager/resources"
TARGET_PATH="usb_imager"


if which pyside6-uic >/dev/null; then
    SOURCE_UI="mainwindow.ui"
    TARGET_PY="ui_mainwindow.py"
    pyside6-uic --no-autoconnection\
                --generator python\
                "$SOURCE_PATH/$SOURCE_UI"\
                --output "$TARGET_PATH/$TARGET_PY" && \
    echo "'$TARGET_PY' was successfully generated in $TARGET_PATH"

    SOURCE_UI="targetwidget.ui"
    TARGET_PY="ui_targetwidget.py"
    pyside6-uic --no-autoconnection\
                --generator python\
                "$SOURCE_PATH/$SOURCE_UI"\
                --output "$TARGET_PATH/$TARGET_PY" && \
    echo "'$TARGET_PY' was successfully generated in $TARGET_PATH"
else
    echo "pyside6-uic not found!"; exit 1
fi
