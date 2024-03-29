# Bluetooth Ordering System

# Concept of Operation
Purpose: To create a music player that recognizes the user’s facial expression and plays music
depending on their current emotion.

# Goal: 
Our system analyses a person’s emotions using image recognition and plays music
accordingly. For example, if the person shows signs of anger or stress through contempt or other
negative emotions, the system will play calming music, however if the person is in a positive
mood, it will continue to play uplifting music. Thus, our primary goal is to elevate a person’s
mood using appropriate music.
# Importance: 
Our project is important because it uses music to improve a person’s mental
wellbeing. Emotional regulation is an essential component to mental health. As an example,
some studies have shown classical music to be a form of antidepressant. Using our emote music
player, we aim to alleviate the user’s mental stress and anxiety, and maintain a sense of calm.
User Interaction: The user puts their music preference in a USB stick which is then plugged
into a raspberry pi. After booting the system, the user faces the camera so it can take a screenshot
to measure their current emotional state. The system then plays the appropriate song, and once
the song is over the camera takes another screenshot to detect the next emotion.

# Outcome: 
If the user is anxious, after playing calming music, their mood should improve until
the emotion of “joy” or other positive emotions exceeds that of “anger”, “sad” or “contempt”,
which signifies that our system has accomplished its goal of improving their mood, or calming
them down
