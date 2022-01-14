import random
import os
import time
data_list = set([ # Create a Set of array'd objects 
(1 , " Whats the best thing youve got going on in your life at the moment?"), 
(2 , " What incredibly common thing have you never done?"), 
(3 , " What has taken you the longest to get good or decent at?"), 
(4 , " What food do you love that a lot of people might find a little odd?"), 
(5 , " If you could start a charity), what would it be for?"), 
(6 , " What was the funniest thing youve seen recently online?"), 
(7 , " What are some of your favorite games to play?"), 
(8 , " What takes a lot of time but is totally worth it?"), 
(9 , " What is the most amazing fact you know?"), 
(10 , " What website or app doesnt exist), but you really wish it did?"), 
(11 , " Whats your favorite type of day(weather), temp), etc , )?"), 
(12 , " What is the most clever or funniest use of advertising youve seen?"), 
(13 , " How into self improvement are you?"), 
(14 , " When someone finds out what you do), or where you are from), what question do they always ask you?"), 
(15 , " Are you more productive at night or in the morning? Do you think its possible to change and get used to another schedule?"), 
(16 , " What scene in a movie always gives you goosebumps every time you watch it?"), 
(17 , " What topic could you give a 20 minute presentation on without any preparation?"), 
(18 , " Whats something that a lot of people are missing out on because they dont know about it?"), 
(19 , " What are some of your guilty pleasures?"), 
(20 , " Who is the most interesting person youve met and talked with?"), 
(21 , " What has really taken a toll on you?"), 
(22 , " How did you spend the money from your very first job?"), 
(23 , " What do you wish someone taught you a long time ago?"), 
(24 , " Do you think you rely too heavily on your phone? Why or why not?"), 
(25 , " How could carousels be spiced up so they are more exciting?"), 
(26 , " Whats your favorite car that youve owned?"), 
(27 , " What subjects should be taught in school but arent?"), 
(28 , " Whats the biggest vehicle youve driven?"), 
(29 , " What songs would be played on a loop in hell?"), 
(30 , " What rule do you wish they would introduce into your favorite sport?"), 
(31 , " What kind of challenges are you facing these days?"), 
(32 , " What do you highly recommend to most people you meet?"), 
(33 , " Do you think you have a pretty good work life balance? Why or why not?"), 
(34 , " What was the last thing you were really excited about?"), 
(35 , " Whats your best “my coworkers are crazy” story?"), 
(36 , " What does your perfect breakfast look like?"), 
(37 , " What are some of your favorite holiday traditions that you did while growing up?"), 
(38 , " If you could choose your dreams), what would you prefer to dream about?"), 
(39 , " Would you ride in a zeppelin if given a chance?"), 
(40 , " Whats something that was once important but is now becoming less and less relevant?"), 
(41 , " What tells you the most about a person?"), 
(42 , " When is the most interesting period in history?"), 
(43 , " What is the best pair of shoes you have owned?"), 
(44 , " What book had the most significant impact on you?"), 
(45 , " Wheres your favorite place to nap?"), 
(46 , " What is the best event youve attended?"), 
(47 , " What do you buy way more of than most people?"), 
(48 , " What do you rebel against?"), 
(49 , " What well known person does the most good for the world?"), 
(50 , " Whats your favorite food combination?"), 
(51 , " Whats the weirdest way you have met someone?"), 
(52 , " Whats the most amazing natural occurrence youve witnessed?"), 
(53 , " How did you get that scar of yours?"), 
(54 , " What do you wish was illegal?"), 
(55 , " If someone came up to you and said “Hey), do that thing you do!”), what thing would pop into your head first?"), 
(56 , " Who is the most intelligent or creative person you know?"), 
(57 , " What wastes the most time in your day to day life?"), 
(58 , " Whats a problem you have), that might be entirely unique to you?"), 
(59 , " What company or brand did you love until they betrayed your trust?"), 
(60 , " Would you ever try space tourism), if you had the money for it?"), 
(61 , " Whats the most annoying machine you must deal with regularly?"), 
(62 , " What are you grateful for?"), 
(63 , " What hobby would you be a lot of fun to get into?"), 
(64 , " What do you resent paying for most?"), 
(65 , " What pets did you have growing up?"), 
(66 , " Whats the best or worst prank youve played on someone?"), 
(67 , " What was the scariest movie youve seen?"), 
(68 , " What motivates you?"), 
(69 , " Where are five places you really want to visit before you die?"), 
(70 , " Whats the best location to fully enjoy a good cup of coffee?"), 
(71 , " How handy are you when it comes to fixing things?"), 
(72 , " What skill or talent would you most like to learn?"), 
(73 , " What weird thing do you have nostalgia for?"), 
(74 , " What works of art have really made an impression on you?"), 
(75 , " What culture would you like to learn more about?"), 
(76 , " If you were featured on the local news), what would you most likely be on there for?"), 
(77 , " What do you wish your phone could do?"), 
(78 , " Whats your favorite international food?"), 
(79 , " What workers have the worst jobs?"), 
(80 , " What kind of physical activities do you like doing?"), 
(81 , " Would you rather watch a movie on your TV at home or on the big screen in the theater), and why?"), 
(82 , " What assumption you made went hilariously wrong?"), 
(83 , " What big problem do you think technology will solve next?"), 
(84 , " What fashion trend needs to be brought back?"), 
(85 , " How do you think you will be/act when you are old?"), 
(86 , " Whats your favorite way to waste time online?"), 
(87 , " Whats the longest trip youve been on?"), 
(88 , " What was something you thought would be easy until you tried it?"), 
(89 , " What), in your opinion), is the most amazing animal?"), 
(90 , " How into tech are you? Why?"), 
(91 , " What is the biggest mistake youve made at work?"), 
(92 , " Who is the oldest person you know personally? What interesting stories have they told you?"), 
(93 , " Who is the funniest person in your family?"), 
(94 , " What useless facts do you know?"), 
(95 , " Whats your favorite Olympic sport to watch?"), 
(96 , " How do you usually get your news?"), 
(97 , " What smell do you hate that doesnt seem to bother other people?"), 
(98 , " Whats the most delightful hotel or house youve stayed in on vacation?"), 
(99 , " What weird quirks did you pick up from your parents?"), 
(100 , " What were your favorite television shows when you were growing up?"), 
(101 , " Whats the silliest thing you are pretty good at?"), 
(102 , " Whats your idea of a great day?"), 
(103 , " What are some of the dumbest misadventures youve been on?"), 
(104 , " What do you want to do when you retire?"), 
(105 , " What do you do to unwind after a hard day?"), 
(106 , " Who is the most competitive person you know?"), 
(107 , " Would you rather spend time with other people or at home alone?"), 
(108 , " What are some films that would make it on to your top 50 list of movies?"), 
(109 , " What slang are you really happy went out of fashion?"), 
(110 , " What music do you put on when you want to get pumped?"), 
(111 , " What makes you feel old when you think about it?"), 
(112 , " How well do you know your neighbors?"), 
(113 , " Whats the best backhanded compliment youve heard / can think of on the spot?"), 
(114 , " Who is the most interesting stranger youve met?"), 
(115 , " What was your funniest or worst experience with a dentist?"), 
(116 , " Whats the noblest endeavor a person can dedicate their life to?"), 
(117 , " Whats your idea of a great party?"), 
(118 , " What are some of your favorite scenes from movies?"), 
(119 , " What are two of your favorite snacks?"), 
(120 , " Whats the biggest adventure youve been on?"), 
(121 , " Besides war and diplomacy), what would be the best way for countries to settle disputes?"), 
(122 , " What household chore do you actually enjoy?"), 
(123 , " What is something you do better than most people and something you do worse than most people?"), 
(124 , " What TV show are you hooked on or were recently hooked on?"), 
(125 , " If you had to lose one of your senses), which would you choose to lose?"), 
(126 , " If a new volcano formed and the government had an online contest to see what it would be named), what name would you submit?"), 
(127 , " What is the last goal you achieved?"), 
(128 , " What was your worst haircut experience?"), 
(129 , " Do you prefer pens or pencils? Why?"), 
(130 , " Whats the best way to stay young?"), 
(131 , " What is the most stressful TV show or movie you watched?"), 
(132 , " How good are you at drawing?"), 
(133 , " What did your teachers and parents say would be really important when you grew up), but it hasnt been?"), 
(134 , " How do you feel about clowns?"), 
(135 , " What is your favorite genre of movie? Why?"), 
(136 , " What brands do you love/hate the most?"), 
(137 , " What is the weirdest food combination youve made and tried?"), 
(138 , " What would you change if you were in charge of the company you work for?"), 
(139 , " Who has been your most interesting/confusing/annoying neighbor?"), 
(140 , " Has there ever been a time when something so amazing or unexpected happened that it literally left you speechless for a time?"), 
(141 , " Wheres the most surreal area you been to?"), 
(142 , " What are common misconceptions about your job?"), 
(143 , " What public spaces do you feel most comfortable in? (Library), bar), park), mall), stadium), etc)?"), 
(144 , " Whats the most outdated piece of tech you still use regularly?"), 
(145 , " Whats the weirdest food youve eaten?"), 
(146 , " Who was your favorite teacher?"), 
(147 , " What recent trend are you totally on board with?"), 
(148 , " What about becoming an adult caught you completely off guard?"), 
(149 , " How often do you dance?"), 
(150 , " Whats the best cake youve ever eaten?"), 
(151 , " What kind of art do you appreciate the most?"), 
(152 , " What crossed way too far into the uncanny valley for you?"), 
(153 , " Whats your favorite thing about the area/city/state you live in?"), 
(154 , " Whats the best day youve had recently?"), 
(155 , " Whats your favorite way to spend time outdoors?"), 
(156 , " What does your perfect burger or sandwich have in it?"), 
(157 , " Whats the worst advice youve been given?"), 
(158 , " Whats the strangest name someone you have met had?"), 
(159 , " What was something courageous youve (in person) seen someone do?"), 
(160 , " What card or board games do you like to play?"), 
(161 , " What are you best at fixing?"), 
(162 , " What movie never gets old no matter how many times youve seen it?"), 
(163 , " If the universe is just a simulation), what update or patch does it need?"), 
(164 , " Where have you traveled to?"), 
(165 , " Whats the scariest horror movie or horror book monster?"), 
(166 , " Whats the most unique shop or restaurant youve been in?"), 
(167 , " What hard time in your life left you a better person after it was finished?"), 
(168 , " Whats the best sports game youve been to?"), 
(169 , " What period would be the best to be born in?"), 
(170 , " What sport do you wish you knew more about?"), 
(171 , " Whats something youre looking forward to?"), 
(172 , " Whats the most creative thing youve done?"), 
(173 , " What are you hilariously bad at?"), 
(174 , " Tell me about a time you were totally out of your element/comfort zone ?"), 
(175 , " Are you a cat or dog person or neither? Why?"), 
(176 , " Who is the most gifted person you know?"), 
(177 , " What was your best vacation?"), 
(178 , " What do you usually do on your commute to work?"), 
(179 , " What was the craziest theme park or fair ride youve been on?"), 
(180 , " What kind of people do you most enjoy hanging out with?"), 
(181 , " What do you think the ideal age to be is?"), 
(182 , " What are you kind of snobby about?"), 
(183 , " What toy did you hate most as a child?"), 
(184 , " Whats your drink of choice (Either alcoholic or non)?"), 
(185 , " If you left your current life behind and ran away to follow your dreams), what would you be doing?"), 
(186 , " What food is underrated or underappreciated?"), 
(187 , " Whats your favorite line from a book or a movie?"), 
(188 , " What is the best thing you have ever bought?"), 
(189 , " What catchy jingle or bit of advertising has stuck with you all these years?"), 
(190 , " What luxury is totally worth the price?"), 
(191 , " What is the most unique or silliest problem you have going on in your life at the moment?"), 
(192 , " What could movie theaters do to improve the experience of going there?"), 
(193 , " If you were so wealthy you didnt need to work), what would you do with your time?"), 
(194 , " What apps do you use most?"), 
(195 , " What is the most tedious and/or the most exciting sport to watch?"), 
(196 , " Whats your favorite island that you've visited?"), 
(197 , " What do you geek out about?"), 
(198 , " Besides insects and spiders), what animals annoy you the most?"), 
(199 , " Whats your favorite month?"), 
(200 , " Whats the best concert youve been to and why was it so good?")
])

