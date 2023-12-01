patterns_list = [
        "[Intro], [Name] is a [Gender] [Religion] name meaning '[Meaning]'. It symbolizes [Symbolism].",
        "[Intro], [Name] is a [Gender] [Religion] name associated with [Meaning]. It represents [Symbolism].",
        "[Name] is a popular [Gender] name in [Religion] culture, signifying [Meaning]. It embodies [Symbolism].",
        "[Name], commonly used in [Religion], is a meaningful [Gender] name denoting [Meaning]. It reflects [Symbolism].",
        "In the context of [Religion], [Name] is a beloved choice for [Gender]s. Its meaning, '[Meaning],' conveys [Symbolism].",
        "[Intro], [Name] is a name deeply rooted in [Religion], carrying the significance of [Meaning]. It exemplifies [Symbolism].",
        "[Name], a [Religion] name, holds a special place for [Gender]s. Its meaning, '[Meaning],' symbolizes [Symbolism].",
        "[Name], derived from [Religion], is a cherished [Gender] name with the profound meaning of [Meaning]. It embodies [Symbolism].",
        "In [Religion], [Name] is a name chosen for [Gender]s, representing [Meaning]. It signifies [Symbolism].",
        "[Name], a [Gender] name associated with [Religion], carries the beautiful meaning of [Meaning]. It encompasses [Symbolism].",
        "The name [Name] is commonly chosen for [Gender]s in [Religion]. Its meaning, '[Meaning],' reflects [Symbolism].",
        "In [Religion], the name [Name] signifies [Meaning]. It is a popular choice for [Gender]s, symbolizing [Symbolism].",
        "Looking for a unique [Gender] name in [Religion]? Consider [Name], which means '[Meaning]' and embodies [Symbolism].",
        "Searching for a meaningful [Gender] name? Look no further than [Name] in [Religion], representing [Meaning] and [Symbolism].",
        "[Name], a name rooted in [Religion], carries the essence of [Meaning]. It is a cherished choice for [Gender]s, symbolizing [Symbolism].",
        "Need a name with a significant meaning? [Name] in [Religion] is a perfect choice for [Gender]s, representing [Meaning] and [Symbolism].",
        "[Name] is a beloved [Religion] name for [Gender]s, symbolizing [Symbolism] and carrying the profound meaning of [Meaning].",
        "When it comes to [Gender] names in [Religion], [Name] stands out with its beautiful meaning of '[Meaning]' and the symbolism of [Symbolism].",
        "Choose [Name] for your [Gender] in [Religion] to embrace the deep meaning of '[Meaning]' and the symbolism of [Symbolism].",
        "Looking for a [Religion] name with a touch of sweetness? [Name], meaning '[Meaning],' represents [Symbolism] for [Gender]s.",
        "[Name] is a [Gender] name derived from [Religion], carrying the meaning of [Meaning]. It symbolizes [Symbolism].",
        "In [Religion], [Name] is a popular choice for [Gender]s due to its profound meaning of [Meaning]. It embodies [Symbolism].",
        "Consider the name [Name] for your [Gender] in [Religion]. Its meaning, '[Meaning],' reflects the essence of [Symbolism].",
        "[Name], a meaningful [Religion] name for [Gender]s, encapsulates the beauty of [Meaning] and represents [Symbolism].",
        "Looking for a [Religion] name? [Name] is a beloved choice for [Gender]s, signifying [Meaning] and embodying [Symbolism].",
        "The name [Name] in [Religion] holds the significance of [Meaning]. It is a perfect fit for [Gender]s and symbolizes [Symbolism].",
        "[Name] is a unique [Gender] name associated with [Religion], representing [Meaning] and carrying the symbolism of [Symbolism].",
        "Embrace the meaningfulness of [Name], a [Religion] name for [Gender]s. Its essence of [Meaning] reflects [Symbolism].",
        "Discover the beauty of [Name], a name commonly used in [Religion]. It carries the profound meaning of [Meaning] and symbolizes [Symbolism].",
        "[Name] is a cherished [Gender] name in [Religion], signifying [Meaning] and capturing the essence of [Symbolism].",
        "[Name] is a name of [Religion] origin, often chosen for [Gender]s. Its meaning, '[Meaning],' conveys the symbolism of [Symbolism].",
        "In [Religion], the name [Name] represents the essence of [Meaning]. It is a beloved choice for [Gender]s, symbolizing [Symbolism].",
        "Searching for a significant [Gender] name? [Name] in [Religion] holds the deep meaning of [Meaning] and the symbolism of [Symbolism].",
        "[Name], derived from [Religion], carries the essence of [Meaning]. It is a unique choice for [Gender]s, symbolizing [Symbolism].",
        "Looking for a [Religion] name? Consider [Name] for your [Gender], as it embodies the meaning of [Meaning] and represents [Symbolism].",
        "The name [Name], rooted in [Religion], represents the essence of [Meaning]. It is a cherished choice for [Gender]s, symbolizing [Symbolism].",
        "Seeking a meaningful [Religion] name? [Name], with its beautiful meaning of [Meaning], captures the essence of [Symbolism] for [Gender]s.",
        "Choose [Name] as a [Gender] name in [Religion] to embrace the deep meaning of [Meaning] and the symbolism of [Symbolism].",
        "[Name], a [Religion] name, is associated with [Meaning] and embodies [Symbolism]. It is a perfect fit for [Gender]s.",
        "In [Religion], [Name] is a popular choice for [Gender]s. Its meaning, '[Meaning],' reflects [Symbolism] and carries a profound significance."
    ]


