# Spaceward Graphics

I found a more recent page with some details about the companies at: http://www.sintefex.com/?targ=contact&src=home


> "**Mike Kemp has had a long involvement with audio and the electronic arts dating from his university days when after graduating from Emmanuel College, Cambridge, UK, with a Master of Arts in mathematics and computer science he turned down a research post at the Cambridge University Computer Laboratory to found his first studio business. He has mixed practical audio engineering with technical research and development in computer, audio and video fields.**
>
> - **_Spaceward Studios (24-track music production studio - founder, technical director and engineer/producer until 1988)_**
> - **_Spaceward Microsystems (8- 24- and 32-bit SuperNova and Matisse Video Graphics Systems for television - founder and technical director until 1991. The Spaceward Group was acquired by Avesco PLC in 1989)_**
> - **_Studio Audio and Video (SADiE Digital Audio Workstation (DAW) - founder and technical director until 1994)_**
> ..."

I emailed the contact email address in case I could reach Mike Kemp, but it seems unlikely to work.

Certainly, [it's too late to contact his co-founder Gary Lucas](https://x.com/morriswindsor/status/1015260568280846338?lang=en).
## Hall of Fame

> - **Spaceward Microsystems Ltd** Founder: **Mike Kemp**
> Founded in 1983, Spaceward Microsystems Ltd manufactured computer graphics equipment for the TV industry.
>   
> - **Spaceward Studios** Co-founder: **Mike Kemp**
> Founded in 1972, Spaceward Studios was first a 16 then a 24 track recording studio in Cambridge, UK.
> 
> [Companies started by Computer Science and Technology graduates and staff](https://www.cst.cam.ac.uk/ring/halloffame)
> Department of Computer Science and Technology, University of Cambridge.

## Quantel vs Spaceward

> "Spaceward lost the case, lost their product, and I was officially branded a liar in Falconer’s decision." 
> 
> [Digital Paint Systems: An Anecdotal and Historical Overview by Alvy Ray Smith](https://ohiostate.pressbooks.pub/app/uploads/sites/45/2017/09/paint.pdf) 
> IEEE Annals of the History of Computing, 2001

> "Adrian Wilson from [www.QuantelPaintbox.com](http://www.QuantelPaintbox.com) just sent me this cutting from 1989 when I organised a petition to save Spaceward, a company set up by a bunch of Cambridge scientists who invented some of the first CG software/hardware and who got me into the industry 40 years ago. They were taken to court by Quantel for infringing some of the patents."
> 
> [Klaudija Cermak on LinkedIn](https://www.linkedin.com/posts/klaudijacermak_vfx-cg-compositing-activity-7152277097237925888-OuJC/)

## Knightmare

Prominent user of Spaceward kit.

- [How Did the Visual Effects Work?](https://www.knightmare.com/backstage/knightmare-made/how-effects-work.html)
- [Computer Images Magazine, which ran from the mid-to-late 1980s, examined how Knightmare was made after Series 1.](https://www.knightmare.com/fanzone/coverage/print/knightmare-1987.html)
- [How Knightmare Began - Part 1](https://www.knightmare.com/backstage/history/part-1.html)
## Satori Paint

According to http://justsolve.archiveteam.org/wiki/Spaceward_Graphics and `dexvert` it seems Satori Paint can at least read `.rir` files and possibly `.r` files. I'm not sure about `.r` but the _Resolution Independent Raster_ files seem to be an interesting early vector image format, so converting those to e.g. TIFF would be quite lossy (although better than nothing). Possibly SVG is a better option. 

Hard to tell, the format is not easy to understand. I attempted a little reverse engineering, but could only discern some overall features and basic structure.

- [Wikipedia Deletion Log for page about Satori Paint. Deleted in 2022.](https://en.wikipedia.org/wiki/Special:Log?type=delete&user=&page=Satori_Paint&wpdate=&tagfilter=&subtype=&wpFormIdentifier=logeventslist)
	- "Expired [PROD](https://en.wikipedia.org/wiki/Wikipedia:PROD "Wikipedia:PROD"), concern was: Non-notable software. Unable to find significant independent coverage."
- [website c. 1997](https://web.archive.org/web/19970408112310/http://satoripaint.com/)
- [website c. 2005](https://web.archive.org/web/20050207030039/http://satoripaint.com/)
- [Overview of Satori FilmFX 64](https://web.archive.org/web/20011028084009fw_/http://www.pawprint.demon.co.uk/html/body_satori_thoughts.html)
- [Review of Satori WebFX 2000](https://www.irt.org/software/sw020/)
- [A disk image](http://www.win3x.org/win3board/viewtopic.php?t=27398&view=min)
- [A gallery](https://web.archive.org/web/20070813084252/http://www.animation-backgrounds.com/soft/software1.html) [via HN](https://news.ycombinator.com/item?id=36207379)


> The next morning the final image had been rendered and the resulting file stored to disk. Ben estimates that this took around 5 hours on a 266MHz Alpha. "This may appear to be time lost, but it was actually time gained, as I continued with the next project, right after hitting the render button". 
>
> https://web.archive.org/web/20001025201654/http://satoripaint.com/Tutorials/Workingwithverylargeimages.html


## Spaceward Studios

There's a bit more online about the music company.

- [Sintefex Audio: Spaceward Studios Retrospective](http://www.sintefex.com/?targ=spst81&src=links)
- [Studio Focus: Spaceward Studios, Cambridge](https://www.muzines.co.uk/articles/studio-focus/2782)
- [Spaceward Studios 1972-1988](https://web.archive.org/web/20130114003814/http://www.spacewardstudios.ukf.net/), [links page (with a working Flash widget!)](https://web.archive.org/web/20120125020826/http://www.spacewardstudios.ukf.net/links.htm)
- [Punk History > Spaceward - Mike Kemp](https://www.punk77.co.uk/punkhistory/spaceward.htm)
- [Punk History > Raw Records - Part 3](https://www.punk77.co.uk/raw/raw_records_history_part3.htm)


## Conversion with DOSBox

I have Ubuntu Linux installed inside Windows, and on there I followed these instructions: [https://wiki.winehq.org/Ubuntu](https://wiki.winehq.org/Ubuntu)

Then with a bit of prompting from WINE, I then needed `sudo apt-get install dosbox` as well...

After which I was able to run this script....

```bash
#!/bin/bash
for filename in *.R; do
    wine ../../Image\ Alchemy.ver.1.11.0.English/ALCHEMY.EXE "$filename" ---n
done
```

Which converted all the .R files to .PNG files (as per the manual via [http://justsolve.archiveteam.org/wiki/Image_Alchemy](http://justsolve.archiveteam.org/wiki/Image_Alchemy) ) as attached in the ZIP!

Now, the question is, are these very early examples of a glitch aesthetic, or are this data problems with the floppy imaging process?

Links:

 - https://blog.dshr.org/2019/08/wine-on-windows-10.html
