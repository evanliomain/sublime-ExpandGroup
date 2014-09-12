ExpandGroup
===================

Sublime Text 3 Plugin to switch and resize 2-Columns layout or 4-Grid layout fastest as possible.

Keys
----

Pressing <kbd>Alt+left</kbd> or <kbd>Alt+right</kbd> or <kbd>Alt+up</kbd> or <kbd>Alt+down</kbd> will switch focus to the respective column or cell and resize it according to the configured ratio (which by default is "4:1" and "1:4"). 

If you add <kbd>shift</kbd> to your shortcut, it will move the current editing file in the target group.

So if you are a full-keyboard coder or a mouse lover, this plugin got you covered.


What it does
-----

#### 2 columns layout

    
    --------------------                  -------------------- 
    |             |    |                  |   |              | 
    |             |    |                  |   |              | 
    |             |    |    alt+left      |   |              | 
    |             |    |    <=======      |   |              | 
    |             |    |                  |   |              | 
    |             |    |    alt+right     |   |              | 
    |             |    |    =======>      |   |              | 
    --------------------                  -------------------- 

#### 4 grid layout
    
    --------------------                  -------------------- 
    |             |    |                  |   |              | 
    |             |    |    alt+left      |   |              | 
    |             |    |    <=======      |   |              | 
    |             |    |                  |   |              | 
    |             |    |    alt+right     |   |              | 
    --------------------                  -------------------- 
    |             |    |    =======>      |   |              | 
    --------------------                  -------------------- 


                          /\     alt+down
                          ||     ||
                        alt+up   \/


    --------------------                  -------------------- 
    |             |    |                  |   |              | 
    --------------------                  -------------------- 
    |             |    |    alt+left      |   |              | 
    |             |    |    <=======      |   |              | 
    |             |    |                  |   |              | 
    |             |    |    alt+right     |   |              | 
    |             |    |    =======>      |   |              | 
    --------------------                  -------------------- 


    



Notes
-----

Numbers are treated as a ratio, so `50:50` is identical to `1:1`.

For example:

    50:50
    (2 columns, equal width. 1 row)

    --------------------
    |        |         |
    |        |         |
    |        |         |
    |        |         |
    |        |         |
    |        |         |
    --------------------

    1:4
    (2 columns, one four times the width of the other. 1 row)

    --------------------
    |      |           |
    |      |           |
    |      |           |
    |      |           |
    |      |           |
    --------------------
    

    

Credits
-------

**Created by**

Evan Liomain