hat = '''
                        oooo     oooo
                    o$$"""$oo$$"""""$o
                    $"      $$"      $$$$
                $"      ""        $$$$$o
                $                  $$$$$o
                $                    $$$$$$
                $"                    "$$$$$
                $                      $$$$$$
                $"                      $$$$$$
                $                        $$$$$
                $                       o$$$$$
                $                       $$$$$$
                $                      o$$$$$$
            ooo                      o$$$$$$$
    ooo$$$$"" $                   oo$$$$$""""""oooo
oo"$$$$$$$ oo"" oooooooooooooooo$$"""           o$$"oo
o"  $$$$$$$ "$o           oo$$$$$"               $$$$o"$o
$    $$$$$$$  " ""oooooooooo$$$$"         o$      $$$$$$o"$
o     $$""               oo$$$"           o$$     o$$$$$$$o$
"o    $$             oo$$$$""            o$$$   o$$$$$$$$$$$
"$o  $$$oo                           $$$$$$$   ooo$$$$$""
"$$oooo ""            ooo$$$$      $$$$$$$$$$$$$$""
    """"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$""""""


Welcome to Magic Hat! The teambuilding question and answer game. There's two options here, Either have the hat give you a question, 
Or enter an interval for the magic hat to give you questions! Ready to get started?
Enter 1 to ask the hat for a single question
Enter 2 to then be promted to enter an interval for a number of questions
'''

