# For PNG
set terminal png
set output "wpt_speedups.png"

set title "WPT Speed Ups"
set xlabel " Processors "
set ylabel " Speed Up "

set xrange [0:17]
set datafile separator ","
set key left top

plot "wpt_consolidated.csv" u 1:4 title 'GALE' with lines, \
	 "wpt_consolidated.csv" u 1:7 title 'GALE FS' with lines