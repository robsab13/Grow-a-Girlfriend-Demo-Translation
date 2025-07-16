Hi, and thank you for your interest in translating the game as a volunteer! Here are the steps on how to translate Grow a Girlfriend!

# Step 0: Sign up to the project
Please open go to this document (https://docs.google.com/document/d/1ReVeinGChA440N3xEIY4DcxImOcht0Lt-f_HkQ3Gizw/edit?usp=sharing) and add your email and the language you wish to translate as shown in the example. If you are unable to do so, please email me and I will add it for you. This will allow anybody who is translating the game to check and see what languages are being worked on and potentially collaborate. It's up to you to email someone working the same language as you, to join a team and split up the tasks.

# Step 1: Download
Download:
1. One of the folders in "tl" directory that's in the language you want to translate it into. If it is not listed, please download "other_language" instead. This will be the case for most of you.
2. "Images"

For those who are new to GitHub: The simplest way to download the files is to click the green "code" button, and then click the "Download ZIP" button. That downloads everything. Extract the folder, then delete the other language folders that you are not using (since this method downloads ALL the language options).
Otherwise, if you are familiar with software such as git, you can fork and clone the repository and work in the cloned directory. I will merge any changes back when a pull request is made.
   
# Step 2: Software and set up
Ensure you have an appropriate editing software (I recommend Notepad++ as it is beginner-friendly, but you can also use Visual Studio Code - the software I use to write the game's code). Opening and saving your progress using Word, for instance, can break the script's format and make it impossible for it to put in the game, so be careful!

You will be opening the .rpy (NOT .rpyc) scripts found in the relevant tl folder.
  
If you downloaded "other_language", please find-and-replace all instances of "other_language" in ALL 5 "rpy" files with the name of the language you will be using, such as "japanese" (Without the quotes). Then, change the name of the folder itself to the same name (They must be identical!). It takes a few minutes, but it's important. What you choose to name it is how it will be displayed in the language selection menu.

# Step 3: Translate
Now for translations! Go through four of the .rpy files ("album.rpy", "options.rpy", "screens.rpy", and "script.rpy") and put your translation where there is a empty "". Please do not use machine translation or AI translation. I trust you to localise it so that a native speaker would find reading it quite natural. I will be checking the quality of all translations.
   
--------------------------------------
Example of what you'll see when you first open "script.rpy": 

`translate russian start_be4321ac:`

`  # "As you wake up, your first thought is:"`   <- The original English line.

`  ""`  <- What you type in here will show instead of the above line. Currently, it would show nothing.

--------------------------------------

A translated line looks like this (I had to use machine translation in my examples, but please do not):

`translate russian start_be4321ac:`

`  # "As you wake up, your first thought is:"`

`  "Когда вы просыпаетесь, ваша первая мысль:"`

--------------------------------------

Some sentences have text effects like bold{b}, italic{i}, shake{sc=1}, sized up/down{size+10}, color {color=#000000}, etc. You can leave these out, however it means that players will not see any text effects for those lines. If you want to include it, it's simple - Just copy and past it however I used it in your translation, like this:
  
`#"{sc=4}{i}{color=#000000}SOMEONE IS AT THE DOOR!{/i}{/sc}"`

`"{sc=4}{i}{color=#000000}кто-то у двери!{/i}{/sc}"`

--------------------------------------

Note on the "common.rpy" file: Translating this file is optional. You can ignore it, translate some, or all if you want. It is mostly for debugging and will likely never been seen by the player. If you are up to it, I recommend that you only translate the months, days and save/load text (These can be found around line 150, or if you ctrl+F search for old "{#weekday}Monday". This will show on the save and load screen.

--------------------------------------
# Testing:
The most recent demo game now allows for language testing! To do it:
1. Download the most recent demo.
2. Download the "translation_testing.rpy" script from github.
3. Place that script into the "game" folder of the demo you downloaded. On Steam, the path to game folders is SteamLibrary > steamapps > common > Grow a Girlfriend Demo > game.
4. Place your language folder into "game/tl". The only other folder in there should be "None", which is English. Do not include Images - the current script does not support image translation testing yet.
5. Launch the game! On the main menu, there should be a button to change languages from English into your translation - It will have the name of your folder.
Note: Translate "screens.rpy" before you do this, otherwise the buttons to start the game, etc will disappear, and you'll find yourself stuck on the main menu!

# Step 4: Images
The image folder contains all images that have English text. Replacing these images with your language will make it easier for players using your translation, but it takes effort and some skill, so if you struggle with image editing, skip this step. I am willing to do it for you once you translate the necessary files!

Else, if you can do it yourself, one way of doing it is opening an image in an image editor, covering all English text with the same colour as the background, inserting translated text on top of it, and saving it so it overwrites the original. Do not change the image's dimensions, else it will not+ display properly.

If you choose to translate the images yourself, please save the translated images WITH THE SAME NAME as its original, and place it in your translation language folder.

--------------------------------------
   
# Step 5: Send it to me
When you have finished translating, preferably create a fork and a pull request for my repo so that I can incorporate the changes automatically. Alternatively, if you do not know how to do that please email me at true.blue.eyes@icloud.com with your updated folder. In your email, please include all the volunteers names as they would like it to be shown in the credits. If you want me to edit images for you, please also include the translation for each image.

After I play play test it, communicate with you, and solve any issues, I'll add your translation to the official demo and add you to the credits!

If you find any typos after submitting it to me, simply correct it and resend whatever file it was in to me.

For any questions, email me! I want to help the best I can!