qualities = {
    "A": ["Adaptable", "Adventurous", "Affable", "Affectionate", "Ambitious", "Amiable", "Assertive", "Attentive", "Authentic", "Avant-garde", "Avid", "Artistic", "Astute", "Athletic", "Auspicious", "Aesthetic", "Altruistic", "Able", "Appreciative", "Amusing"],
    "B": ["Bold", "Brave", "Bright", "Brilliant", "Benevolent", "Blissful", "Bubbly", "Boundless", "Balanced", "Beautiful", "Beloved", "Bountiful", "Brainy", "Brawny", "Blithe", "Breathtaking", "Broad-minded", "Businesslike", "Busy", "Boisterous"],
    "C": ["Calm", "Capable", "Caring", "Candid", "Clever", "Compassionate", "Confident", "Considerate", "Creative", "Curious", "Charming", "Cheerful", "Coherent", "Comical", "Consistent", "Courageous", "Courteous", "Crisp", "Cultured", "Cunning"],
    "D": ["Daring", "Dazzling", "Debonair", "Decisive", "Delightful", "Dependable", "Determined", "Devoted", "Dignified", "Discerning", "Disciplined", "Discreet", "Dynamic", "Distinctive", "Dreamy", "Driven", "Dutiful", "Dazzling", "Decent", "Down-to-earth"],
    "E": ["Eager", "Easygoing", "Eccentric", "Educated", "Efficient", "Elegant", "Eloquent", "Empathetic", "Energetic", "Enthusiastic", "Entrepreneurial", "Equal", "Ethical", "Excellent", "Exciting", "Expressive", "Extraordinary", "Exuberant", "Easy to talk to", "Effervescent"],
    "F": ["Fabulous", "Fair", "Fantastic", "Fearless", "Fierce", "Friendly", "Focused", "Forgiving", "Funny", "Free-spirited", "Fascinating", "Fervent", "Fiery", "Fitting", "Flawless", "Flowing", "Fluent", "Fluffy", "Forgiving", "Frank"],
    "G": ["Generous", "Gentle", "Genuine", "Glamorous", "Glowing", "Graceful", "Gracious", "Grandiose", "Great-hearted", "Grounded", "Growing", "Guiding", "Gutsy", "Good", "Good-natured", "Gregarious", "Guarded", "Goal-oriented", "Gleeful", "Grateful"],
    "H": ["Happy", "Hard-working", "Harmonious", "Healthy", "Heartfelt", "Hearty", "Healing", "Helpful", "Honest", "Honorable", "Hopeful", "Humble", "Humorous", "Hypnotic", "Hospitable", "Hardy", "Handsome", "High-spirited", "High-reaching", "Holistic"],
    "I": ["Idealistic", "Imaginative", "Impartial", "Impressive", "Industrious", "Innovative", "Inquisitive", "Insightful", "Intelligent", "Intense", "Intrepid", "Inventive", "Irresistible", "Inspiring", "Influential", "Independent", "Inventive", "Inquisitive", "Inclusive", "Iconic"],
    "J": ["Jolly", "Joyful", "Jovial", "Jubilant", "Judicious", "Just", "Jazzy", "Jaunty", "Jocular", "Jittery", "Jumpy", "Jitterbug", "Jitterbugging", "Jambalaya", "Jagged", "Jaded", "Jamming", "Jaunting", "Jubilating", "Juking"],
    "K": ["Kind", "Keen", "Knowledgeable", "Kaleidoscopic", "Kaput", "Keen-eyed", "Kooky", "Kosher", "Kissable", "Knockout", "Kittenish", "Knavish", "Kingly", "Knightly", "Knowable", "Kooky", "Kick-ass", "Kind-hearted", "Kooky-crazy", "Kaleidoscopic"],
    "L": ["Lively", "Loving", "Loyal", "Luminous", "Lucky", "Literate", "Logical", "Limitless", "Liberated", "Lyrical", "Legendary", "Leisurely", "Level-headed", "Light-hearted", "Loud", "Luxuriant", "Laid-back", "Lucky", "Loving-kindness", "Luscious"],
    "M": ["Motivated", "Magical", "Magnetic", "Majestic", "Masterful", "Mellow", "Memorable", "Merry", "Methodical", "Mindful", "Modest", "Mature", "Musical", "Magnificent", "Marvellous", "Meek", "Modern", "Merciful", "Majestic", "Motivational"],
    "N": ["Nurturing", "Natural", "Neat", "Nice", "Nimble", "Noble", "Nurtured", "Nifty", "Nimble-fingered", "Nirvanic", "Noble-minded", "Nondiscriminatory", "Non-judgmental", "Notable", "Noteworthy", "Numerical", "Nutritious", "Nautical", "Navigational", "Nimble-footed"],
    "O": ["Optimistic", "Organized", "Original", "Outgoing", "Open-minded", "Observant", "Objective", "Outstanding", "Overwhelming", "Overjoyed", "Over the moon", "Overpowering", "Obedient", "Olympic", "On-the-ball", "On-target", "One-of-a-kind", "Out-of-this-world", "Outspoken", "Overflowing"],
    "P": ["Passionate", "Patient", "Persistent", "Positive", "Playful", "Polite", "Powerful", "Practical", "Precise", "Prepared", "Productive", "Professional", "Proud", "Peaceful", "Pleasant", "Precious", "Prompt", "Prominent", "Praiseworthy", "Proactive"],
    "Q": ["Quick-witted", "Quiet", "Quirky", "Quixotic", "Quaint", "Qualified", "Quantifiable", "Quiescent", "Quality-minded", "Queenly", "Questioning", "Quick-thinking", "Quick-tempered", "Quarrelsome", "Quotable", "Quavered", "Quarantine", "Quantum", "Quivering", "Quellable"],
    "R": ["Resilient", "Resourceful", "Respectful", "Responsible", "Romantic", "Reliable", "Radiant", "Rational", "Reasonable", "Refreshing", "Rejoicing", "Relaxed", "Receptive", "Renowned", "Robust", "Rhapsodic", "Ravishing", "Razor-sharp", "Reassuring", "Rhapsodizing"],
    "S": ["Sincere", "Sensitive", "Strong", "Stylish", "Supportive", "Smart", "Spirited", "Sociable", "Sophisticated", "Successful", "Serene", "Stimulating", "Self-assured", "Selfless", "Serendipitous", "Sumptuous", "Sustainable", "Sagacious", "Stupendous", "Sassy"],
    "T": ["Trustworthy", "Talented", "Tactful", "Tenacious", "Thoughtful", "Thrifty", "Tolerant", "Transparent", "Transformative", "Truthful", "Trendy", "Tireless", "Triumphant", "Terrific", "Terrifying", "Thrilled", "Tantalizing", "Teeming", "Tempting", "Tender-hearted"],
    "U": ["Understanding", "Unflappable", "Unpretentious", "Unwavering", "Upbeat", "Unbiased", "Uncommon", "Unconventional", "Uninhibited", "Unique", "Ultimate", "Unstoppable", "Upstanding", "Uplifting", "Unselfish", "Urgent", "Undaunted", "Unforgettable", "Unfailing", "Ubiquitous"],
    "V": ["Vibrant", "Versatile", "Valiant", "Valuable", "Vigilant", "Virtuous", "Visionary", "Vivacious", "Venturesome", "Valedictory", "Venerated", "Voluminous", "Voluptuous", "Vivifying", "Vigorous", "Vexatious", "Vigilante", "Vocalizing", "Venerated", "Venerable"],
    "W": ["Wise", "Witty", "Warm-hearted", "Well-informed", "Well-rounded", "Willing", "Wondrous", "Winning", "Wealthy", "Wholesome", "Welcoming", "Wonder-struck", "Workaholic", "World-class", "Worshipful", "Wistful", "Windswept", "Wondrous", "Whimsical", "Wavy-haired"],
    "X": ["Xenial", "Xenodochial", "Xenolithic", "Xeric", "Xylographic", "Xanthic", "Xenogenic", "Xerothermic", "Xerophytic", "Xylophagous", "Xenophobic", "Xyloid", "Xenotropic", "Xylophilous", "Xanthochroic", "Xenotropic", "Xenotransplantable", "Xerophilous", "Xylotomous", "Xenogamous"],
    "Y": ["Youthful", "Yearning", "Yielding", "Yummy", "Yare", "Yogic", "Yarely", "Yampy", "Yester", "Yearlong", "Yeasty", "Yippee", "Yummylicious", "Yin", "Yarely", "Yellowish", "Yellow-bellied", "Yawning", "Yarely", "Youngish"],
    "Z": ["Zealous", "Zestful", "Zippy", "Zany", "Zippy", "Zonal", "Zillionaire", "Zappy", "Zygodactyl", "Zealotic", "Zeitgeisty", "Zestiness", "Zestily", "Zigzagging", "Zesty", "Zooarchaeological", "Zoomorphic", "Zoophoric", "Zoophilous", "Zoophagous"]
}


