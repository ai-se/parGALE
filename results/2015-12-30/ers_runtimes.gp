# For PNG
set terminal png
set output "ers_runtimes.png"

set title "ERS Runtimes"
set xlabel " Processors "
set ylabel " Runtimes(secs) "

set xrange [0:17]
set datafile separator ","

plot "ers_consolidated.csv" u 1:2 title 'GALE' with lines, \
	 "ers_consolidated.csv" u 1:5 title 'GALE FS' with lines