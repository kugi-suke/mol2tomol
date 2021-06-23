## 指定ディレクトリ内のmol2ファイルをmolファイルに変換
### 1. 指定ディレクトリ内のmol2ファイルのリストを作成
```
sh create_mollist.sh ./dir ./output.txt
```
### 2. pymolを用いてmol2ファイルをmolファイルに変換して保存
```
python mol2tomol.py ./output.txt ./output_dir
```