# Blender Blosm’s Objects Exporter

## これは何ですか？
BlenderのOpenStreetMapなどのインポーターBlosmでインポートした3DマップのオブジェクトをオブジェクトごとにGLTFファイルにエクスポートするスクリプトです

## 使い方
1. このスクリプトをBlenderのテキストエディタにコピーします。
2. 10行目の「save_dir = "c:\\models\\」をGLTFを出力したいフォルダに書きかえます。
3. Alt+pキーを押します

## ノート

Blosmでbuildingsをインポートする前にindividualにチェックを入れておきます。オブジェクト1つにまとめてインポートだと1つ1つを選択してエクスポートできないので。


## About

This Blender script exports the objects of city map loaded by Blosm (OpenStreetMap etc Importer) as individual objects to gltf files.

## How to use
1. Copy this script to Blender's Text Editor.
2. Change "save_dir = "c:\\models\\" to your folder path at Line 10.
3. Hit Alt+p.

## Note

Check individual check button before importing buildings with Blosm. Because it would not export objects individualiy from the one object.

