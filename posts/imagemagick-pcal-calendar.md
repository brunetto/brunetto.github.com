<!-- 
.. link: 
.. description: 
.. tags: calendar, code, linux, pcal, scout, imported
.. date: 2013/08/18 22:34:15
.. title: Imagemagick + pcal = calendar
.. slug: imagemagick-pcal-calendar
-->

This is the first version of the script I've created to make a calendar with photos using pcal and Imagemagik. It needs some folder and a "ps-type" font (here ChickenScratchAOE), but I think it's quite easy to understand. I have created some of the files, such as "copertina", before, using Gimp.    

<!-- TEASER_END -->    

````bash
#!/bin/bash

# Parameters
footnote = "..."

# Create ps calendar files and convert them to pdf
echo "Create pdf files of months..."
j=0
for i in $(cat mesi.txt); do
  j=$(echo "$j + 1" | bc);
  pcal -f santi.txt -E -m -B -F monday -o ../mesi/$i.ps -P a4 -b all -t ChickenScratchAOE -d ChickenScratchAOE -C "$footnote" -a it $j 2011 1;
  ps2pdf ../mesi/$i.ps ../mesi/$i.pdf;
done
echo "Done."

# Desaturate and resize the images for the months background
# and put them with opacity 25% on a white canvas. 
echo "Preparing background images..."
for i in $(cat mesi.txt); do
  convert ../immagini/$i.JPG -resize 3508x2480\! -colorspace Gray ../immagini/sfondi-bw/bw-$i.png; composite -dissolve 25% ../immagini/sfondi-bw/bw-$i.png ../immagini/sfondo.png ../immagini/sfondi-bw/diss/bw-diss-$i.png;
done
echo "Done."

# Convert months to png to remove the white background
echo "Converting months to png..."
for i in $(cat mesi.txt); do
  convert -density 500 ../mesi/$i.pdf -transparent white ../mesi/mesi-png/$i.png;
done
echo "Done."

# Combine png months and backgrounds
# converting them back to pdf
echo "Combining png months and backgrounds..."
for i in $(cat mesi.txt); do
 composite ../mesi/mesi-png/$i.png -resize 5847x4132 ../immagini/sfondi-bw/diss/bw-diss-$i.png ../mesi/mesi-finali/finale-$i.pdf
done
echo "Done."

# Resize photos to have smaller files
echo "Resizeing photos and convert to pdf..."
for i in $(cat mesi.txt); do
 convert ../immagini/$i.JPG -resize 3508x2480 ../immagini/pdf/$i.pdf;
done
echo "Done."

#uniamo il tutto
echo "Combine all..."
pdftk ../copertina/copertina.pdf ../immagini/pdf/Gennaio.pdf ../mesi/mesi-finali/finale-Gennaio.pdf ../immagini/pdf/Febbraio.pdf ../mesi/mesi-finali/finale-Febbraio.pdf ../immagini/pdf/Marzo.pdf ../mesi/mesi-finali/finale-Marzo.pdf ../immagini/pdf/Aprile.pdf ../mesi/mesi-finali/finale-Aprile.pdf ../immagini/pdf/Maggio.pdf ../mesi/mesi-finali/finale-Maggio.pdf ../immagini/pdf/Giugno.pdf ../mesi/mesi-finali/finale-Giugno.pdf ../immagini/pdf/Luglio.pdf ../mesi/mesi-finali/finale-Luglio.pdf ../immagini/pdf/Agosto.pdf ../mesi/mesi-finali/finale-Agosto.pdf ../immagini/pdf/Settembre.pdf ../mesi/mesi-finali/finale-Settembre.pdf ../immagini/pdf/Ottobre.pdf ../mesi/mesi-finali/finale-Ottobre.pdf ../immagini/pdf/Novembre.pdf ../mesi/mesi-finali/finale-Novembre.pdf ../immagini/pdf/Dicembre.pdf ../mesi/mesi-finali/finale-Dicembre.pdf ../copertina/quarta.pdf cat output ../calendario-finale.pdf
echo "Done."
````

