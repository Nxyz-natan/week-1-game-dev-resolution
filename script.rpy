define mc    = Character("You", color="#FFFFFF")
define riley = Character("Riley", color="#FFB7C5")
define jun   = Character("Jun", color="#B7D7FF")
define narr  = Character(None, what_color="#AAAAAA")

image bg classroom = "bg_classroom.jpg"
image bg hallway   = "bg_hallway.jpg"
image bg rooftop   = "bg_rooftop.jpg"
image bg cafeteria = "bg_cafeteria.jpg"
image bg park      = "bg_park.jpg"
image bg library   = "bg_library.jpg"
image bg gym       = "bg_gym.jpg"

image riley = "riley.png"
image jun   = "jun.png"



show riley at riley_pos

label start:

    scene bg classroom
    with fade

    narr "Monday. Five days left of the school year."
    narr "You've sat next to Riley Park since September."
    narr "That's nine months of passing worksheets back and forth."
    narr "Nine months of 'did you do the reading' and 'can I borrow a pen'."
    narr "Nine months of almost saying something real."
    hide jun
    with dissolve
    show riley at  center
    with dissolve

    narr "They're drawing in the margin of their notes again."
    narr "Little figures. They think nobody notices."
    narr "You notice."

    riley "You're staring."
    mc "I'm not."
    riley "You were doing the thing."
    mc "What thing."
    riley "The thing where you look at my notebook and pretend you're looking at the board."

    narr "Caught."

    menu:
        "How do you handle this?"

        "Own it. 'Your drawings are good.'":
            $ noticed_art = True
            mc "Your drawings are good. The little figures."
            riley "You can actually see those from there?"
            mc "I've had nine months of practice."
            riley "That's either really sweet or really creepy."
            mc "Bit of both, probably."
            riley "...Fair."

        "Deny it completely.":
            $ noticed_art = False
            mc "I was looking at the board. Mr. Chen wrote something."
            riley "He hasn't written anything all lesson."
            mc "He was going to."
            riley "Sure he was."

        "Change the subject fast.":
            $ noticed_art = False
            mc "Did you get question four? I can't figure it out."
            narr "Riley looks at you for a second longer than necessary."
            riley "Yeah. It's the quadratic one  here."
            narr "They slide their notebook over."
            narr "You look at the answer. You already had it right."
            narr "They don't say anything about that."

    narr "The bell goes. Everyone starts packing up."

    riley "Hey  are you going to the end of year thing on Friday?"
    mc "The gym party thing?"
    riley "Yeah. Jun's organising it. It's going to be either really fun or a disaster."
    hide riley
    with dissolve
    show jun at  center
    with dissolve

    jun "Probably both!"
    narr "Jun materialises from nowhere, as Jun does."
    jun "You're coming right? We need bodies. Good ones."
    mc "Gee, thanks."
    jun "You know what I mean."

    hide jun
    with dissolve

    menu:
        "Do you say you'll go?"

        "Yes, definitely.":
            $ going_friday = True
            mc "Yeah, I'll be there."
            riley "Cool."
            narr "One word. But they're smiling at their bag."

        "Maybe, I'll see.":
            $ going_friday = False
            mc "Maybe. Depends how the week goes."
            riley "No pressure."
            narr "They mean it. Somehow that makes it worse."

        "Only if Riley's going.":
            $ going_friday = True
            mc "Are you going?"
            riley "I  yeah, probably."
            mc "Then yeah, I'll go."
            narr "A pause."
            riley "Okay then."

    narr "Riley heads out. Jun reappears instantly."
    hide riley
    with dissolve
    show jun at  center
    with dissolve

    jun "So."
    mc "Don't."
    jun "I'm just saying."
    mc "Jun."
    jun "Nine months, and you still haven't"
    mc "Goodbye, Jun."
    hide riley
    with dissolve
    hide jun
    with dissolve

    narr "You pick up your bag."
    narr "Four days left."

    jump day2_morning

