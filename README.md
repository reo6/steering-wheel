# My story of building a steering wheel

## Starting off: ``mouse_test.py``

First, I was planning to use a mouse optical sensor, there are a lot of tutorials about this on youtube. While dad was building the wheel
with cardboard pieces, I coded mouse_test in order to see how it works. But there was a problem here, the game (ets2), was using something
different with the pointer. I had no idea about it, but when I automatically place the cursor in the middle of the screen with pyautogui, the cursor
was a little bit right of the screen when I launch the game. And also mouse controller option of the game was too sensitive. So this was
impossible.

Then we switched to a potentiometer since already we had one at home.

## Potentiometer with cardboard wheel and first lost version of ``driver.py``

<img src="https://i.imgur.com/UCLFHDY.jpeg" width=400 height=auto></img>
<img src="https://i.imgur.com/fuVOHhL.jpeg" width=400 height=auto></img>


This version was nice! We also built gas and brake pedals with just buttons. I and dad played with this thing a lot,
it was funny, we had great times.

But there was a problem, this thing was too small for a steering wheel, didn't feel realistic and because of the potentiometer,
it could rotate only 270 degrees. Then it became unstable as we played.

We had a couple of ideas. The first of them was buying a toy steering wheel. We went to a toy shop together and found something suitable,
but its quality was terrible, smells bad. And it was damn expensive.

We had only one option left after a long time: **A wooden steering wheel!**

## Fresh new wooden steering wheel


Alright, we need a new, heavy steering wheel and a mechanism to use it
with a **rotary encoder**. The thing called the rotary encoder was able to rotate endlessly.


*[Image of a rotary encoder]*

We failed. It took weeks to make a wooden steering wheel with its stand and the damn mechanism, but the rotary encoder, after a few turns, broke.

We needed a better solution. **A Mouse!**

The optical sensor of the mouse was absolutely perfect for this job!
It wasn't so hard to use it with our wooden wheel. We accidentally broke my sister's mouse but there was an old,
forgotten Microsoft mouse at home. It was so hard to open it, there were no screws.

It took a few hours to combine it with the wooden wheel.

<img src="https://i.imgur.com/rjDB97C.jpg" width=400 height=auto></img>
<img src="https://i.imgur.com/4p9mgXM.jpg" width=400 height=auto></img>

There was another problem now, *the software part*.

## New version of ``driver.py``

### Getting raw mouse data.

No pyautogui or no cursor monitoring. I had to read the raw data of a specific mouse. After a few hours of research, I found ``evdev``!
It was a python library, at first, I thought I needed to use C for such low-level stuff, but I was lucky.

It took me some time to figure out ``evdev``.

I wanted to use my regular mouse to browse menus and such things, so I disabled the Microsoft mouse with ``xinput``,
I had to do it every time I plugged it in. I was still able to read raw data.

And now;

### Creating a virtual steering wheel

This was truly harder than the ``evdev`` thing. I had to create a virtual steering wheel, I couldn't find a high-level python library that
works on Linux. I checked out every single steering wheel project on the internet, then got [europilot](https://github.com/marsauto/europilot)!
It's a self-driving bot for ets2, and I found ``joystick.py`` that does my thing. I included it in my project, read the code, and used it
at ``driver.py``. Unfortunately, the code became even dirtier.

## Happy Ending!

We played with it for one week, then switched to the keyboard again. I don't play the game anymore, dad continues playing it consistently **every day**.

