<!-- 
.. link: 
.. description: 
.. tags: 
.. date: 2013/08/21 12:00:15
.. title: Photos
.. slug: photos
-->

Some links regarding the world of photography...    

## Photographers
### Professional
* [Juza Photo](http://www.juzaphoto.com/home.php?l=it)
* [Sigfrido Corradi](http://www.sigfridocorradi.net/)
* [Garry](http://www.flickr.com/photos/garry61/)
* [Jonathan Besler](http://500px.com/JonathanBesler)
* [Anton Jankovoy](http://500px.com/jankovoy)
<!--* [Gergo](http://www.flickr.com/photos/pgaalien/) [Antal](http://500px.com/alienart)
[John Tisbury](johntisbury.deviantart.com)
-->

### Amateur

* [Enrico Prenna](http://www.flickr.com/photos/enricoprenna/)
* [Giorgio Ruberti](http://www.flickr.com/photos/giorgio_ruberti/)

## Sites

* [Flickr](http://www.flickr.com/)
* [500px](http://500px.com/)

## HDR/blending

* Wikipedia
* QTPSF-gui
* Gimp

## Panoramas

* Hugin
* [Planetoids Gallery](http://www.visualswirl.com/inspiration/22-amazing-planetoid-photographs/)
* [Create planetoids](http://haloramics.tiedtheleader.com/PlanetoidHowTo/PlanetoidHowTo.html)

## CLI tricks

* Align images
````bash
align_image_stack -a <aligned images prefix> -p <.pto file name for hugin> -o <hdr file name>
* Blend images
````bash
enfuse -o <output file> <input files, also as prefix???.ext>
````
* Create GIF
````bash
convert -delay <delay between frames in 1/100 secs> -loop <number of loops, 0==infinite> -size <w>x<h> <output>.gif
````
* Resize

* Mosaic
1. [ShapeCollage](http://pollycoke.org/2009/02/19/%C2%ABfacce-da-pollycoke%C2%B2%C2%BB-con-shape-collage-howto/)
2. Metapixel, [site](http://www.complang.tuwien.ac.at/schani/metapixel/), [repo](https://github.com/schani/metapixel/blob/master/README)
````bash
metapixel-prepare -r <photos source> <thumbnails dest> --width=<width, eg 32> --height=<height, eg 32>
metapixel --metapixel <input photo> <output mosaic> --library <thumbnails dir> \
--scale=<original scale factor, eg 10> \
--distance=<distance between replicated thumbnails, eg 300> \
--cheat=<original image overlay percentage>
````
you can use the `--collage` option instead --metapixel for a slower but better result and 

## My galleries

* 
* 