label day2_morning:

    scene bg library
    with fade

    narr "Tuesday. Free period. You're in the library."
    narr "Or you're supposed to be doing work in the library."
    narr "Mostly you're just sitting there."
    hide jun
    with dissolve
    show riley at  center
    with dissolve

    narr "Riley drops into the seat across from you."

    riley "Hide me."
    mc "From what?"
    riley "Ms. Okafor wants volunteers for the leavers' assembly and I've been avoiding her for two days."
    mc "Just say no."
    riley "I can't say no to Ms. Okafor. Nobody can say no to Ms. Okafor."

    narr "This is true."

    menu:
        "What do you do?"

        "Offer to be their decoy  walk out with them.":
            mc "Come on. I'll walk out with you. Safety in numbers."
            riley "You'd do that?"
            mc "I do a lot of things."
            narr "You both sneak out through the back of the library like absolute cowards."
            narr "It's one of the best five minutes of the week."
            $ library_escape = True

        "Let them hide behind your bag.":
            mc "Just  get behind my bag. Pretend to read."
            riley "This is a terrible plan."
            mc "Do you have a better one?"
            narr "They crouch slightly behind your backpack."
            narr "Ms. Okafor walks past without stopping."
            narr "Riley exhales."
            riley "I can't believe that worked."
            $ library_escape = True

        "Tell them to just go talk to Ms. Okafor.":
            mc "Honestly? Just go do it. It'll be over in two minutes."
            riley "..."
            riley "You're right. I hate that you're right."
            narr "They go. They come back twelve minutes later having agreed to read a poem at the assembly."
            riley "I hate everything."
            $ library_escape = False

    narr "You end up staying in the library the whole free period."
    narr "Not doing much. Just talking."

    riley "Can I show you something?"

    narr "They slide their sketchbook across the table."
    narr "Not the notebook  the actual sketchbook. The one they usually keep in their bag."
    narr "It's full of small detailed drawings. Streets. Buildings. People on buses."
    narr "One page is just hands. Dozens of hands in different positions."
    narr "There's one near the back that looks like it could be your classroom."

    mc "These are incredible."

    riley "They're just sketches."
    mc "Riley. These are genuinely really good."
    riley "I want to study architecture. Or illustration. I can't decide."
    mc "Why not both."
    riley "That's the dream, isn't it."

    narr "They take the sketchbook back carefully."
    narr "Like it's something precious."

    menu:
        "What do you say?"

        "Tell them they should go for it.":
            mc "You should. Seriously. Don't pick the safe option just because it's safe."
            riley "Is that advice for me or for you?"
            narr "You don't answer that."
            narr "Mostly because you're not sure."

        "Ask about the classroom drawing.":
            mc "Is that  is that our classroom? Near the back?"
            riley "You weren't supposed to see that one."
            mc "It's good."
            riley "It's just practice."
            narr "They close the sketchbook."
            narr "But they're smiling."

        "Ask who the people on the buses are.":
            mc "The bus ones  are those people you know?"
            riley "Sometimes. Sometimes strangers. I draw people when I'm bored."
            mc "Have you ever drawn me?"
            narr "A pause."
            riley "Maybe."
            narr "They don't elaborate."
            narr "You don't push it."

    narr "The bell goes."

    riley "Same time tomorrow? I have free period again."

    menu:
        "Yes.":
            mc "Yeah. Same time."
        "I'll try.":
            mc "I'll try to make it."
            riley "No pressure."

    narr "They head off."
    narr "Three days left."

    jump day3

