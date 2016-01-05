# For PNG
set terminal png
set output "wpt_runtimes.png"

set title "WPT Runtimes"
set xlabel " Processors "
set ylabel " Runtimes(secs) "

set xrange [0:17]
set datafile separator ","

plot "wpt_consolidated.csv" u 1:2 title 'GALE' with lines, \
	 "wpt_consolidated.csv" u 1:5 title 'GALE FS' with lines