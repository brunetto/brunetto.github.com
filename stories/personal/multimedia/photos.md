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
* [Sigfrido Corradi blog](http://sigfridocorradi.wordpress.com/)
* [Garry](http://www.flickr.com/photos/garry61/)
* [Jonathan Besler](http://500px.com/JonathanBesler)
* [Anton Jankovoy](http://500px.com/jankovoy)
<!--* [Gergo](http://www.flickr.com/photos/pgaalien/) [Antal](http://500px.com/alienart)[John Tisbury](johntisbury.deviantart.com)* [John Suler](http://www.flickr.com/photos/jsuler)-->
* [Lincoln Harrison](http://500px.com/Hakka), [on Flickr](http://www.flickr.com/photos/hakka69), [personal site](http://www.lincolnharrison.com/)
* [Peter Greig](http://www.flickr.com/photos/st1nkypete/)
* [Sébastien GABORIT](http://www.flickr.com/photos/90291911@N08/)
* [Javier Pérez](http://instagram.com/cintascotch)

#### Lightpainting

* [10 Amazing Light Painting Photographers You Should Start Following Right Now](http://petapixel.com/2013/08/27/10-amazing-light-painting-photographers/)
* [tackyshack](http://www.tackyshack.net/), [on Flickr](http://www.flickr.com/photos/tackyshack/), 
* [Jan Leonardo](http://www.lightart-photography.de/)
* [Hannu Huhtamo](http://www.flickr.com/photos/hhuhtamo/)
* [Trevor Williams](http://fiz-iks.com/)
* [Light Junkies Flickr group](http://www.flickr.com/groups/lightjunkies/)
* [Dana Maltby](http://twincitiesbrightest.com/)
* [Brian Matthew Hart](https://sites.google.com/site/brianmatthewhart/recentextrapolations)
* [Janne Parviainen](http://jannepaint.wix.com/jannepaint)
* [Patrick Rochon](http://www.patrickrochon.com/), [RedBull collaboration](http://petapixel.com/2013/04/11/experimental-light-painting-photographs-with-lights-strapped-to-wakeboards/)
* [Michael Ross](http://mrossphoto.com/wordpress32/)
* [Dennis Calvert](http://denniscalvert.net/blog/)

### Amateur

* [Enrico Prenna](http://www.flickr.com/photos/enricoprenna/)
* [Giorgio Ruberti](http://www.flickr.com/photos/giorgio_ruberti/)

## Sites

* [Flickr](http://www.flickr.com/)
* [500px](http://500px.com/)

### Strangeness etc.

* [Lego bloks camera](http://petapixel.com/2012/07/31/a-nifty-panoramic-pinhole-camera-made-with-lego-blocks/)
* [Lego bloks camera 2] (http://petapixel.com/2011/03/31/working-4x5-camera-created-with-lego/)

## Tricks

* [Snowflakes Photography](http://chaoticmind75.blogspot.ru/2013/08/my-technique-for-snowflakes-shooting.html)

## HDR/blending

* Wikipedia
* QTPSF-gui
* Gimp

## Panoramas

* Hugin
* [Planetoids Gallery](http://www.visualswirl.com/inspiration/22-amazing-planetoid-photographs/)
* [Create planetoids](http://haloramics.tiedtheleader.com/PlanetoidHowTo/PlanetoidHowTo.html)
* [krpano](http://krpano.com/)

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
* stich two images
````bash
convert one.png two.png -append stiched.png
````
to stich the images vertically, `+append` to stich them horizontally

## My galleries

* 
* 