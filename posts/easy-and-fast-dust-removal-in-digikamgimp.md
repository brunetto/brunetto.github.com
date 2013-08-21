<!-- 
.. link: 
.. description: 
.. tags: digikam, dust, gimp, mask, photography, removal, spot, imported
.. date: 2012-09-04
.. title: Easy and fast dust removal in Digikam+Gimp
.. slug: easy-and-fast-dust-removal-in-digikamgimp
-->


It's a long time I was searching for an easy and fast way to remove dust spot from my photos.    
Unfortunately it seem that until now no tools like "dust removal mask" or something similar are present in the open-source/linux panorama.    
But yesterday I've found a <a href="http://dodonov.net/blog/2009/12/29/cleaning-dust-on-photos-or-in-gimp-we-trust/" target="_blank">post</a> explaining how to use a Gimp plugin to easy clean photos from dust spot.    
It was not exactly what I was searching for but it worked really well.    
The only thing to to it was to find a way to automatize the task.    

<!-- TEASER_END -->    

After some thinking I've found this way:    
    
1. In Digikam, right-click on the photo and select "Open in Gimp"
2. In Gimp:
* Add a new transparent layer (reduce opacity to see the photo's layer)
* Paint on the spots with the brush (this will be our "mask")
* In the layer window select the new layer and click on "Alpha to selection"
* In the layer window selectthe photo's layer
* Ctrl+x to remove dust spot
* Selection-&gt;Grow selection
* Filters-&gt;Map-&gt;Resynthetize
* Save with postfix "_v1" (non destructive editing supported in Digikam)
* Enjoy you photo:)



    
This is the result:    
    
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="../files/jam-2011-07-27_08-07-svezia-jamboree-1432_v1.jpg" style="margin-left: auto; margin-right: auto;"><img alt="" class="size-medium wp-image-886" height="200" src="../files/jam-2011-07-27_08-07-svezia-jamboree-1432_v1.jpg?w=300" title="JAM-2011-07-27_08-07-Svezia-Jamboree-1432_v1" width="300" /></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Image before dust removal</td></tr>
</tbody></table>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="../files/jam-2011-07-27_08-07-svezia-jamboree-1432_v2.jpg" style="margin-left: auto; margin-right: auto;"><img alt="" class="size-medium wp-image-887" height="200" src="../files/jam-2011-07-27_08-07-svezia-jamboree-1432_v2.jpg?w=300" title="JAM-2011-07-27_08-07-Svezia-Jamboree-1432_v2" width="300" /></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">Image after dust removal</td></tr>
</tbody></table>




