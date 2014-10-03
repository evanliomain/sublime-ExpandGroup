ExpandGroup
===================

Sublime Text 3 Plugin to switch and resize 2-Columns layout or 4-Grid layout fastest as possible.

Install
----
**With the Package Control plugin** 

- Install [Package Control](http://wbond.net/sublime_packages/package_control)
- restart ST and bring up the Command Palette :
    - <kbd>Command+Shift+P</kbd> on OS X, 
    - <kbd>Control+Shift+P</kbd> on Linux/Windows. 
- Select "Package Control: Install Package", 
- Wait while Package Control fetches the latest package list, then select `Expand Group` when the list appears. 

The advantage of using this method is that Package Control will automatically keep Expand Group up to date with the latest version.

**Without Git** 

- Download the latest source from [GitHub](https://github.com/evanliomain/sublime-ExpandGroup)
- Copy the sublime-ExpandGroup folder to your Sublime Text "Packages" directory.

**With Git** 

- Clone the repository in your Sublime Text "Packages" directory:

    git clone https://github.com/evanliomain/sublime-ExpandGroup.git


The "Packages" directory is located at:

|OS|Path|
|-|-|
|OS X|~/Library/Application Support/Sublime Text 2/Packages/|
|Linux|~/.config/sublime-text-2/Packages/|
|Windows|%APPDATA%/Sublime Text 2/Packages/|


Keys
----

Pressing <kbd>Alt+left</kbd> or <kbd>Alt+right</kbd> or <kbd>Alt+up</kbd> or <kbd>Alt+down</kbd> will switch focus to the respective column or cell and resize it according to the configured ratio (which by default is "4:1" and "1:4"). 

If you add <kbd>shift</kbd> to your shortcut, it will move the current editing file in the target group.

So if you are a full-keyboard coder or a mouse lover, this plugin got you covered.


Warning, the <kbd>Alt+up</kbd> and <kbd>Alt+down</kbd> may be in conflict with another plugin, such as "Emmet". Please set this keybinding into the "Key Bindings - User" file.



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


#### 2 rows layout
    
    --------------------    
    |                  |    
    |                  |    
    |                  |    
    |                  |    
    |                  |    
    --------------------    
    |                  |    
    --------------------    
         /\   alt+down
         ||     ||
       alt+up   \/
    --------------------  
    |                  |  
    --------------------  
    |                  |  
    |                  |  
    |                  |  
    |                  |  
    |                  |  
    --------------------  


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
                            /\   alt+down
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