label day3:

    scene bg park
    with fade

    narr "Wednesday. Someone propped the fire exit open."
    narr "Half the year is sitting outside on the grass."
    narr "It's technically not allowed."
    narr "Nobody seems to care today."

    show riley at  left
    with dissolve
    show jun at  right
    with dissolve

    narr "You find Riley and Jun near the old oak tree."
    narr "Jun is eating crisps directly from the bag."

    jun "There they are. The person who abandoned me at lunch yesterday."
    mc "I was in the library."
    jun "With Riley."
    mc "..."
    jun "Just an observation."

    riley "Leave them alone."
    jun "I'm just saying it's very convenient that"
    riley "Jun."
    jun "I'm eating my crisps. I'm not saying anything."

    hide jun
    with dissolve

    narr "You sit down next to Riley."
    narr "The sun is actually out for once."

    riley "Okay. Genuine question."
    mc "Go ahead."
    riley "If you could be anywhere that isn't here right now, where would you be?"

    menu:
        "What do you say?"

        "Somewhere with better weather.":
            mc "Somewhere warm. Abroad. Anywhere with a beach."
            riley "Okay, but which beach?"
            mc "Does it matter?"
            riley "It matters a lot actually. Beach taxonomy is very important."
            narr "You spend ten minutes debating beach types."
            narr "It is a genuinely great conversation."

        "Honestly? Nowhere. This is fine.":
            mc "Nowhere, actually. This is fine."
            narr "Riley looks at you."
            riley "Yeah?"
            mc "Yeah."
            narr "A small quiet moment."
            riley "Same."

        "Somewhere with better food than the canteen.":
            mc "Literally anywhere with food that isn't the canteen."
            riley "Oh my god, the pasta. What IS the pasta."
            mc "I don't know and I've stopped asking."
            riley "Every Wednesday. Like clockwork. Mystery pasta."
            narr "You both sit there laughing about the pasta for longer than is reasonable."
    hide riley
    with dissolve
    show jun at  center
    with dissolve

    narr "Jun comes back and sits between you both."

    jun "So what are we talking about."
    riley "Beaches."
    jun "Love that for us."

    narr "The afternoon drifts."
    narr "At some point Jun falls asleep in the sun."

    hide jun
    with dissolve

    narr "You and Riley keep talking."
    narr "About next year. About leaving. About how weird it is that this is almost over."

    riley "Do you think we'll stay in touch? After."
    narr "After. The word sits there."

    menu:
        "What do you say?"

        "I want to.":
            mc "I want to. Yeah."
            riley "Good. Me too."
            narr "Simple. But it lands."

        "That depends on you.":
            mc "That kind of depends on you, doesn't it."
            riley "Does it?"
            mc "You're the one who's hard to read."
            riley "I'm hard to read?"
            mc "Little bit."
            riley "You're one to talk."

        "Honestly I don't know.":
            mc "Honestly? I don't know. I hope so."
            riley "Yeah. I hope so too."
            narr "It's not a promise."
            narr "But it's something."

    narr "Two days left."

    jump day4

label day4:

    scene bg hallway
    with fade

    narr "Thursday. One day before the end."
    narr "The school feels different."
    narr "People are signing shirts. Taking photos."
    narr "There's a specific kind of sadness that only exists in the last week of something."

    hide jun
    with dissolve
    show riley at  center
    with dissolve

    narr "Riley finds you at your locker."

    riley "Hey."
    mc "Hey."
    riley "Are you okay? You seem"
    mc "I'm fine. Just. End of year stuff."
    riley "Yeah."

    narr "They lean against the locker next to yours."

    riley "Can I tell you something weird?"
    mc "Always."
    riley "I'm going to miss this. Like, actually miss it."
    riley "Which is strange because most of the time this place drives me insane."
    mc "Not all of it drives you insane though."
    riley "No. Not all of it."

    narr "They look at you when they say it."

    menu:
        "This is the moment. What do you do?"

        "Tell them what they mean to you.":
            jump thursday_honest

        "Ask if you can walk home together.":
            jump thursday_walk

        "Say 'me too' and leave it there.":
            jump thursday_quiet

        "Ask about the Friday party.":
            jump thursday_party

label thursday_honest:

    mc "Riley."
    riley "Yeah?"
    mc "I need to tell you something before Friday because if I don't I'm going to spend all summer thinking about it."
    riley "Okay. You're scaring me a little."
    mc "Don't be scared. It's a good thing. I think."
    mc "I really like you. Like  not just as the person I sit next to. I've liked you for months."
    mc "And I know that's a lot to just say in a hallway but there it is."

    narr "Silence."
    narr "A proper, full silence."

    riley "...You picked a Thursday."
    mc "Yeah."
    riley "In a hallway."
    mc "Yeah."
    riley "You couldn't have said this, like, eight months ago?"
    mc "Would you have been ready eight months ago?"

    narr "They think about it."

    riley "...No. Probably not."
    riley "But I'm ready now."

    jump ending_good

label thursday_walk:

    mc "Do you want to walk home together? After school?"
    riley "Yeah. Yeah, I'd like that."

    scene bg park
    with fade
    hide jun
    with dissolve
    show riley at  center
    with dissolve

    narr "You take the long way."
    narr "Past the park, past the shops, along the canal."
    narr "It adds forty minutes to the journey."
    narr "Neither of you mentions it."
    narr "At some point your hands brush."
    narr "Neither of you moves away."

    riley "This is nice."
    mc "Yeah."

    narr "Riley stops outside a small bookshop."

    riley "I used to come here every Saturday when I was little."
    riley "My mum would let me pick one book and one book only and I always spent like an hour deciding."
    mc "What did you pick?"
    riley "The same series every time, basically. Different book, same series."
    mc "That's not really picking."
    riley "I was nine! I didn't have range!"

    narr "You stand outside the bookshop laughing."
    narr "People walk past."
    narr "You don't move."

    menu:
        "Say something."

        "Tell them you like this. Them, specifically.":
            mc "For what it's worth  I really like this. You."
            narr "Silence."
            riley "Yeah?"
            mc "Yeah."
            riley "...Me too."
            jump ending_good

        "Leave it unsaid and just enjoy the moment.":
            narr "You don't say anything."
            narr "But you walk the rest of the way closer together."
            jump ending_neutral