sorry= [
    "I'm sorry, but I don't have any information on that topic",
    "Unfortunately, I don't have any data related to what you're asking for.",
    "I'm afraid I don't understand what you're looking for.",
    "I'm sorry, but I don't have any relevant data to provide.",
    "I'm unable to find any information that matches your request.",
    "I'm sorry, but I cannot assist you with that particular matter.",
    "I'm afraid I don't have the capability to answer that question.",
    "Unfortunately, I'm not able to provide you with a helpful response.",
    "I'm sorry, but I don't have any knowledge related to your inquiry.",
    "I'm unable to help you with that topic, as it is outside my area of expertise.",
    "I'm sorry, but I couldn't find any information related to your query.",
    "I'm sorry, but your query does not match any data in my system.",
    "I'm unable to find any relevant data based on your query.",
    "I'm sorry, but I don't have any data that matches your request.",
    "I'm afraid I couldn't understand your query. Could you please rephrase it?",
    "I'm sorry, but the information you're looking for is not available in my database.",
    "I'm unable to provide any information on that topic as it is outside my scope.",
    "I'm sorry, but I don't have any data that corresponds to your query.",
    "I'm afraid I cannot help you with that query as it is not within my area of expertise."
]

fake_vars = ['aadhaar_card_number', 'aba', 'address', 'administrative_unit', 'am_pm', 'android_platform_token', 'ascii_company_email', 'ascii_email', 'ascii_free_email', 'ascii_safe_email', 'bank_country', 'basic_phone_number', 'bban', 'binary', 'boolean', 'bothify', 'bs', 'building_number', 'catch_phrase', 'century', 'chrome', 'city', 'city_prefix', 'city_suffix', 'color', 'color_name', 'company', 'company_email', 'company_suffix', 'coordinate', 'country', 'country_calling_code', 'country_code', 'credit_card_expire', 'credit_card_full', 'credit_card_number', 'credit_card_provider', 'credit_card_security_code', 'cryptocurrency', 'cryptocurrency_code', 'cryptocurrency_name', 'csv', 'currency', 'currency_code', 'currency_name', 'currency_symbol', 'current_country', 'current_country_code', 'date', 'date_between', 'date_between_dates', 'date_object', 'date_of_birth', 'date_this_century', 'date_this_decade', 'date_this_month', 'date_this_year', 'date_time', 'date_time_ad', 'date_time_between', 'date_time_between_dates', 'date_time_this_century', 'date_time_this_decade', 'date_time_this_month', 'date_time_this_year', 'day_of_month', 'day_of_week', 'dga', 'domain_name', 'domain_word', 'dsv', 'ean', 'ean13', 'ean8', 'ein', 'email', 'emoji', 'file_extension', 'file_name', 'file_path', 'firefox', 'first_name', 'first_name_female', 'first_name_male', 'first_name_nonbinary', 'fixed_width', 'free_email', 'free_email_domain', 'future_date', 'future_datetime', 'get_providers', 'hex_color', 'hexify', 'hostname', 'http_method', 'iana_id', 'iban', 'image', 'image_url', 'internet_explorer', 'invalid_ssn', 'ios_platform_token', 'ipv4', 'ipv4_address', 'ipv4_network_class', 'ipv4_private', 'ipv4_public', 'ipv6', 'ipv6_address', 'isbn10', 'isbn13', 'iso8601', 'items', 'itin', 'job', 'json', 'json_bytes', 'language_code', 'language_name', 'last_name', 'last_name_female', 'last_name_male', 'last_name_nonbinary', 'latitude', 'latlng', 'lexify', 'license_plate', 'linux_platform_token', 'linux_processor', 'local_latlng', 'locale', 'localized_ean', 'localized_ean13', 'localized_ean8', 'location_on_land', 'longitude', 'mac_address', 'mac_platform_token', 'mac_processor', 'md5', 'military_apo', 'military_dpo', 'military_ship', 'military_state', 'mime_type', 'month', 'month_name', 'msisdn', 'name', 'name_female', 'name_male', 'name_nonbinary', 'nic_handle', 'nic_handles', 'null_boolean', 'numerify', 'opera', 'paragraph', 'paragraphs', 'password', 'past_date', 'past_datetime', 'phone_number', 'port_number', 'postalcode', 'postalcode_in_state', 'postalcode_plus4', 'postcode', 'postcode_in_state', 'prefix', 'prefix_female', 'prefix_male', 'prefix_nonbinary', 'pricetag', 'profile', 'psv', 'pybool', 'pydecimal', 'pydict', 'pyfloat', 'pyint', 'pyiterable', 'pylist', 'pyobject', 'pyset', 'pystr', 'pystr_format', 'pystruct', 'pytimezone', 'pytuple', 'random_choices', 'random_digit', 'random_digit_not_null', 'random_digit_not_null_or_empty', 'random_digit_or_empty', 'random_element', 'random_elements', 'random_int', 'random_letter', 'random_letters', 'random_lowercase_letter', 'random_number', 'random_sample', 'random_uppercase_letter', 'randomize_nb_elements', 'rgb_color', 'rgb_css_color', 'ripe_id', 'safari', 'safe_color_name', 'safe_domain_name', 'safe_email', 'safe_hex_color', 'sbn9', 'secondary_address', 'seed_instance', 'sentence', 'sentences', 'sha1', 'sha256', 'simple_profile', 'slug', 'ssn', 'state', 'state_abbr', 'street_address', 'street_name', 'street_suffix', 'suffix', 'suffix_female', 'suffix_male', 'suffix_nonbinary', 'swift', 'swift11', 'swift8', 'tar', 'text', 'texts', 'time', 'time_delta', 'time_object', 'time_series', 'timezone', 'tld', 'tsv', 'unix_device', 'unix_partition', 'unix_time', 'upc_a', 'upc_e', 'uri', 'uri_extension', 'uri_page', 'uri_path', 'url', 'user_agent', 'user_name', 'uuid4', 'windows_platform_token', 'word', 'words', 'year', 'zip', 'zipcode', 'zipcode_in_state', 'zipcode_plus4']


