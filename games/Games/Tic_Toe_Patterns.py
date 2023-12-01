import random


patterns = {
    'regular_moves' : [
    "I've placed my piece at {}. Your move! Where will you go next?",
    "I chose {}. Let's keep this game rolling! Your move.",
    "My move is {}. How will you respond?",
    "I just took {}. What's your strategy to counter that?",
    "Placing my piece at {}. How will you challenge this move?",
    "Your move! I've chosen {}. What's your next move?",
    "At {}, that's my move. How will you respond?",
    "I went for {}. Your turn! What's your plan?",
    "Placed my piece at {}. What's your next move?",
    "At {}, I've made my move. Your move!"
],

# Strategic Move
    'strategic_moves' : [
        "A strategic move: I've taken {}. What's your counter-strategy?",
        "I've placed my piece at {}, setting the stage for an interesting play. Your move!",
        "I've made a move at {}. What's your plan to counter this?",
        "Strategically, I chose {}. How will you adapt?",
        "At {}, a strategic move from me. What's your next move?",
        "I'm setting the tone with {}. Your move - how will you respond?",
        "Taking a strategic approach with {}. What's your strategy now?",
        "Strategic move at {}. How will you counter this?",
        "At {}, a strategic choice. What's your next move?",
        "Strategic play! I've chosen {}. What's your plan?"
    ],

    # Blocking Move
    'blocking_moves' : [
        "I've blocked your potential win by taking {}. How will you adjust your strategy?",
        "To prevent any threats, I've chosen {}. Your move! What's your next move?",
        "I've made a defensive move at {}. How will you break through?",
        "Blocking your path at {}. What's your next move?",
        "At {}, I've blocked your potential victory. What's your response?",
        "Defensive move: {}. Your move! What's your strategy now?",
        "Blocking your path with {}. What's your countermove?",
        "I've taken {}. Your potential win is blocked. How will you respond?",
        "Defensive play at {}. What's your plan to overcome this?",
        "Blocking at {}. Your move! What's your next strategy?"
    ],

    # Surprising Move
    'surprising_moves' : [
        "Surprise! I've placed my piece at {}. Did that catch you off guard?",
        "I've made a surprising move at {}. What are your thoughts on the current board?",
        "Unexpected move, right? I'm at {}. Your move!",
        "Surprising you with {}. How will you react?",
        "Unexpected move: {}. Your move! What's your plan?",
        "Catch me if you can! {}. Your move.",
        "Surprise move at {}. How will you adjust your strategy?",
        "Unexpected choice: {}. What's your next move?",
        "I've added a twist with {}. Your move! How will you respond?",
        "Surprise move at {}. What's your strategy to counter this?"
    ],

    # Expressing Confidence
    'confident_moves' : [
        "Confident move: I've taken {}. Ready for the challenge?",
        "I'm feeling good about this move at {}. What's your strategy now?",
        "With my move at {}, I'm setting the pace. How will you respond?",
        "Confidently placed my piece at {}. Your move!",
        "Feeling confident with {}. What's your next move?",
        "At {}, I'm confident in this move. Your move!",
        "Confidence is key! {}. Your move. What's your strategy?",
        "Placing my piece confidently at {}. How will you counter this?",
        "Confident move at {}. Your move! What's your strategy?",
        "At {}, feeling confident. What's your next move?"
    ],

    # Building Tension
    'tension_moves' : [
    "The game is getting intense! I've chosen {}. What's your next move?",
    "Tension is building with my move at {}. How will you navigate this?",
    "Exciting times! I've made a move at {}. Your move - any surprises up your sleeve?",
    "At {}, the tension rises. What's your strategy now?",
    "The excitement builds! {}. Your move. What's your next plan?",
    "Tension in the air with my move at {}. How will you respond?",
    "At {}, things are heating up. Your move! What's your next strategy?",
    "Tense moments with {}. Your move! What's your plan?",
    "With my move at {}, the game intensifies. What's your next move?",
    "The stakes are high! I've chosen {}. Your move - how will you respond?"
],
    
    "user_winning_texts" : [
        "Congratulations! You've won with {}! Well played.",
        "Victory is yours! {} led you to success. Great job!",
        "Impressive move! With {}, you've claimed victory.",
        "You've outsmarted me with {}! Well done!",
        "A winning strategy! {} secured your victory.",
        "The triumph is yours! Well played with {}.",
        "With {}, you've emerged victorious. Congratulations!",
        "Well done! {} led you to victory.",
        "You've won with {}! Excellent strategy.",
        "Cheers to your victory! {} proved to be the winning move."
    ],
    # Winning Texts for Chatbot
    "chatbot_winning_texts" : [
        "I've secured victory with {}. Better luck next time!",
        "The victory is mine! {} led to my success.",
        "Impenetrable strategy! With {}, I claim victory.",
        "You gave it your best shot, but I triumph with {}.",
        "I emerge victorious! {} proved to be unstoppable.",
        "The tables have turned! I win with {}.",
        "My strategic move with {} secures the win. Better luck next game!",
        "With {}, I claim victory! Well played.",
        "I've outplayed you with {}. Victory is mine!",
        "A winning strategy! {} leads to my triumph."
    ],
    'draw_texts' : [
    "The game ends in a draw! Well played by both sides.",
    "It's a tie! Neither side was able to secure a victory.",
    "A stalemate! The game concludes with no winner.",
    "No winner this time! The game results in a draw.",
    "A deadlock! The game is a draw with no clear victor.",
    "The match ends in a draw. Good effort from both players!",
    "No one takes the lead! The game concludes in a draw.",
    "A balanced game! It's a draw with no winner.",
    "The board is full, and the game is a draw. Well played!",
    "A draw it is! Both sides played evenly throughout the game."
]
}


def get_pattern(type_of_pattern, postion):
    if type_of_pattern == 'surprising_moves' and random.randint(0,10) > 5:
        type_of_pattern = 'confident_moves'
    type_patterns = patterns[type_of_pattern]
    pattern = random.choice(type_patterns)
    if postion is not None:
        pattern = pattern.format(postion+1)
    return pattern
    