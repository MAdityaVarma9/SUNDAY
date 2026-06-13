# 🤖 Sunday - AI Assistant
## Your Personal Jarvis-like AI Running on Your PC

Welcome! Sunday is a fully functional AI chatbot powered by Claude that runs entirely on your local machine. It features voice input/output, just like Jarvis from Iron Man.

---

## 📦 What You Downloaded

```
sunday_chatbot.html      ← Main chatbot application (open this!)
launch_sunday.bat        ← Windows launcher (double-click to run)
start_server.py          ← Optional: Local web server launcher
SETUP_GUIDE.md          ← Detailed setup instructions
README.md               ← This file
```

---

## ⚡ FASTEST WAY TO GET STARTED

### Windows Users:
1. **Get API Key** (2 minutes):
   - Go to https://console.anthropic.com
   - Sign up or log in
   - Create an API key and copy it

2. **Launch Sunday** (10 seconds):
   - Double-click `launch_sunday.bat`

3. **Configure** (1 minute):
   - Click ⚙️ settings icon
   - Paste your API key
   - Click "Save API Key"

4. **Start Using**:
   - Type a message or click 🎤 to speak
   - Press Enter or click Send
   - Sunday responds with voice and text!

### Mac/Linux Users:
1. Get API key from https://console.anthropic.com
2. Double-click `sunday_chatbot.html` to open in browser
3. Click ⚙️ and paste your API key
4. Start chatting!

---

## 🎤 VOICE FEATURES (Like Jarvis!)

### Voice Input:
- Click the 🎤 button
- Speak your command
- Sunday transcribes and responds

### Voice Output:
- Sunday automatically speaks all responses
- Set your computer volume to hear
- Mute/unmute anytime

**Example Commands:**
```
"Write me a Python script to organize my files"
"Explain quantum computing in simple terms"
"Debug this code for me"
"Tell me a funny story about robots"
"What are the best productivity tips?"
```

---

## 🔑 Getting Your API Key

**Why you need it:**
- API key gives you access to Claude AI
- Your key is stored locally on your PC only
- Never shared with anyone except Anthropic

**How to get it:**
1. Visit https://console.anthropic.com
2. Click "Sign Up" (or "Log In" if you have an account)
3. Create your account
4. Go to "API Keys" section
5. Click "Create API Key"
6. Copy the key (it only shows once!)
7. Paste it in Sunday's settings ⚙️

---

## 💻 Running on Your PC

### Option 1: Direct (Simplest)
- Double-click `sunday_chatbot.html`
- Opens in your default browser
- No installation needed

### Option 2: Windows Batch Launcher
- Double-click `launch_sunday.bat`
- Sunday opens automatically
- Create a shortcut to your desktop for easy access

### Option 3: Local Web Server (Advanced)
For better performance and future improvements:

**Windows:**
```cmd
# Method A: Python
python -m http.server 8000
# Then open: http://localhost:8000/sunday_chatbot.html

# Method B: Use the launcher
python start_server.py
```

**Mac/Linux:**
```bash
python3 -m http.server 8000
# Then open: http://localhost:8000/sunday_chatbot.html
```

---

## 🎯 WHAT SUNDAY CAN DO

✅ **Writing & Content**
- Essays, articles, stories
- Emails, cover letters, resumes
- Poetry, lyrics, creative writing

✅ **Coding & Development**
- Write code in any language
- Debug and fix errors
- Explain programming concepts
- Code reviews and optimization

✅ **Analysis & Research**
- Summarize documents
- Answer questions on any topic
- Compare options and ideas
- Explain complex topics

✅ **Creative Tasks**
- Brainstorming
- Worldbuilding
- Dialogue and character creation
- Idea development

✅ **Learning**
- Tutorial creation
- Concept explanation
- Study guides
- Practice problems

---

## 🛡️ SECURITY & PRIVACY

### Your Data is Safe:
- ✅ API key stored only on YOUR computer
- ✅ Conversations stay in your browser
- ✅ Nothing saved to disk automatically
- ✅ No tracking or data collection
- ✅ No sends to servers except api.anthropic.com

### How to Delete Data:
- **Clear API Key**: Settings ⚙️ → Clear the field → Save
- **Clear Conversation**: Refresh the page (Ctrl+R)
- **Clear Browser Cache**: Browser settings → Clear browsing data

---

## 💰 COSTS

Sunday uses the Anthropic API, which has usage costs:

- **Pricing**: ~$0.003-$0.01 per message (varies by model)
- **Monitor Usage**: Visit https://console.anthropic.com/usage
- **Set Limits**: You can set monthly spending limits in your account
- **Budget Friendly**: Most users spend $5-50/month

---

## 🔧 CUSTOMIZATION

### Change Colors
Open `sunday_chatbot.html` in any text editor, find the CSS section, and change these hex colors:
- `#667eea` - Primary purple
- `#764ba2` - Secondary pink
- `#f59e0b` - Voice button color

### Change the Model
Replace the model name in the API call:
```javascript
model: 'claude-3-5-sonnet-20241022',  // Change this line
```

Available models:
- `claude-opus-4-1` - Most powerful, slower
- `claude-3-5-sonnet-20241022` - Balanced (current)
- `claude-3-haiku-20240307` - Fastest, good for simple tasks

