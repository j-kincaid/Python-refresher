
path1 = input("Which way do you go? Enter left or right.").lower()
if path1 == "left":
    print('''
    **************************************************************    
                ,      .-;
             ,  |\    / /  __,
             |\ '.`-.|  |.'.-'
              \`'-:  `; : /
               `-._'.  \'|
              ,_.-=` ` `  ~,_
               '--,.    .-. ,=".
                 /     { 0 )`;-.}
                 |      '-' /__ |
                 /          \_,\|
                 |          (
             __ / '          \
     /\_    /,'`|     '   .-~"~~-.
     |`.\_ |   /  ' ,    /        \
   _/  `, \|  ; ,     . |  ,  '  . |
   \   `,  |  |  ,  ,   |  :  ;  : |
   _\  `,  \  |.     ,  |  |  |  | |
   \`  `.   \ |   '     |\_|-'|_,'\|
   _\   `,   `\  '  . ' | |  | |  |           __
   \     `,   | ,  '    |_/'-|_\_/     __ ,-;` /
    \    `,    \ .  , ' .| | | | |   _/' ` _=`|
     `\    `,   \     ,  | | | | |_/'   .="  /
     \`     `,   `\      \ | | ;/'   .="    |
      \      `,    `\' ,  | ; /'    ="    _/
       `\     `,  .-""-. ': /'    ="     /
    jgs _`\    ;_{  '   ; /'    ="      /
       _\`-/__.~  `.8.'."`~-. ="     _,/
    __\      {   '-.|.'.--~'`}"    _/
    \    .="` }.-~"'u'-. '-..'  __/
   _/  ."    {  -'.~('-._,.'\_,/
  /  ."    _/'`--; ;  `.  ;
   .="  _/'      `-..__,-'
    __/'

**************************************************************  
You see a brilliantly colored bird perching in a tree next to the path. It urges you to keep going! You're on the path to the treasure! As you follow along the path, you approach a river bank with a sign pointing to the treasure cave. There is a schedule of boat rides on the sign. 
    ''')
    print("Swim or wait")
    swim_or_wait = input("Do you swim or wait for a boat? Enter swim or wait.").lower()
    if swim_or_wait == "swim":
        which_door = input("Enter red, yellow, or blue.").lower()
        if which_door == "red":
            print("GAME OVER")
        elif which_door == "yellow":
            print('''

            ***********************************************************
                                ____...------------...____
                    __________
                    /\____;;___\
                | /         /
                `. ())oo() .
                    |\(%()*^^()^\
                %| |-%-------|
                % \ | %  ))   |
                %  \|%________|
            ejm97  %%%%
            ***********************************************************
            You found the treasure!!!
            ''')

        else:
            print("GAME OVER")
    else:
        
        print('''
        **************************************************************
                    ____...---...___
    ___.....---"""        .       ""--..____
        .                  .            .
    .             _.--._       /|
            .    .'()..()`.    / /
                ( `-.__.-' )  ( (    .
    .         \        /    \ \
        .      \      /      ) )        .
                .' -.__.- `.-.-'_.'
    .        .'  /-____-\  `.-'       .
            \  /-.____.-\  /-.
            \ \`-.__.-'/ /\|\|           .
            .'  `.    .'  `.
            |/\/\|    |/\/\|
    jro
    **************************************************************  
    Oh no! A komodo dragon is coming up out of the water and it noticed you! Wait... Oh, how awful. Buzzards are already circling above... GAME OVER! 
        ''')
else:
    print('''
***********************************************************
                                       ` )
                              (         (
                               )      (
                             )          )
                            (          ( ,
                           _ _)_      .-Y.
                .--._ _.--'.',T.\_.--' (_)`.
              .'_.   `  _.'  `-'    __._.--;
             /.'  `.  -'     ___.--' ,--.  :       o       ,-. _
            : |  xX|       ,'  .-'`.(   |  '      (   o  ,' .-' `,
           :  `.  .'    ._'-,  \   | \  ||/        `.{  / .'    :
          .;    `'    ,',\|\|   \  |  `.;'     .__(()`./.'  _.-'
          ;           |   ` `    \.'|\\ :      ``.-. _ '_.-'
         .'           ` /|,         `|\\ \        -'' \  \
         :             \`/|,-.       `|\\ :         ,-'| `-.
         :        _     \`/  |   _   .^.'\ \          -'> \_
         `;      --`-.   \`._| ,' \  |  \ : \           )`.\`-
          :.      .---\   \   ,'   | '   \ : .          `  `.\_,/
           :.        __\   `. :    | `-.-',  :               `-'
           `:.     -'   `.   `.`---'__.--'  /
            `:         __.\    `---'      _'
             `:.     -'    `.       __.--'
              `:.          __`--.--'\
         -bf-  `:.      --'     __   `.

***********************************************************    
    '''
        "Oh no! The komodo dragons are on the loose and one has attacked your leg. The venom has immobilized you and you will die within the next few hours. GAME OVER." )
