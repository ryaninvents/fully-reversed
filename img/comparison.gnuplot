set title "Cross-section of encoded values"
set terminal png enhanced font "cmr10,16" size 800,600
set output "comparison.png"
set xlabel "Image position (pixels)"
set ylabel "Encoded projector value (pixels)"
set key inside top left horizontal
plot [610:920]  'plotdata.dat' using 1:($2>0?$2:1/0) with lines title 'Binary',  'plotdata.dat' using 1:($3>0?$3:1/0) with lines title 'Hybrid'