### Change Greeting Message
Search for: "Hi! I'm Sunday" and change the message

---

## 🐛 TROUBLESHOOTING

### "File won't open"
- Right-click → Open With → Choose your browser
- Or drag the file into your browser window
- Try Chrome, Firefox, or Edge

### "API key isn't working"
- Check you copied the full key from console.anthropic.com
- Make sure no extra spaces before/after
- Verify your account is active
- Check you have API credits remaining

### "Voice input not working"
- Chrome/Edge: Works great
- Firefox/Safari: May need to allow microphone permission
- Click "Allow" when browser asks for microphone access
- Check microphone is plugged in and working

### "No voice output"
- Check your speakers/volume isn't muted
- Text-to-speech works in all modern browsers
- Try a different browser if it doesn't work

### "Server won't start"
- Make sure Python is installed: `python --version`
- Check port 8000 isn't in use: Try `python -m http.server 9000`
- Use the direct method instead (just open the HTML file)

---

## 📱 Browser Compatibility

| Browser | Status | Voice Input | Voice Output |
|---------|--------|-------------|--------------|
| Chrome | ✅ Best | ✅ Yes | ✅ Yes |
| Firefox | ✅ Good | ⚠️ Limited | ✅ Yes |
| Safari | ✅ Good | ✅ Yes | ✅ Yes |
| Edge | ✅ Best | ✅ Yes | ✅ Yes |

---

## 🚀 ADVANCED SETUP

### Create Desktop Shortcut (Windows)
1. Right-click `sunday_chatbot.html`
2. Send to → Desktop (create shortcut)
3. Change the shortcut's "Start in" folder to where the HTML is
4. Now double-click the shortcut anytime to launch

### Keyboard Shortcut (Windows - Advanced)
Install AutoHotkey, create file `sunday.ahk`:
```autohotkey
^!s::Run("C:\path\to\sunday_chatbot.html")
```
Now press Ctrl+Alt+S to launch Sunday from anywhere!

### Run on Startup
- Windows: Add `launch_sunday.bat` to Startup folder
- Mac: System Preferences → General → Login Items → Add sunday_chatbot.html
- Linux: Add `xdg-open /path/to/sunday_chatbot.html` to startup script

---

## 📚 USEFUL RESOURCES

- **Anthropic Documentation**: https://docs.anthropic.com
- **API Console**: https://console.anthropic.com
- **API Status**: https://status.anthropic.com
- **Get Help**: https://support.anthropic.com

---

## 🎓 EXAMPLE CONVERSATIONS

### Example 1: Code Help
```
You: "Write a Python function to check if a string is a palindrome"
Sunday: (provides code, explanation, test cases)
```

### Example 2: Creative Writing
```
You: "Help me write the opening paragraph of a sci-fi novel"
Sunday: (writes engaging opening, asks about your story's direction)
```

### Example 3: Learning
```
You: "Explain machine learning to a 10-year-old"
Sunday: (uses simple analogies and examples)
```

### Example 4: Problem Solving
```
You: "I have too many meetings, what can I do?"
Sunday: (suggests strategies, time management tips)
```

---

## 💡 TIPS FOR BEST RESULTS

1. **Be Specific**: "Write me a 500-word article about renewable energy in India" works better than "Write about energy"

2. **Use Context**: "I'm a Python beginner, explain decorators in simple terms"

3. **Ask Follow-ups**: "Tell me more about that" or "Give me an example"

4. **Voice Tips**: Speak clearly, in a quiet room, at normal speed

5. **Check Your Budget**: Monitor usage at console.anthropic.com to avoid surprises

---

## 📝 LICENSE & TERMS

- **This Interface**: Free to use and modify
- **Claude API**: Requires Anthropic account and payment
- **Responsibility**: You're responsible for your API key and usage costs
- **Terms**: Comply with Anthropic's Terms of Service

---

## ✨ FEATURES OVERVIEW

| Feature | Status |
|---------|--------|
| Text Chat | ✅ Full |
| Voice Input | ✅ Full (Chrome/Edge/Safari) |
| Voice Output | ✅ Full |
| Conversation Memory | ✅ Full |
| Multiple Models | ✅ Supported |
| Local Storage | ✅ Yes |
| No Installation | ✅ True |
| Web Server Optional | ✅ Yes |
| Mobile Friendly | ✅ Yes |
| Dark Mode Support | ✅ Auto |

---

## 🤝 NEED HELP?

1. **Check SETUP_GUIDE.md** - Has detailed instructions
2. **Check Anthropic Docs** - https://docs.anthropic.com
3. **Verify API Key** - Make sure it's valid and active
4. **Try Different Browser** - Chrome/Edge usually work best
5. **Restart Everything** - Close browser, clear cache, reopen

---

## 🎉 YOU'RE ALL SET!

You now have a powerful AI assistant running on your PC with voice capabilities!

**Next Steps:**
1. ✅ Download files
2. ✅ Get API key from console.anthropic.com
3. ✅ Open sunday_chatbot.html
4. ✅ Add your API key in settings
5. ✅ Start asking Sunday anything!

Enjoy! 🚀

---

**Questions?** Check the SETUP_GUIDE.md for more detailed instructions on any topic.
