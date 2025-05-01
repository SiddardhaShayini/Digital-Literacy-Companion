def get_responses():
    """
    Returns a dictionary of predefined responses for common digital literacy questions.
    Each response is associated with keywords and patterns for matching.
    """
    responses = {
        "Internet Basics": {
            "wifi connect how to connect wifi internet": """
            # Connecting to WiFi
            
            Here's how to connect to a WiFi network:
            
            1. **Find your WiFi settings**:
               - On a smartphone: Look for "Settings" then "WiFi" or "Connections"
               - On a computer: Click the WiFi icon in the corner of your screen
            
            2. **Turn WiFi ON** if it's not already on
            
            3. **Choose your network** from the list - look for your home network name
            
            4. **Enter the password** when prompted (this is usually on the back of your router)
            
            5. **Tap "Connect"** and wait for the connection to complete
            
            You'll know you're connected when you see a WiFi symbol at the top of your screen!
            
            Need help finding your WiFi password? It's usually printed on a sticker on your internet router.
            """,
            
            "browser what is web browser internet explorer chrome firefox safari": """
            # What is a Web Browser?
            
            A web browser is the program you use to access websites and explore the internet. Think of it as your car for traveling on the information superhighway!
            
            **Common web browsers include**:
            - Google Chrome (has a colorful circle icon)
            - Safari (compass icon - comes pre-installed on Apple devices)
            - Microsoft Edge (blue "e" icon - comes with Windows)
            - Firefox (orange fox icon)
            
            **What browsers do**:
            - Let you visit websites by typing addresses or searching
            - Store your favorite sites as "bookmarks"
            - Remember your browsing history
            - Fill in forms automatically
            
            **To use a browser**:
            1. Click or tap the browser icon on your device
            2. Type a website address in the bar at the top (like "google.com") or a search term
            3. Press Enter to go to the site or see search results
            
            Let me know if you'd like to learn how to do something specific with your browser!
            """,
            
            "search effectively online google how to find information": """
            # How to Search Effectively Online
            
            Searching effectively online is like being a detective - using the right clues to find exactly what you need!
            
            **Simple search tips**:
            
            1. **Be specific** - Instead of "cake recipe," try "easy chocolate cake recipe no eggs"
            
            2. **Use quotation marks** - Put exact phrases in quotes like "how to fix leaky faucet"
            
            3. **Try different words** - If you don't find what you need, try synonyms (like "repair" instead of "fix")
            
            4. **Look at more than just the first result** - Sometimes the best answer is further down
            
            5. **Use search filters** - Most search engines let you filter by date, image, news, etc. Look for these options
            
            6. **Check the source** - Make sure information comes from trustworthy websites
            
            7. **Refine your search** - If you get too many results, add more specific details
            
            Remember: The more specific your search terms, the better your results will be!
            """
        },
        
        "Online Safety & Privacy": {
            "password strong create secure how to make good password": """
            # Creating Strong Passwords
            
            Creating strong passwords is one of the most important steps for staying safe online.
            
            **How to create a strong password**:
            
            1. **Make it long** - At least 12 characters is good
            
            2. **Mix it up** - Use a combination of:
               - Uppercase letters (ABC)
               - Lowercase letters (abc)
               - Numbers (123)
               - Special characters (@#$%)
            
            3. **Avoid obvious information** like:
               - Your name or family names
               - Birthdays or anniversary dates
               - Common words like "password" or "qwerty"
               - Sequential numbers like "12345"
            
            4. **Try using a passphrase** - A sentence or phrase you'll remember, like "MyDogLovesTreatsIn2024!"
            
            5. **Use different passwords** for different accounts - especially for important ones like banking
            
            **Tip**: Consider using a password manager app to help you create and remember strong passwords.
            
            Remember: Never share your passwords with anyone, and don't write them down where others might find them!
            """,
            
            "phishing recognize scam email fake how to identify": """
            # Recognizing Phishing Attempts
            
            Phishing is when someone tries to trick you into sharing personal information by pretending to be a trusted organization. Here's how to spot these scams:
            
            **Warning signs of phishing**:
            
            1. **Suspicious sender address** - Look carefully at the email address (not just the display name). 
               Example: "amazon-support@mail247.com" instead of a real "amazon.com" address
            
            2. **Urgent or threatening language** - "Your account will be closed unless you act now!"
            
            3. **Grammar and spelling errors** - Legitimate companies proofread their messages
            
            4. **Suspicious links** - Hover over links without clicking to see where they really go
            
            5. **Requests for personal information** - Legitimate companies rarely ask for passwords or banking details via email
            
            6. **Generic greeting** - "Dear Customer" instead of your actual name
            
            7. **Too good to be true offers** - "You've won a prize!" when you never entered a contest
            
            **What to do**:
            - Never click suspicious links
            - Don't download unexpected attachments
            - When in doubt, go directly to the company's website by typing the address yourself
            - Report phishing emails to your email provider
            
            If you're ever unsure about an email, it's better to be safe and delete it!
            """
        },
        
        "Social Media": {
            "facebook account create set up how to start": """
            # Setting Up a Facebook Account
            
            Creating a Facebook account is a great way to connect with family and friends. Here's a simple guide:
            
            **Step-by-step instructions**:
            
            1. **Go to Facebook's website** - Open your web browser and go to www.facebook.com
            
            2. **Fill in the sign-up form** with:
               - Your name
               - Email address or mobile phone number
               - Password (make it strong!)
               - Birthday
               - Gender
            
            3. **Click "Sign Up"**
            
            4. **Verify your account** - Facebook will send a code to your email or phone
            
            5. **Find friends** - Facebook will suggest people you might know
            
            6. **Add a profile picture** - This helps friends recognize you
            
            7. **Fill in your profile** - Add information you're comfortable sharing
            
            **Important privacy tips**:
            
            - Review your privacy settings right away (click the down arrow in the top right, then "Settings & Privacy")
            - Consider who can see your posts (Public, Friends, or Only Me)
            - Be selective about friend requests - only accept people you know
            
            Would you like me to explain any specific part of this process in more detail?
            """,
            
            "privacy settings social media facebook instagram protect": """
            # Privacy Settings on Social Media
            
            Controlling your privacy on social media helps you share with only the people you want to. Here's how to check your settings on popular platforms:
            
            **Facebook Privacy Settings**:
            1. Click the down arrow in the top right corner
            2. Select "Settings & Privacy" then "Privacy Shortcuts"
            3. Review "Who can see what you share" and "How people can find you"
            4. Adjust who can see your posts, friend list, and profile information
            
            **Instagram Privacy Settings**:
            1. Go to your profile and tap the three lines (menu)
            2. Select "Settings and privacy"
            3. Consider setting your account to private (only approved followers can see posts)
            4. Check "Comments" and "Tags" settings to control who can interact with you
            
            **Important settings to check on any platform**:
            
            - **Post privacy** - Who can see what you share (Public, Friends, Only Me)
            - **Profile information** - What personal details are visible
            - **Friend/follow requests** - Who can send you requests
            - **Location sharing** - Whether your location is shown with posts
            - **Search visibility** - How people can find you (email, phone, etc.)
            
            Remember to review these settings regularly, as platforms sometimes update their privacy options!
            """
        },
        
        "Email & Communication": {
            "email account setup create gmail yahoo how to": """
            # Setting Up an Email Account
            
            Having an email account is essential for many online activities. Gmail (from Google) is one of the most popular and easy-to-use options. Here's how to set one up:
            
            **Setting up a Gmail account**:
            
            1. **Go to gmail.com** in your web browser
            
            2. **Click "Create account"**
            
            3. **Fill in the form** with:
               - Your first and last name
               - Username (this will be your email address: username@gmail.com)
               - Password (make it strong and secure!)
               - Phone number (for account recovery)
            
            4. **Verify your information** and agree to Google's terms
            
            5. **Complete the verification process** (usually via text or phone call)
            
            6. **You're done!** Your new email address is username@gmail.com
            
            **First steps with your new email**:
            - Take the tour if offered
            - Add a profile picture if you wish
            - Practice sending an email to yourself
            - Add contacts of family and friends
            
            **Tips for choosing a good email address**:
            - Professional (like firstname.lastname@gmail.com)
            - Easy to remember and spell
            - Avoid including sensitive information like birthyear
            
            Would you like instructions for a different email provider or more details about using Gmail?
            """,
            
            "send receive email attach file attachment how to": """
            # How to Send and Receive Emails
            
            **Sending an email**:
            
            1. **Open your email app or website** (Gmail, Yahoo, Outlook, etc.)
            
            2. **Click "Compose" or "New Email"** (usually a button with a plus sign or pen icon)
            
            3. **Fill in these fields**:
               - To: Enter the recipient's email address
               - Subject: Write a brief description of what the email is about
               - Body: Type your message in the main area
            
            4. **Click "Send"** when you're ready
            
            **Receiving and reading emails**:
            
            1. **Check your inbox** - New emails appear here
            
            2. **Unread emails** are usually in bold or marked with a dot
            
            3. **Click on an email** to open and read it
            
            4. **Reply options**:
               - Reply: Respond to only the sender
               - Reply All: Respond to everyone in the conversation
               - Forward: Send the email to someone new
            
            **Handling attachments**:
            
            - **To send an attachment**: Look for a paper clip or attachment icon, click it, select your file
            
            - **To open a received attachment**: Click on the attachment icon in the email
            
            **Email etiquette tips**:
            - Use a clear subject line
            - Keep messages concise
            - Be polite and professional
            - Double-check recipient addresses before sending
            
            Is there anything specific about email you'd like to know more about?
            """
        },
        
        "Smartphones & Apps": {
            "app download install how to get apps store": """
            # How to Download and Install Apps
            
            Apps can make your smartphone or tablet more useful and fun. Here's how to find and install them:
            
            **For iPhone or iPad (Apple devices)**:
            
            1. Locate the **App Store** icon (blue icon with an "A")
            2. Tap to open the App Store
            3. Use the **Search** tab (magnifying glass) to find a specific app
            4. Or browse categories in the **Apps** or **Games** tabs
            5. Tap the app you want
            6. Tap **Get** (free apps) or the price (paid apps)
            7. Authenticate with Face ID, Touch ID, or your Apple password
            8. The app will download and install automatically
            
            **For Android devices (Samsung, Google, etc.)**:
            
            1. Find the **Google Play Store** icon (colorful triangle)
            2. Tap to open the Play Store
            3. Search for an app using the search bar at the top
            4. Or browse categories by tapping "Apps" or "Games"
            5. Tap the app you're interested in
            6. Tap **Install** (free) or the price (paid apps)
            7. Accept permissions if asked
            8. The app will download and install automatically
            
            **Important tips**:
            
            - Only download apps from the official App Store or Google Play Store
            - Check app ratings and reviews before downloading
            - Be cautious about apps requesting excessive permissions
            - Consider using wifi rather than cellular data for large downloads
            
            Once installed, the app icon will appear on your home screen or in your app library!
            """,
            
            "app permissions understand privacy security what are": """
            # Understanding App Permissions
            
            When you install or use apps, they often ask for "permissions" to access different parts of your device. Understanding these helps protect your privacy.
            
            **What are app permissions?**
            Permissions are requests from apps to access specific features or information on your device, such as:
            
            - **Camera** - To take photos or video
            - **Microphone** - To record audio or make calls
            - **Location** - To know where you are
            - **Contacts** - To access your address book
            - **Storage** - To save or access files
            - **Phone** - To make/manage calls or access your phone number
            
            **How to make smart permission decisions**:
            
            1. **Question why** - Does the app really need this permission to function?
               (Example: A map app needs location, but a simple game shouldn't)
            
            2. **Be selective** - Only grant permissions that make sense
               (Example: A flashlight app doesn't need your contacts)
            
            3. **Choose "Only while using"** for location when possible
            
            4. **Review periodically** - Check and update app permissions in your device settings
            
            **How to check app permissions**:
            
            On iPhone:
            - Go to Settings > Privacy
            - Select each category to see which apps have permission
            
            On Android:
            - Go to Settings > Apps
            - Select an app, then "Permissions"
            
            Remember: You can always revoke permissions later if you change your mind!
            """
        },
        
        "Online Entertainment": {
            "streaming service netflix setup how to use watch": """
            # Setting Up Netflix or Other Streaming Services
            
            Streaming services let you watch movies and TV shows anytime. Here's how to get started with Netflix (similar steps apply to other services like Hulu or Disney+):
            
            **Setting up Netflix**:
            
            1. **Sign up**:
               - Go to netflix.com or download the Netflix app
               - Click "Sign Up" or "Get Started"
               - Choose a plan (Basic, Standard, or Premium)
               - Create an account with your email and a password
               - Enter payment information
            
            2. **Set up your profile**:
               - Create profiles for different family members
               - Each profile keeps separate recommendations
            
            3. **Start watching**:
               - Search for specific shows/movies, or
               - Browse categories like "Comedies" or "Dramas"
               - Click on a title to read more about it
               - Click "Play" to start watching
            
            **Watching on different devices**:
            
            - **TV**: Use a smart TV with Netflix app or devices like Roku, Amazon Fire Stick, or Chromecast
            - **Computer**: Visit netflix.com in your web browser
            - **Phone/Tablet**: Download the Netflix app
            
            **Helpful features**:
            
            - Add shows to "My List" to watch later
            - Resume watching where you left off
            - Set parental controls for kids' profiles
            
            **Tips for better streaming**:
            - Use a strong WiFi connection
            - Close other apps/browsers while streaming
            - Adjust video quality settings if your internet is slow
            
            Would you like more specific information about using Netflix or setting up a different streaming service?
            """,
            
            "podcast audiobook find listen how to": """
            # Finding Podcasts and Audiobooks
            
            Podcasts and audiobooks are wonderful ways to enjoy stories and information - like radio shows you can listen to whenever you want!
            
            **Finding and listening to podcasts**:
            
            1. **Using a smartphone or tablet**:
               - iPhone/iPad: Use the pre-installed "Podcasts" app
               - Android: Download "Google Podcasts" or "Spotify" from the Play Store
            
            2. **Find podcasts**:
               - Tap "Browse" or "Discover" to see popular shows
               - Use the search function to find topics you're interested in
               - Look at "Top Charts" for popular options
            
            3. **Subscribe to podcasts you like** - You'll automatically get new episodes
            
            4. **Download episodes** for offline listening (great for travel!)
            
            **Finding and listening to audiobooks**:
            
            1. **Popular audiobook services**:
               - Audible (subscription service with largest selection)
               - Libby/OverDrive (free with your library card!)
               - Apple Books or Google Play Books
            
            2. **Using Libby (free library audiobooks)**:
               - Download the Libby app
               - Enter your library card information
               - Browse or search for audiobooks
               - Borrow and download to your device
            
            **Listening tips**:
            
            - Use headphones for better sound quality
            - Adjust playback speed if narration is too fast or slow
            - Set sleep timers for bedtime listening
            
            **Podcast recommendations for beginners**:
            - "This American Life" (interesting stories)
            - "How Stuff Works" (educational)
            - "The Daily" (news)
            
            Would you like recommendations for specific types of podcasts or help with a particular audiobook service?
            """
        },
        
        "Digital Health & Wellbeing": {
            "screen time limit reduce addiction how to": """
            # Setting Screen Time Limits
            
            Too much screen time can affect sleep, physical health, and well-being. Here's how to find a healthy balance:
            
            **Setting up screen time controls**:
            
            **On iPhone/iPad**:
            1. Go to Settings > Screen Time
            2. Tap "Turn On Screen Time"
            3. Choose "This is My Device" or "This is My Child's Device"
            4. Set "Downtime" (scheduled time away from screen)
            5. Set "App Limits" for specific app categories
            
            **On Android**:
            1. Go to Settings > Digital Wellbeing
            2. View your app usage
            3. Set timers for apps using "App Timers"
            4. Use "Focus Mode" to pause distracting apps
            5. Set up "Bedtime Mode" to reduce interruptions at night
            
            **Practical tips for reducing screen time**:
            
            - **Create tech-free zones** - No devices at the dinner table or bedroom
            - **Use the 20-20-20 rule** - Every 20 minutes, look at something 20 feet away for 20 seconds
            - **Set boundaries** - Choose specific times to check email or social media
            - **Find alternatives** - Replace some screen time with reading, walking, or hobbies
            - **Turn off notifications** - Reduce the urge to constantly check devices
            
            **Signs you might need a digital break**:
            - Feeling anxious when away from your device
            - Difficulty concentrating on other activities
            - Disrupted sleep after using screens
            - Physical symptoms like eye strain or headaches
            
            Remember: Technology should enhance your life, not control it!
            """,
            
            "telehealth appointment virtual doctor visit how to": """
            # Telehealth Appointments
            
            Telehealth lets you meet with healthcare providers through video calls. Here's how to prepare for a successful virtual appointment:
            
            **Before your telehealth appointment**:
            
            1. **Confirm technology requirements**:
               - Which platform will be used (Zoom, FaceTime, special healthcare app)
               - Test your camera and microphone ahead of time
               - Ensure you have a strong internet connection
            
            2. **Prepare information**:
               - Make a list of your symptoms or questions
               - Have your medications nearby to show the doctor
               - Write down your recent temperature, blood pressure, or other measurements
               - Have your insurance card ready
            
            3. **Set up your space**:
               - Find a quiet, private area with good lighting
               - Position your camera at eye level
               - Ensure the area is well-lit so the doctor can see you clearly
            
            **During the appointment**:
            
            1. Join the call 5-10 minutes early
            2. Speak clearly and look at the camera
            3. Have paper and pen ready to take notes
            4. Ask for clarification if you don't understand something
            
            **After the appointment**:
            
            1. Review your notes and any instructions
            2. Set up any follow-up appointments
            3. Order any prescribed medications
            
            **Tips for a successful telehealth visit**:
            - Wear loose clothing if the doctor needs to see a body part
            - Have someone help you if you need assistance holding the camera
            - Write down instructions for any prescribed treatments
            
            Telehealth is convenient, but always go in person for emergencies or if you feel your condition requires hands-on examination.
            """
        },
        
        "Fallback": {
            "default fallback unknown": "I'm not sure I understand. Could you try rephrasing your question? I'm here to help with topics like internet basics, online safety, social media, email, smartphones, and other digital topics."
        }
    }
    
    return responses