label thursday_quiet:

    mc "Me too."

    narr "That's all."
    narr "Riley nods."
    narr "You close your locker."
    narr "You walk to your next class separately."
    narr "But for the rest of the day, every time you're in the same room,"
    narr "you're a little more aware of exactly where they are."

    jump day5_setup

label thursday_party:

    mc "Are you actually excited for tomorrow?"
    riley "The party? Honestly yeah. Jun's put a lot into it."
    riley "I think it could be really good."
    mc "Are you going with anyone?"
    riley "Just showing up. You?"
    mc "Same."

    narr "A pause that lasts about one second too long."

    riley "We could go together. If you wanted."
    mc "Yeah. I'd want that."
    riley "Cool. Meet me at the gate at seven?"
    mc "Seven. Yeah."

    narr "They head off."
    narr "Jun appears from around the corner."

    show jun at center
    hide riley
    with dissolve

    jun "Did you just get a date to the party?"
    mc "It's not a date."
    jun "It's a date."
    mc "Jun"
    jun "It's a date! Own it!"

    hide jun
    with dissolve

    narr "You walk to class."
    narr "You might be smiling."

    jump day5_setup

label day5_setup:

    scene bg gym
    with fade

    narr "Friday."
    narr "The gym is decorated with strings of lights."
    narr "Someone's made a playlist that's trying to be everything at once."
    narr "It's loud and warm and a little chaotic."
    hide riley
    with dissolve
    show jun at center
    with dissolve

    jun "Okay, it looks good right? Tell me it looks good."
    mc "It looks really good, Jun."
    jun "I spent four hours on those lights."
    mc "It shows."

    hide jun
    with dissolve

    show riley at  center
    with dissolve

    narr "Riley finds you near the drinks table."

    riley "Hey. You made it."
    mc "Of course."

    narr "They're dressed differently from school. More themselves, somehow."
    narr "You don't say that out loud."

    menu:
        "How does the night go?"

        "Spend the whole night with Riley.":
            jump friday_together

        "Hang out with the group, but keep finding Riley.":
            jump friday_group

        "Something feels off  slip away to the rooftop.":
            jump friday_rooftop

label friday_together:

    narr "You don't really leave each other's side."
    narr "It's not a decision. It just happens."
    narr "You dance badly on purpose."
    narr "You steal food from the good table before Jun catches you."
    narr "You find a quiet corner when the music gets too loud and just talk."

    riley "I keep thinking about next year."
    mc "Good thoughts or bad?"
    riley "Both. Mostly good."
    riley "There are things I'm going to miss."

    narr "They look at you."

    mc "You don't have to miss all of them."
    riley "Yeah?"

    menu:
        "Say the thing."

        "Say it properly tell them how you feel.":
            jump ending_good

        "Just ask for their number.":
            mc "Give me your number. So we don't have to miss each other."
            riley "That might be the smoothest thing you've ever said."
            mc "Don't tell anyone. It'll ruin my reputation."
            jump ending_good

label friday_group:

    narr "The night moves in groups."
    narr "Jun's games. Someone's speech. A lot of photos."
    narr "But you keep finding Riley."
    narr "Across the room. In the same queue. At the same table."
    narr "Like gravity."
    narr "Near the end of the night, the crowd thins out."
    narr "You end up sitting on the floor by the speaker with Riley."
    narr "It's too loud to hear properly."
    narr "You lean in to talk."
    narr "They lean in to listen."

    riley "I'm glad you came."
    mc "Me too."

    narr "It's simple."
    narr "But Riley's smiling like you said something much better."

    menu:
        "End of the night."

        "Walk them home.":
            mc "Can I walk you home?"
            riley "Yeah. Yeah, I'd really like that."
            jump ending_good

        "Exchange numbers and say goodnight.":
            jump ending_neutral