joke_categories = [
    "Programming",
    "Miscellaneous",
    "Pun",
    "Spooky",
    "Christmas"
]

cards = ('Ace of Spades', '2 of Spades', '3 of Spades', '4 of Spades', '5 of Spades', '6 of Spades', '7 of Spades', '8 of Spades', '9 of Spades', '10 of Spades', 'Jack of Spades', 'Queen of Spades', 'King of Spades', 'Ace of Hearts', '2 of Hearts', '3 of Hearts', '4 of Hearts', '5 of Hearts', '6 of Hearts', '7 of Hearts', '8 of Hearts', '9 of Hearts', '10 of Hearts', 'Jack of Hearts', 'Queen of Hearts', 'King of Hearts', 'Ace of Diamonds', '2 of Diamonds', '3 of Diamonds', '4 of Diamonds', '5 of Diamonds', '6 of Diamonds', '7 of Diamonds', '8 of Diamonds', '9 of Diamonds', '10 of Diamonds', 'Jack of Diamonds', 'Queen of Diamonds', 'King of Diamonds', 'Ace of Clubs', '2 of Clubs', '3 of Clubs', '4 of Clubs', '5 of Clubs', '6 of Clubs', '7 of Clubs', '8 of Clubs', '9 of Clubs', '10 of Clubs', 'Jack of Clubs', 'Queen of Clubs', 'King of Clubs')
card_patterns = (
    "Here is a random card: {card_name}",    "You got the {card_name}!",
    "The selected card is: {card_name}",
    "Behold! The card of the day is: {card_name}",
    "And the winner is... {card_name}!",
    "You drew the {card_name}!",
    "It's a lucky day! The card you picked is {card_name}.",
    "The magic card is revealed: {card_name}!",
    "In the game of cards, fortune favors the {card_name}.",
    "The universe has spoken, presenting you with the {card_name}.",
    "Behold the power of the {card_name}!",
    "Your fate lies in the {card_name}.",
    "A whisper in the wind reveals the {card_name}.",
    "The {card_name} holds the key to your destiny.",
    "Gather 'round and witness the marvel that is the {card_name}!",
    "Luck smiles upon you with the {card_name}.",
    "With the turn of a card, your future is unveiled: {card_name}.",
    "The stars align, and the {card_name} emerges.",
    "The realm of possibilities expands with the presence of the {card_name}.",
    "Enchantment fills the air as the {card_name} is revealed.",
    "Through the deck of cards, destiny guides you to the {card_name}.",
    "The {card_name} appears, illuminating your path forward.",
    "Unlock the mysteries of life with the wisdom of the {card_name}.",
    "A card worth remembering: the legendary {card_name}.",
    "Embrace the power and beauty of the {card_name}."
)
coin_toss_patterns = (
    "You got: {outcome}!",
    "It's a {outcome}!",
    "The coin landed on: {outcome}.",
    "And the result is... {outcome}!",
    "You flipped: {outcome}.",
    "The outcome is: {outcome}.",
    "The coin reveals: {outcome}!",
    "It's {outcome} this time!",
    "The coin settles on: {outcome}.",
    "You called {outcome} and it's correct!",
    "The coin shows: {outcome}.",
    "It's a clear {outcome}!",
    "The verdict is {outcome}.",
    "You are blessed with {outcome}!",
    "The coin whispers: {outcome}.",
    "Behold, {outcome}!",
    "The universe decides: {outcome}.",
    "In the realm of chance, {outcome} shines.",
    "Your destiny is {outcome}!",
    "The fates decree: {outcome}!"
)
dice_patterns = (
    "You rolled a {dice_value}!",
    "You got {dice_value} on the dice!",
    "The dice shows {dice_value}.",
    "Behold! The roll of the day is {dice_value}!",
    "And the winner is... {dice_value}!",
    "You rolled the lucky number {dice_value}!",
    "It's a fortunate day! The dice shows {dice_value}.",
    "The magical dice reveals {dice_value}!",
    "Luck favors you with {dice_value}.",
    "The universe has spoken, presenting you with {dice_value}.",
    "Behold the power of {dice_value}!",
    "Your fate lies in {dice_value}.",
    "A sign from the dice: {dice_value}!",
    "The dice holds the key to your destiny: {dice_value}.",
    "Gather 'round and witness the marvel of {dice_value}!",
    "Luck smiles upon you with {dice_value}.",
    "The roll unveils your future: {dice_value}.",
    "The stars align, and {dice_value} appears.",
    "The realm of possibilities expands with {dice_value}.",
    "Enchantment fills the air as {dice_value} is revealed.",
    "Through the roll of the dice, destiny guides you to {dice_value}.",
    "The dice shows {dice_value}, illuminating your path forward.",
    "Unlock the mysteries of life with the wisdom of {dice_value}.",
    "A roll worth remembering: {dice_value}.",
    "Embrace the luck and excitement of {dice_value}!"
)

