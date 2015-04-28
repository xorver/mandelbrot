f(x) = k/x
g(x) = P / (x + d)**B

k = 20000
P = 6000
d = -1.5
B = 0.3

FIT_LIMIT = 1e-10
fit f(x) 'statistics2.txt' using 2:3 via k
fit g(x) 'statistics2.txt' using 2:3 via P, d, B

# Setup terminal
set terminal png size 640,480 enhanced font 'Verdana,10'
set border linewidth 1.5
set style line 1 linecolor rgb '#0060ad' linetype 1 linewidth 2
set style line 2 linecolor rgb '#dd181f' linetype 1 linewidth 2
set style line 3 lc rgb '#06f0ad' lt 1 lw 2 pt 7 ps 0.1

# Plot f(x) and g(x)
set output 'diagram.png'
set xrange [1:500]
set yrange [0.1:100000]

set logscale y 10
plot 'statistics2.txt' using 2:3 title 'datapoints' with lines linestyle 1, f(x) title 'k/x' with lines linestyle 2, g(x) title 'P / (x + d)**B' with lines linestyle 3