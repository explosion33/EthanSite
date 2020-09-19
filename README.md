# code for my personal website

## Setup
### dependancies
```
pip install flask==1.1.2
pip install Werkzeug==0.16.0
```

### run
```
python main.py
```

## dynamic page creating

pages are created dynamicaly using the file pageData.txt the structure is as follows
```
[
  {
    "root": "", #Used if pages are similar and need to be specified
    "ID": "samplePage", #Used to find the page data on load
    "title": "Sample Page", #page title, displayed at the top
    "sections": [ #each section is divided by an <hr> tag
        {
          "title": "Title of the first section",
          "groups": [ #sections are made up of groups, groups are just seperate rows in bootstrap
              {
                "type": "text",
                "text": "This is a group, groups are individual parts of a section"
              },
              {
                "type": "textImage",
                "text": "There can be more than one group per section and more than one section per pages",
                "image": "sampleImage.png",
                "size": "50%"
              },
          ],
        }
    ],
  }
]
```

### types of group
**textImage**: text on left image on right (defualt when type is not defined)

  &emsp;text: the text content for the text field

  &emsp;image: image path. Starts in static/images

  &emsp;size: size of the image in % (25%)
  
  &emsp;link: the link content for the text

  &emsp;imLink: the link for the image


**text**: regular paragraph text

  text: the text content for the text field

  link: the link content for the text


**list**: a bulleted list

  text: list of text to be bulleted


**video**: A centered video (file only)

  aspect: the aspect ratio of the video (5by10)

  path: the video path. Starts in static/videos


**imageGroup**: a carousel of images

  images: list of image paths. Path starts in static/Images

  size: size of the carousel (25%)

  autoSlide: speed at which to scroll through images. use false to disable slide. (false by default)


**textWithImages**: text on left imageGroup on the right

  text: the text content for the text field

  images: list of image paths. Path starts in static/Images

  size: size of the carousel (25%)

  autoSlide: speed at which to scroll through images. use false to disable slide. (false by default)


**break**: inserts specified number of <br> tags

  amount: number of tags (2)
