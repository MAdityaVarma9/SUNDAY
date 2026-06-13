# Sunday Chatbot - Local Setup Guide
## How to Run Sunday Like Jarvis on Your PC

---

## QUICK START (5 minutes)

### Step 1: Download the File
1. Download `sunday_chatbot.html` to your computer
2. Save it in a folder you can easily access (e.g., Desktop or Documents)

### Step 2: Get an API Key
1. Go to https://console.anthropic.com
2. Sign up or log in with your Anthropic account
3. Create an API key
4. Copy your API key (you'll need it in the next step)

### Step 3: Open and Configure
1. Open `sunday_chatbot.html` in your web browser (double-click the file)
2. Click the ⚙️ settings icon in the top right
3. Paste your API key in the "API Key" field
4. Click "Save API Key"
5. Start chatting!

---

## FEATURES

✅ **Full Claude Capabilities** - Writing, coding, analysis, creative tasks, and more
✅ **Voice Input** - Click 🎤 to speak instead of typing (Chrome, Edge, Safari)
✅ **Voice Output** - Sunday speaks responses back to you (like Jarvis!)
✅ **Local Storage** - Your API key is stored locally on your PC, never sent elsewhere
✅ **Conversation Memory** - Sunday remembers context across messages
✅ **Beautiful UI** - Modern, responsive interface
✅ **No Installation Required** - Just open the HTML file!

---

## MAKING IT JARVIS-LIKE

### 1. Voice Activation (Recommended)
- Click the 🎤 button to speak commands
- Sunday will listen, transcribe your speech, and respond
- Sunday's response will be spoken aloud automatically
- This gives you that Jarvis hands-free experience!

### 2. Create Desktop Shortcut (Windows)
To make it easily accessible like an app:

**Method A: Shortcut with Custom Icon**
1. Right-click on `sunday_chatbot.html`
2. Send to → Desktop (create shortcut)
3. Right-click the shortcut → Properties
4. Change "Start in" to the folder containing the HTML file
5. Click "Advanced" and check "Run as Administrator" (optional)
6. Click OK

**Method B: Batch File Launcher**
1. Create a new text file in the same folder as sunday_chatbot.html
2. Add this content:
```
@echo off
start sunday_chatbot.html
```
3. Save as `launch_sunday.bat`
4. Now you can double-click the .bat file to launch Sunday!

### 3. Keyboard Shortcut (Advanced - Windows)
Using AutoHotkey to launch with a custom hotkey:

1. Download AutoHotkey from https://www.autohotkey.com
2. Create a new file called `sunday_launcher.ahk`
3. Add this content (replace path with your actual path):
```autohotkey
; Press Ctrl+Alt+S to launch Sunday
^!s::
{
    Run("C:\Users\YourUsername\Desktop\sunday_chatbot.html")
}
```
4. Save and run the .ahk file
5. Now press Ctrl+Alt+S anytime to launch Sunday!

### 4. Mac Setup
1. Open Finder, navigate to the folder with sunday_chatbot.html
2. Right-click the file → Open With → Safari (or your preferred browser)
3. Create a desktop shortcut by dragging the file to Desktop

### 5. Linux Setup
```bash
# Navigate to the folder containing sunday_chatbot.html
cd ~/path/to/folder

# Run with default browser
xdg-open sunday_chatbot.html

# Or use a simple server (more reliable)
python3 -m http.server 8000
# Then visit http://localhost:8000/sunday_chatbot.html
```

---

## USING SUNDAY LIKE JARVIS

### Voice Commands Example
**You:** 🎤 "Write me a funny poem about cats"
**Sunday:** (speaks response aloud)

**You:** 🎤 "Debug this Python code for me"
**Sunday:** (analyzes and explains, speaks the solution)

**You:** 🎤 "What's the weather like and what should I wear?"
**Sunday:** (notes: Sunday can't check real-time weather, but you can tell it the temperature)

### Text Mode
Simply type your commands and press Enter. Perfect for:
- Code writing and debugging
- Content creation
- Research and analysis
- Problem solving
- Creative brainstorming

---

## TROUBLESHOOTING

### "API Key not working"
- Check that you've copied the full API key from console.anthropic.com
- Make sure you don't have extra spaces before/after the key
- Verify you have an active Anthropic account
- Check that you have API credits available

### "Voice input not working"
- Voice is only supported in Chrome, Edge, and Safari
- Your browser must have microphone access
- Click "Allow" when your browser asks for microphone permission
- Make sure your microphone is working

### "Voice output not working"
- Check if text-to-speech is enabled in your browser
- Text-to-speech works in all modern browsers
- Volume should not be muted
- Try a different browser if it doesn't work

### "HTML file won't open"
- Right-click the file → Open With → Choose your browser
- Or drag the file into your browser window
- Try a different browser (Chrome, Firefox, Edge recommended)

---

## SECURITY & PRIVACY

🔐 **Your API Key is Safe:**
- Your API key is stored only in your browser's local storage
- It never leaves your computer
- It's never sent to any server except api.anthropic.com
- Clear browser data to delete it anytime

🔐 **Your Conversations:**
- Stored only in your browser while the chat is open
- Not saved to your disk unless you copy-paste them
- Each browser session is independent
- No tracking or data collection

---

## ADVANCED: RUN ON A LOCAL SERVER

For a more stable experience, you can run a local web server:

### Using Python (Windows/Mac/Linux)
1. Open Command Prompt/Terminal in the folder with sunday_chatbot.html
2. Run one of these commands:

**Python 3:**
```bash
python -m http.server 8000
```

**Python 2:**
```bash
python -m SimpleHTTPServer 8000
```

3. Open your browser and go to: `http://localhost:8000/sunday_chatbot.html`

### Using Node.js (Windows/Mac/Linux)
1. Install Node.js from https://nodejs.org
2. Open Command Prompt/Terminal in the folder with sunday_chatbot.html
3. Run:
```bash
npx http-server
```
4. Visit the URL shown in the terminal

---

## CUSTOMIZATION

### Change Sunday's Appearance
Open sunday_chatbot.html in a text editor and find the CSS section. You can modify:

- **Colors:** Change the gradient colors (currently purple #667eea and pink #764ba2)
- **Font:** Change the font family
- **Greeting message:** Search for "Hi! I'm Sunday" and change it
- **Avatar character:** Change the "S" to something else

### Change Model
The chatbot uses `claude-3-5-sonnet-20241022`. You can change it to:
- `claude-opus-4-1` (most powerful, slower)
- `claude-3-sonnet-20240229` (faster, slightly less capable)
- `claude-3-haiku-20240307` (fastest, for quick tasks)

Find this line and replace the model name:
```javascript
model: 'claude-3-5-sonnet-20241022',
```

---

## TIPS FOR BEST EXPERIENCE

1. **Voice Quality:** Speak clearly when using voice input for best results
2. **API Costs:** Each message costs a small amount. Monitor your usage at console.anthropic.com
3. **Browser:** Chrome and Edge have the best speech recognition
4. **Local Server:** If you use it frequently, set up a local server for faster loading
5. **Bookmarks:** Bookmark the localhost URL for quick access

---

## WHAT SUNDAY CAN DO

✅ Answer questions and explain concepts
✅ Write code in any programming language
✅ Debug and fix existing code
✅ Write essays, stories, and creative content
✅ Analyze documents and summarize text
✅ Brainstorm ideas and plan projects
✅ Translate between languages
✅ Solve math problems
✅ And much more!

---

## GET HELP

- **Anthropic API Documentation:** https://docs.anthropic.com
- **API Key Issues:** https://support.anthropic.com
- **Report Issues:** https://github.com/anthropics/anthropic-sdk-python/issues

---

## LICENSE

This chatbot interface is provided as-is. You're responsible for:
- Obtaining and managing your own Anthropic API key
- Monitoring your API usage and costs
- Complying with Anthropic's Terms of Service

---

Enjoy using Sunday! 🚀

Questions? Need help? Check the Anthropic docs or create a fresh API key if you're having issues.
