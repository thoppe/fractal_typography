# Fractal Typography
_(sierpinski, knuth, memes, and a Turning complete system)_

*[Travis Hoppe](http://thoppe.github.io/)*
----------
[https://github.com/thoppe/fractal_typography](https://github.com/thoppe/fractal_typography)

====
Donald Knuth created TeX; wrote a a [diatribe](http://www-cs-faculty.stanford.edu/~uno/cm.html) on the shape of $\delta$.
!(figures/knuth.jpg) <<height:270px;transparent>> 
!(figures/typography.jpg) <<height:270px;transparent>>


## $i\hbar\frac{\partial}{\partial t} \Psi(\mathbf{r},t) = \left [ \frac{-\hbar^2}{2\mu}\nabla^2 + V(\mathbf{r},t)\right ] \Psi(\mathbf{r},t)$
Used by physics & mathematics to make equations and papers beautiful.

====
# Fractals
self-similar patterns governed by a rule

!(figures/mand2.jpg) <<height:400px;transparent>>
!(figures/mand.gif) <<height:400px;transparent>>

====*
# Fractals via memes
the inception arguement

!(figures/800px-Sup_dawg.jpg)
=====*
## Fractals + typography = ?
=====
### Sierpinski's carpet
will be our "template"
!(figures/sierpinski.gif) <<height:650px;transparent>>
=====*
### Source image
!(figures/s1.png) <<height:650px;transparent>>
=====*
### Compile and repeat
Used `pdflatex` to compile and copy the result back into `source.pdf`.

    \documentclass{standalone}
    \usepackage{graphicx}
    \newcommand{\A}{\includegraphics[width=50cm]{pdf/source.pdf}}
    
    \begin{document}
    \begin{center}
    \begin{tabular}{lll}
    \A & \A & \A\\
    \A &    & \A\\
    \A & \A & \A
    \end{tabular}
    \end{center}
    \end{document}

====
### [Level 2 (8 copies)](pdf/level_002.pdf)
!(figures/s2.png) <<height:650px;transparent>>
====*
### [Level 3 (512 copies)](pdf/level_003.pdf)
!(figures/s3.png) <<height:650px;transparent>>
====*
### [Level 4 (4096 copies)](pdf/level_004.pdf)
!(figures/s4.png) <<height:650px;transparent>>
====*
### [Level 5 (32768 copies)](pdf/level_005.pdf)
!(figures/s5.png) <<height:650px;transparent>>
====*
### Level 6 (262144 copies)

crashes my PDF viewer

used to crash Google Docs (funny story...)

...

Can we go deeper?
====
## How big are the files?
compiled to depth 1000

    -rw-r--r-- 1 hoppeta hoppeta 27664 Dec  8 13:52 level_001.pdf
    -rw-r--r-- 1 hoppeta hoppeta 28753 Dec  8 13:52 level_002.pdf
    -rw-r--r-- 1 hoppeta hoppeta 29132 Dec  8 13:52 level_003.pdf
    -rw-r--r-- 1 hoppeta hoppeta 29539 Dec  8 13:52 level_004.pdf
    -rw-r--r-- 1 hoppeta hoppeta 29938 Dec  8 13:52 level_005.pdf
    -rw-r--r-- 1 hoppeta hoppeta 30338 Dec  8 13:52 level_006.pdf
    ...
    -rw-r--r-- 1 hoppeta hoppeta 431996 Dec  8 11:10 level_999.pdf

_Not exponential growth...?_

====*
## How much information in each PDF?
!(figures/depth.png) <<height:550px;transparent>>
only 41 unique bytes per level!  (FYI PDF's are Turing complete)
====

# Thanks, you!
Tweet thoughts to [@metasemantic](https://twitter.com/metasemantic)!