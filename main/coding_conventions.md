# コーディング規約
1. chapter は main.tex ファイル内に書き，section 以下は (input).tex ファイル内に書く

1. 相互参照は wtref.sty の記法に則って記す
```latex
\usepackage{wtref}
% 参照の定義
\newref{part,chap,sec,subsec,subsubsec}
\newref{equ,tab,fig}
\newref{thm,prob,defi,lem,cor,eg,prop,nota,supple}

\setrefstyle{part}{prefix=第, suffix=部}
\setrefstyle{chap}{prefix=第, suffix=章}
\setrefstyle{sec}{prefix=第, suffix=節}
\setrefstyle{subsec}{prefix=第, suffix=小節}
\setrefstyle{subsubsec}{prefix=第, suffix=小々節}

\setrefstyle{equ}{refcmd=(\ref{#1}), prefix=式}
\setrefstyle{tab}{prefix=表}
\setrefstyle{fig}{prefix=図}

\setrefstyle{prob}{prefix=問}
\setrefstyle{thm}{prefix=定理}
\setrefstyle{defi}{prefix=定義}
\setrefstyle{lem}{prefix=補題}
\setrefstyle{cor}{prefix=系}
\setrefstyle{eg}{prefix=例}
\setrefstyle{prop}{prefix=命題}
\setrefstyle{nota}{prefix=記法}
\setrefstyle{supple}{prefix=補足}
```

例えば，
```latex
\begin{align}
    \sum_{n = 1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6} \equlabel{Euler}
    \\
    a^{p - 1} \equiv 1 \pmod{p} \equlabel{Fermat}
    \\
    z(1 - z) w^{(2)}(z) + \{c - (a + b + 1) z} w^{(1)}(z) - a b w(z) = 0 \equlabel{Gauss}
\end{align}
```
として，本文中で，
```latex
ここで，\equref{Euler,Fermat,Gauss}に拠ると......
```
とすると，
> ここで，式(1), (2), (3)に拠ると......

のように出力される。
特に，昔のソースをコピペすると
```latex
\label{eq:a}, \eqref{eq:a}
```
などが残っている恐れがあるので注意。


また，問題を，
```latex
\begin{prob}\problabel{hoge}
    (problem)
\end{prob}
```
> 問題 1.1. (problem)

とした場合，解答は，
```latex
\begin{ans}{hoge}
    (answer)
\end{ans}
```
とすれば，
> 問題 1.1. (answer)

のようになる。
