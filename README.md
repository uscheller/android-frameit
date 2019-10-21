# android-frameit
A tool for rendering a device frame around screenshots with text and a background image. 
Google [recommends not using framed screenshots in Play Store](https://developer.android.com/distribute/marketing-tools/device-art-generator). 
Nevertheless, a lot of companies do that for conversion optimization. 

## Installation
You should have Python with Pillow installed, preferably via [pipenv](https://github.com/pypa/pipenv).

```python
pipenv install
```


## Usage
Edit the frameit.py configuration to match your needs and run it.

```python
FramedImage(background_name="frame_dog_paws.png", frame=device_to_frame[device],
                    screen_shot=f"screenshot_{device}.png", output_name=f"output_{device}") \
            .add_text("Zooplus Android App",
                      "Von überall bequem und schnell durch\nmehr als 8.000 Produkte für Ihr Haustier stöbern",
                      title_font='fonts/MYRIADPRO-BOLDCOND.otf', text_font='fonts/HelveticaNeueLTPro-LtCn.otf') \
            .save()
```

It will transform a typical screenshot like

![Screenshot](example_screenshot.png)

into a framed image with text:

![Framed](example_framed.png)

## Credits
Developed for [Zooplus](https://www.zooplus.de/) by [Ulrich Scheller](https://www.ulrich-scheller.de/)