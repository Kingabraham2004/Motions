from moviepy import VideoFileClip, concatenate_videoclips
import speech_recognition as sr
import os

def text_to_gloss(sentence):
    sentence = sentence.lower()

    remove_words = ["is", "are", "the", "a"]
    words = [w for w in sentence.split() if w not in remove_words]

    return " ".join([w.upper() for w in words])

print("Gloss:")


sign_dictionary = {
    "0": "motions/0.mp4",
    "1": "motions/1.mp4",
    "2": "motions/2.mp4",
    "3": "motions/3.mp4",
    "4": "motions/4.mp4",
    "5": "motions/5.mp4",
    "6": "motions/6.mp4",
    "7": "motions/7.mp4",
    "8": "motions/8.mp4",
    "9": "motions/9.mp4",

    "A": "motions/A.mp4",
    "B": "motions/B.mp4",
    "C": "motions/C.mp4",
    "D": "motions/D.mp4",
    "E": "motions/E.mp4",
    "F": "motions/F.mp4",
    "G": "motions/G.mp4",
    "H": "motions/H.mp4",
    "I": "motions/I.mp4",
    "J": "motions/J.mp4",
    "K": "motions/K.mp4",
    "L": "motions/L.mp4",
    "M": "motions/M.mp4",
    "N": "motions/N.mp4",
    "O": "motions/O.mp4",
    "P": "motions/P.mp4",
    "Q": "motions/Q.mp4",
    "R": "motions/R.mp4",
    "S": "motions/S.mp4",
    "T": "motions/T.mp4",
    "U": "motions/U.mp4",
    "V": "motions/V.mp4",
    "W": "motions/W.mp4",
    "X": "motions/X.mp4",
    "Y": "motions/Y.mp4",
    "Z": "motions/Z.mp4",

    "AFTER": "motions/After.mp4",
    "AGAIN": "motions/Again.mp4",
    "AGAINST": "motions/Against.mp4",
    "AGE": "motions/Age.mp4",
    "ALL": "motions/All.mp4",
    "ALONE": "motions/Alone.mp4",
    "ALSO": "motions/Also.mp4",
    "AND": "motions/And.mp4",
    "ASK": "motions/Ask.mp4",
    "AT": "motions/At.mp4",
    "BE": "motions/Be.mp4",
    "BEAUTIFUL": "motions/Beautiful.mp4",
    "BEFORE": "motions/Before.mp4",
    "BEST": "motions/Best.mp4",
    "BETTER": "motions/Better.mp4",
    "BUSY": "motions/Busy.mp4",
    "BUT": "motions/But.mp4",
    "BYE": "motions/Bye.mp4",
    "CAN": "motions/Can.mp4",
    "CANNOT": "motions/Cannot.mp4",
    "CHANGE": "motions/Change.mp4",
    "COLLEGE": "motions/College.mp4",
    "COME": "motions/Come.mp4",
    "COMPUTER": "motions/Computer.mp4",
    "DAY": "motions/Day.mp4",
    "DISTANCE": "motions/Distance.mp4",
    "DO": "motions/Do.mp4",
    "DO NOT": "motions/Do Not.mp4",
    "DOES NOT": "motions/Does Not.mp4",
    "EAT": "motions/Eat.mp4",
    "ENGINEER": "motions/Engineer.mp4",
    "FIGHT": "motions/Fight.mp4",
    "FINISH": "motions/Finish.mp4",
    "FROM": "motions/From.mp4",
    "GLITTER": "motions/Glitter.mp4",
    "GO": "motions/Go.mp4",
    "GOD": "motions/God.mp4",
    "GOLD": "motions/Gold.mp4",
    "GOOD": "motions/Good.mp4",
    "GREAT": "motions/Great.mp4",
    "HAND": "motions/Hand.mp4",
    "HANDS": "motions/Hands.mp4",
    "HAPPY": "motions/Happy.mp4",
    "HELLO": "motions/Hello.mp4",
    "HELP": "motions/Help.mp4",
    "HER": "motions/Her.mp4",
    "HERE": "motions/Here.mp4",
    "HIS": "motions/His.mp4",
    "HOME": "motions/Home.mp4",
    "HOMEPAGE": "motions/Homepage.mp4",
    "HOW": "motions/How.mp4",
    "INVENT": "motions/Invent.mp4",
    "IT": "motions/It.mp4",
    "KEEP": "motions/Keep.mp4",
    "LANGUAGE": "motions/Language.mp4",
    "LAUGH": "motions/Laugh.mp4",
    "LEARN": "motions/Learn.mp4",
    "ME": "motions/ME.mp4",
    "MORE": "motions/More.mp4",
    "MY": "motions/My.mp4",
    "NAME": "motions/Name.mp4",
    "NEXT": "motions/Next.mp4",
    "NOT": "motions/Not.mp4",
    "NOW": "motions/Now.mp4",
    "HI": "motions/hi.mp4",
    "WHAT": "motions/What.mp4",
    "WHEN": "motions/When.mp4",
    "WHERE": "motions/Where.mp4",
    "WHICH": "motions/Which.mp4",
    "WHO": "motions/Who.mp4",
    "WHOLE": "motions/Whole.mp4",
    "WHOSE": "motions/Whose.mp4",
    "WHY": "motions/Why.mp4",
    "WILL": "motions/Will.mp4",
    "WITH": "motions/With.mp4",
    "WITHOUT": "motions/Without.mp4",
    "WORDS": "motions/Words.mp4",
    "WORK": "motions/Work.mp4",
    "WORLD": "motions/World.mp4",
    "WRONG": "motions/Wrong.mp4",
    "YOU": "motions/You.mp4",
    "YOUR": "motions/Your.mp4",
    "YOURSELF": "motions/Yourself.mp4", 
}




def generate_video(gloss_sentence):

    words = gloss_sentence.split()

    clips = []

    for word in words:

        if word in sign_dictionary:

            print(f"Adding sign for {word}")

            clip = VideoFileClip(sign_dictionary[word])

            
            clip = clip.resized(height=480)

            clips.append(clip)
    else:

        print(f"Finger-spelling {word}")

        for letter in word:

            if letter in sign_dictionary:

                clip = VideoFileClip(sign_dictionary[letter])

                clip = clip.resize(height=480)

                clips.append(clip)

        else:
            print(f"Missing sign for {word}")

    if clips:

        final = concatenate_videoclips(clips, method="compose")

        output_path = "output.mp4"

        print("Rendering video...")

       
        final.write_videofile(
            output_path,
            codec="libx264",
            audio=False
        )

        print("Video saved!")

        
        os.startfile(output_path)

       
        final.close()

        for clip in clips:
            clip.close()

    else:
        print("No valid signs found!")

recognizer = sr.Recognizer()
mic = sr.Microphone()

while True:

    with mic as source:

        recognizer.adjust_for_ambient_noise(source)

        print("Listening...")

        audio = recognizer.listen(source)

    try:

        text = recognizer.recognize_google(audio)

        print("You said:", text)

        gloss = text_to_gloss(text)

        print("Gloss:", gloss)

        generate_video(gloss)

    except Exception as e:

        print("Error:", e)

