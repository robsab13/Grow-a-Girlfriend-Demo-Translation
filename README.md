Hi, and thank you for your interest in translating the game as a volunteer! Here are the steps on how to translate Grow a Girlfriend!

1. Download the appropriate zip file and extract it. If the language you want to translate the game into is not listed in the options, please download "other_language" instead.
  
2. Ensure you have an appropriate editing software (I recommend Notepad++ as it is beginner-friendly, but you can also use Visual Studio Code - the software I use to write the game's code). Opening and saving your progress using Word, for instance, can break the script's format and make it impossible for it to put in the game, so be careful!
  
3. If you downloaded "other_language", please find-and-replace all instances of "other_language" in ALL 5 "rpy" files with the name of the language you will be using, such as "japanese" (Without the quotes). It takes a few seconds, but it's important. What you choose to name it is how it will be displayed in the language selection menu.

4. Now for translations! Translate everything in "album.rpy", "options.rpy", "screens.rpy", and "script.rpy" by putting your translation where there is a empty "". Please do not use machine translation or AI translation. I trust you to localise it so that a native speaker would find reading it quite natural. I will be checking the quality of all translations. 

Example of what you'll see when you first open "script.rpy": 

  translate russian start_be4321ac:
      # "As you wake up, your first thought is:"   <- The original English line.
      ""  <- What you put in here is going to show instead. Currently, it would show absolutely nothing.

A translated line looks like this (I had to use machine translation in my examples, but please do not):

  translate russian start_be4321ac:
      # "As you wake up, your first thought is:"
      "Когда вы просыпаетесь, ваша первая мысль:"

* Notes on text effects: I make some sentences or words bold{b}, italic{i}, shake{sc=1}, sized up/down{size+10}, color {color=#000000}, etc. You can leave these out, however it means that players will not see any text effects for those lines. If you want to include it, it's simple - Just copy and past it however I used it in your translation, like this:
    #"{sc=4}{i}{color=#000000}SOMEONE IS AT THE DOOR!{/i}{/sc}"
    "{sc=4}{i}{color=#000000}кто-то у двери!{/i}{/sc}"

* Note on the "common.rpy" file. This particular file is mostly for debugging and will likely never been seen by the player. Translating "common.rpy" is entirely optional. You can ignore it, translate some, or all if you want. If you are up to it, I recommend that you only translate the months, days and save/load text (These can be found around line 150, or if you ctrl+F search for old "{#weekday}Monday". This will show on the save and load screen.

4. The image folder contains all images that have English text. Replacing these images with your language will make it easier for players using your translation, but it takes effort and some skill, so if you struggle with image editing, skip this step. I am willing to do it for you once you translate the necessary files!

Else, if you can do it yourself, one way of doing it is opening an image in an image editor, covering all English text with the same colour as the background, inserting translated text on top of it, and saving it so it overwrites the original. Do not change the image's name or dimensions, else it will not work or display properly.
   
5. When you have finished translating, please email me at true.blue.eyes@icloud.com with your updated folder. In your email, please include your name as you'd like it to be shown in the credits. If you want me to edit images for you, please also include the translation for each image.

After I play play test it, communicate with you, and solve any issues, I'll add your translation to the official demo and add you to the credits!

If you find any typos after submitting it to me, simply correct it and resend whatever file it was in to me.

For any questions, comment here or email me (true.blue.eyes@icloud.com)!