label friday_rooftop:

    hide riley
    with dissolve

    scene bg rooftop
    with fade

    narr "You slip out through the fire exit."
    narr "Up the stairs. Through the door that's always unlocked if you know where to push."
    narr "The rooftop."
    narr "The city stretches out below."
    narr "You can faintly hear the music from the gym."
    narr "You sit on the low wall and look out."
    narr "Ten minutes later, you hear the door."

    show riley at center
    with dissolve

    riley "I saw you leave."
    mc "Sorry."
    riley "Don't be. I followed you."

    narr "They sit beside you."
    narr "Close enough that your shoulders touch."

    riley "It's nice up here."
    mc "Yeah."
    riley "I didn't know you were a rooftop person."
    mc "I didn't know either until now."
    narr "The music drifts up faintly."
    narr "The sky is clear."

    riley "Hey."
    mc "Hey."
    riley "What's going on in your head?"

    menu:
        "Tell them."

        "Tell them everything.":
            mc "I've been trying to figure out how to talk to you all year."
            mc "And now it's the last day and I still don't really know how."
            mc "But I think I really like you. And I didn't want to not say it."
            narr "Riley doesn't say anything for a moment."
            narr "Then they lean their head on your shoulder."
            riley "You could have just said that in September."
            mc "I know."
            riley "I would have said it back."
            jump ending_secret

        "Say you don't know. Let them talk.":
            mc "I don't know. What about you?"
            riley "I think... I'm sad it's ending."
            riley "But I think some of it doesn't have to end."
            narr "They look at you."
            narr "You know what they mean."
            jump ending_secret

label ending_good:

    hide riley
    with dissolve

    scene bg park
    with fade

    show riley at center
    with dissolve

    narr "~ GOOD ENDING: Finally ~"
    narr " "
    narr "You walk home the long way."
    narr "Past the park. Along the canal. Nowhere in particular."
    narr "Your hands find each other somewhere near the old bookshop."
    narr "Neither of you says anything about it."
    narr "You don't need to."
    narr "Jun texts you both at 11 PM."
    narr "'I SAW THAT. YOU'RE WELCOME. IT WAS THE LIGHTS.'"
    narr "Riley shows you the text and laughs."
    narr "You walk the rest of the way laughing."
    narr "Summer starts."
    narr "But this doesn't end."
    narr " "
    narr "Sometimes you just have to say the thing."
    narr "Even if it takes you nine months to get there."

    return

label ending_bad:

    hide riley
    with dissolve

    scene bg hallway
    with fade

    show riley at center
    with dissolve

    narr "~ BAD ENDING: Too Late ~"
    narr " "
    narr "Friday comes and goes."
    narr "The party is fun. You and Riley talk."
    narr "But the moment passes."
    narr "As moments do when you wait too long."
    narr "Summer arrives."
    narr "Riley posts photos of somewhere abroad."
    narr "You like them."
    narr "You don't comment."
    narr "In September, you'll both be somewhere new."
    narr "Different cities, probably."
    narr "You'll think about the hallway."
    narr "About what you didn't say."
    narr " "
    narr "There's always next time."
    narr "Except when there isn't."

    return

label ending_neutral:

    hide riley
    with dissolve

    scene bg cafeteria
    with fade

    show riley at center
    with dissolve

    narr "~ NEUTRAL ENDING: A Start ~"
    narr " "
    narr "You exchange numbers."
    narr "It's a small thing."
    narr "But small things matter."
    narr "Over the summer, you text."
    narr "About nothing much. Memes. Music. What you're reading."
    narr "Riley sends you photos of their sketchbook."
    narr "You tell them they're good every time."
    narr "They say 'shut up' every time."
    narr "They keep sending them."
    narr "In September, before you both leave for your respective new lives,"
    narr "you meet for coffee."
    narr "It goes for three hours."
    narr "Some things are slow."
    narr "That doesn't make them less real."
    narr " "
    narr "This is the beginning of something."
    narr "You're just not sure what yet."

    return

label ending_secret:

    scene bg rooftop
    with fade

    show riley at center
    with dissolve

    narr "~ SECRET ENDING: The Rooftop ~"
    narr " "
    narr "You stay on the rooftop long after the party ends."
    narr "You can hear Jun locking up below."
    narr "You can hear the city."
    narr "Riley sketches you in the low light."
    narr "They warn you it won't be good."
    narr "It is good."
    narr "You walk home at midnight."
    narr "The long way."
    narr "Of course."
    narr "Neither of you planned this."
    narr "That's what makes it matter."
    narr " "
    narr "The best things happen when you almost walk away"
    narr "but don't."

    return
