# E04a-Sprites Exercise

This is an exercise to start experimenting with sprites in Python Arcade. This repository assumes that you have Python Arcade installed.

The exercise takes place across three files:

 * main1.py:
   * The panda is feeling lonely. Change main1.py so that 20 random animals are displayed on the screen.
   * You will need to edit lines 26–32 to accomplish this assignment
   * To repeat something 20 times, you can use a loop:
     * for i in range(20):
     * will set i = 0, i = 1, i = 2, etc. until i = 19
   * To get a random element of a list, you can use:
     * animal = random.choice(animals)
   * To get a random location:
     * x = random.randint(0,800)
     * y = random.randint(0,600)
 * main2.py:
   * The alligator would like someone to talk to. Move her over and add a second animal with a (corresponding) speech bubble.
   * You will need to edit lines 48–56 to accomplish this assignment
   * self.animal_list and self.emote_list are lists of sprites that all get updated together
   * The .append() method adds an element to a list
   * Choose another animal from the assets folder, and then update the X,Y coordinates for the two animals and speech bubbles
 * main3.py:
   * The moose would like to be more mobile. Change the code so the moose follows the mouse around the screen.
   * You will need to edit line 40 to accomplish this assignment
   * If you look on lines 25–26, you will see that the sprite location is set using the center_x and center_y attributes
   * The moose is now part of the self.animal_list, so you will need to update the element(s) of that list:
     * for a in self.animal_list:
 * main4.py—*extra credit*:
   * Find some other sprites, and make them into a collage
   * Using what you have learned in the other exercise files, draw at least ten sprites in the window
   * [kenney.nl](https://kenney.nl) or [openGameArt.org](https://opengameart.org) are resources for free images
   * If you would like to make them move or react to the mouse, I will award extra points

As usual, fork and clone this repository. Edit the LICENSE and README.md, and submit the URL of your repository to Canvas.
