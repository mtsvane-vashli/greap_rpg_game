# RPG Game

\*注: こちらでは markdown の更新は行わない。`main` を最新とする。

## 開発の前に

前提知識としてコーディングにおいて注意してほしいことなどを以下にまとめました。必要なところだけでも一読してもらえると嬉しいです。いいファイル分けができてなくて申し訳ない…(随時更新予定)

- [可読性について](markdown/readability.md) (2024/07/10 更新)

- [開発における基本方針](markdown/policy.md) (2024/07/10 更新)

## ブランチ

`*<branch>*` はこのブランチ

```
------- main
    |--- *sample/rpg-map*
```

`main`: ここに完成品を作っていく

`sample/rpg-map`: @mtsvane-vashli に仮に作ってもらったやつを残しておくためのブランチ

## ファイル構造

## Git, GitHub の使い方

Git の構想や仕組みについては省略する。(各自調べてほしい。余裕があれば説明は追加するかも。) よって、以下は Git と GitHub は特に区別せず、まとめて GitHub と呼称する。ここでは GitHub を扱うためのおすすめのソフト、GitHub の今回の管理方法について記述する。

### GitHub Desktop

ローカルリポジトリ (個人のパソコン内のディレクトリ) とリモートリポジトリ (≒ GitHub に作ったオンライン上の共有用ディレクトリ) 間の操作をするための、GUI アプリケーション。ローカルディレクトリに clone (≒ 最初の pull (pull: リモートリポジトリ上の変更をローカルディレクトリにダウンロードすること)) したり、ブランチ (コードを変更するときに、複数人による変更内容が *~~コンフリクト (衝突、競合)~~ 競合しないようにするために作る分岐) を作って publish (≒ ブランチの push) したり、ローカルディレクトリのブランチを切り替えたり、変更を commit (≒ どの部分の何を変更したかを変更ログとして保存すること) して push (リモートリポジトリに commit をアップロードすること) したり、などといった操作をコマンドなしで容易にできるため非常に便利。以下、ダウンロードの手順のページ (ページ内にダウンロードページのリンクあり):

https://docs.github.com/ja/desktop/installing-and-authenticating-to-github-desktop/installing-github-desktop

なお、Git だけインストールして、VSCode で拡張機能を用いて、1つのソフトで完結するのもアリ。ここら辺は個人の好みで構わない。GitHub Desktop を強要するわけではないので、既に好みのものがあるならそちらを、今環境がないならこちらをおすすめしたい。

*修正: コンフリクト(conflict) とは、あるブランチを別のブランチに merge (統合) するときに、変更内容が衝突すること。同じ行を変更したときなどに起きる。~~これが起きた時の対処は…正直分かんないので起きないように気を付けて避けたいところ。~~

(上の括弧だらけの説明、見づらければどうにかするんで言ってください)

### GitHub での開発

上でも少し触れたが、複数人での開発では、全員が main ブランチをいじると大変なことになるので、各自個人作業用のブランチを作って、そこで編集、commit、push をして、ひと段落ついたら pull request を出して確認が終わったら main に marge という進め方が基本である。ブランチ名は "main" などでなければ何でもいいのではあるが、一応今回名づけ方は統一しておこうかと思う。

#### ブランチ名

以下の書式にしようと思う。なお、必要に応じて柔軟に逸脱してよいことにする。

```
(変更の種類)/(変更するファイル or 機能)/(変更者の名前)

ex: dev/State_1/Saito
```

仮に参考例として置くための場合は `dev` のところを `sample` にするとか。
