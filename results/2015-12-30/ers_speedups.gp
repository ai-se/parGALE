# For PNG
set terminal png
set output "ers_speedups.png"

set title "ERS Speed Ups"
set xlabel " Processors "
set ylabel " Speed Up "

set xrange [0:17]
set datafile separator ","
set key left top

plot "ers_consolidated.csv" u 1:4 title 'GALE' with lines, \
	 "ers_consolidated.csv" u 1:7 title 'GALE FS' with lines