number_patterns = (
    "Here are the {number_category} numbers from <b>{start}</b> to <b>{end}</b>:<br>",
    "The {number_category} numbers between <b>{start}</b> and <b>{end}</b> are:<br>",
    "Behold, the magnificent {number_category} numbers from <b>{start}</b> to <b>{end}</b>:<br>",
    "Unlock the secrets of {number_category} numbers between <b>{start}</b> and <b>{end}</b>:<br>",
    "In the realm of numbers, the {number_category} ones from <b>{start}</b> to <b>{end}</b> are:<br>",
    "Witness the beauty of {number_category} numbers as we reveal those from <b>{start}</b> to <b>{end}</b>:<br>",
    "The mysterious sequence of {number_category} numbers between <b>{start}</b> and <b>{end}</b> is:<br>",
    "Prepare to be amazed by the {number_category} numbers we've discovered from <b>{start}</b> to <b>{end}</b>:<br>",
    "Explore the fascinating world of {number_category} numbers from <b>{start}</b> to <b>{end}</b>:<br>",
    "Gather around and marvel at the {number_category} numbers revealed, spanning from <b>{start}</b> to <b>{end}</b>:<br>",
    "Attention! Here are the {number_category} numbers from <b>{start}</b> to <b>{end}</b>:<br>",
    "Calling all number enthusiasts! Feast your eyes on the {number_category} numbers between <b>{start}</b> and <b>{end}</b>:<br>",
    "Ready or not, here come the {number_category} numbers from <b>{start}</b> to <b>{end}</b>:<br>",
    "Prepare yourself for the {number_category} numbers that lie within <b>{start}</b> and <b>{end}</b>:<br>",
    "Let's embark on a journey to discover the {number_category} numbers from <b>{start}</b> to <b>{end}</b>:<br>",
    "Attention, number lovers! The {number_category} numbers from <b>{start}</b> to <b>{end}</b> are:<br>",
    "Get ready to explore the world of {number_category} numbers from <b>{start}</b> to <b>{end}</b>:<br>",
    "Calling all math enthusiasts! Brace yourself for the {number_category} numbers between <b>{start}</b> and <b>{end}</b>:<br>",
    "Unveiling the magnificent {number_category} numbers from <b>{start}</b> to <b>{end}</b>:<br>",
    "Prepare for a mind-boggling experience with the {number_category} numbers from <b>{start}</b> to <b>{end}</b>:<br>",
)

