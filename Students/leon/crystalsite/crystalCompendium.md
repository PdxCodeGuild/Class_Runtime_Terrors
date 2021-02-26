# Project: Crystal Compendium
---
## Overview: 
This wesbite will allow a user to upload and manage their collection of rocks, crystals, and gems ("crystals"). The user will be able to create and add "tags" to their crystals so they can sort their collection to easily find the crystals they may need. The user will also have the option of uploading images of their cyrstals to make it easier for them to identify crystals in their collections. A blog feature is also included, which also takes "tags", so the user may journal their experiences with the crystals. Additional functionality includes a moon-phase tracker, which identifies the days of the current month when the major lunar phases occur (important for clearing and recharging crystals); a 'rockhound' page where the user can identify and store information about nearby sites where they can go collect crystals from nature; and a 'rock shop' area where they can keep tabs on the local shops selling crystals. 
---
## Functionality
The overall architecture of the site uses a modularity to app design, assuming that apps can be re-used in other sites. So, each app has its own template folder and even 'base' html file independent of the main site to maximize the swappability but retain control over the app. 
The site uses a blog model in combination with django-easy-maps package, sorl.thumbnails and bulma css framework. Supporting the concept of an individualized experience, the blog is kept minimalist so it is more of a journal. The 'compendium' keeps models of crystals and tags. The user can create tags easily and the tag can mean whatever they want. Tags are simple ways to be able to pull up all blogs and crystals related to that tag. Crystal model allows the user to upload an image file of their crystal, and to define the crystal however they wish, and add what-ever tags they want. Shop model allows the user to keep track of their favorite stores and visit their websites, notating what they like about that store. The map provides a look at the area, but is not meant to be used in place of other well-established programs that provide directions from current location data. Rockhound sites is similar, but the types of crystals found in the site are explicitly listed when the site is created, as this information is known and will not change. The 'notes' field is for entering other key information for the site, as whether one must pay to enter, or requires 4x4 vehicles. The map of the rockhound site is zoomed further out so one can appreciate the remoteness of these places. Again, the 'get directions' feature is left to established programs. 
sorl.thumbnails establishes a defined size where an image may go so that crystals without images display with the same spacing and alignment as those with images.
Bulma CSS was used because it has an easier 'human-readable' tagging system - however, it often created new problems which were not easily addressed. 
An effort was made at incorporating 'flatpages' but abandoned. 
---
## Data Model
An assumption made at the outset of the project was to have 1 server run multiple instances of the site which could then be cloned to run unique websites for individuals - with only Rockhound and Rock Shops being identical across all instances for ease of administration. The "SITE_ID" call was used in SETTINGS.PY to establish this relationship but is not yet fully implemented.
Taking a "fat models, thin views" approach, most of the models assume class-based views and django default templates where possible. This means models have more functions to accomodate these features - common functions added to the models include get-absolute-url, get-update-url, and get-delete-url.
Blog Model, in addition to the standard functions above, also has get-archive-year-url and get-archive-month-url.
Rock Shop model uses a URLField so that a properly formatted hyperlink is displayed in 'detail view'. 
Other models are as expected, but those that require mapping take a simple string (CharField) and pass it to django-easy-maps package, which itself calls on google-maps to complete the final rendered map.
The User Model relies heavily on django default templates but runs into a conflict with admin in certain places, so two urls for 'user' are implemented - the first to a custom User app which handles the things which would cause a conflict, and the second for the parts that django defaults can handle without conflict. These are placed one after the other in project.urls.py so that django first attempts the custom, and if then attemnpts the default to resolve urls. 
---
## Schedule
01:07 FEB 
    layout of website and design object relations
    gather data and resources
    skeleton website
    develop models
    test model relationships in shell
    develop basic functionality of views
08:14 FEB 
    barebones templates
    test functionality
    add ImageField functionality and test (sorl.thumbnail)
    implement user model functionality
    setup ADMIN controls 
    customise ADMIN

15:21 FEB
    add mapping (django-easy-maps)
    choose a CSS Framework and start to 'fleshout' templates
    develop the CSS code to get more aesthetics

22:24 FEB
    reveiw deployment options
    develop deployment strategy
    determine whether to deploy or continue developing the app













001