hat2 = '''
                        oooo     oooo
                    o$$"""$oo$$"""""$o
                    $"      $$"      $$$$
                $"      ""        $$$$$o
                $                  $$$$$o
                $                    $$$$$$
                $"                    "$$$$$
                $                      $$$$$$
                $"                      $$$$$$
                $                        $$$$$
                $                       o$$$$$
                $                       $$$$$$
                $                      o$$$$$$
            ooo                      o$$$$$$$
    ooo$$$$"" $                   oo$$$$$""""""oooo
oo"$$$$$$$ oo"" oooooooooooooooo$$"""           o$$"oo
o"  $$$$$$$ "$o           oo$$$$$"               $$$$o"$o
$    $$$$$$$  " ""oooooooooo$$$$"         o$      $$$$$$o"$
o     $$""               oo$$$"           o$$     o$$$$$$$o$
"o    $$             oo$$$$""            o$$$   o$$$$$$$$$$$
"$o  $$$oo                           $$$$$$$   ooo$$$$$""
"$$oooo ""            ooo$$$$      $$$$$$$$$$$$$$""
    """"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$""""""


The Magic Hat is thinking! Hold on....
'''


if __name__ == "__main__":
  
    current_list = data_list.copy() # Datalist is a global, so we need to create a copy
    try: 
        while True:
            os.system('cls' if os.name == 'nt' else 'clear') # Clear Function
            print(hat)    
            grabbed_input = input("")
            if grabbed_input == "1": # Grab A Question
                os.system('cls' if os.name == 'nt' else 'clear') # Clear Function
                if len(current_list) == 0:
                    current_list = data_list.copy() # Creates a clean copy to repeat questions
                else: 
                    dirty_question = random.choices(list(current_list), k = 1) # Grabs a singel choice at random from the list
                    clean_question = dirty_question[0] # Grabs the index @ 0 (As we created the list of choices), which gives us our tuple
                    index, question = clean_question # Cleans Question
                    current_list.remove(clean_question) # Removes from bank
                    print(hat2)
                    time.sleep(3)
                    print(question)
                    time.sleep(10)
            if grabbed_input == "2": # Grab a time
                print("INTERVAL TIME")
                grab_time = int(input("On what interval do you want questions? (Every x seconds): "))
                print("OK, the magic hat will print questions every: " + str(grab_time) + " Seconds")
                time.sleep(3)
                try: 
                    while True:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        # There's a better way to do this, but I'm not sure what it is without a ton of libraries
                        print("Press CTRL-C to Ask the hat to stop the periodic questions") 
                        if len(current_list) == 0:
                            current_list = data_list.copy() # Creates a clean copy to repeat questions
                        else: 
                            dirty_question = random.choices(list(current_list), k = 1) # Grabs a singel choice at random from the list
                            clean_question = dirty_question[0] # Grabs the index @ 0 (As we created the list of choices), which gives us our tuple
                            index, question = clean_question # Cleans Question
                            current_list.remove(clean_question) # Removes from bank
                            print(hat2)
                            if grab_time > 10:
                                grab_time -= 3
                                time.sleep(3)
                            print(question)
                        time.sleep(int(grab_time))
                except KeyboardInterrupt: # Catches the interupt signal
                    os.system('cls' if os.name == 'nt' else 'clear') # Clear Function
                    pass
    except KeyboardInterrupt: # Catches the interupt signal
        print("Thank you for playing magic hat!")
        exit()
        