languages =('Afrikaans', 'Amharic', 'Arabic', 'Azerbaijani', 'Belarusian', 'Bulgarian', 'Bengali', 'Bosnian', 'Catalan', 'Cebuano', 'Czech', 'Welsh', 'Danish', 'German', 'Greek', 'English', 'Esperanto', 'Spanish', 'Estonian', 'Basque', 'Persian', 'Finnish', 'French', 'Irish', 'Scottish Gaelic', 'Galician', 'Gujarati', 'Hausa', 'Hawaiian', 'Hindi', 'Hmong', 'Croatian', 'Haitian Creole', 'Hungarian', 'Armenian', 'Indonesian', 'Igbo', 'Icelandic', 'Italian', 'Hebrew', 'Japanese', 'Javanese', 'Georgian', 'Kazakh', 'Khmer', 'Kannada', 'Korean', 'Kurdish', 'Kyrgyz', 'Latin', 'Luxembourgish', 'Lao', 'Lithuanian', 'Latvian', 'Malagasy', 'Maori', 'Macedonian', 'Malayalam', 'Mongolian', 'Marathi', 'Malay', 'Maltese', 'Burmese', 'Nepali', 'Dutch', 'Norwegian', 'Chichewa', 'Punjabi', 'Polish', 'Pashto', 'Portuguese', 'Romanian', 'Russian', 'Kinyarwanda', 'Sindhi', 'Sinhala', 'Slovak', 'Slovenian', 'Samoan', 'Shona', 'Somali', 'Albanian', 'Serbian', 'Sesotho', 'Sundanese', 'Swedish', 'Swahili', 'Tamil', 'Telugu', 'Tajik', 'Thai', 'Filipino', 'Turkish', 'Ukrainian', 'Urdu', 'Uzbek', 'Vietnamese', 'Xhosa', 'Yiddish', 'Yoruba', 'Chinese', 'Chinese (Traditional)', 'Zulu')
