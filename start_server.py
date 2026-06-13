#!/usr/bin/env python3
"""
Sunday Chatbot - Local Server Launcher
Runs a local web server for the Sunday chatbot
"""

import os
import sys
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading
import time

class SundayHTTPHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add headers to prevent caching
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

def run_server(port=8000):
    """Start the local web server"""
    server_address = ('', port)
    httpd = HTTPServer(server_address, SundayHTTPHandler)
    
    print("=" * 50)
    print("   Sunday Chatbot - Local Server")
    print("=" * 50)
    print()
    print(f"Starting server on http://localhost:{port}")
    print()
    print("Opening Sunday in your browser...")
    print()
    
    # Open browser
    time.sleep(1)
    webbrowser.open(f'http://localhost:{port}/sunday_chatbot.html')
    
    print(f"Server running at http://localhost:{port}")
    print()
    print("Press Ctrl+C to stop the server")
    print()
    print("=" * 50)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\nServer stopped.")
        sys.exit(0)

if __name__ == '__main__':
    port = 8000
    
    # Check if HTML file exists
    if not os.path.exists('sunday_chatbot.html'):
        print("ERROR: sunday_chatbot.html not found!")
        print("Make sure this script is in the same folder as sunday_chatbot.html")
        sys.exit(1)
    
    # Try to use port 8000, fall back to others if needed
    server = HTTPServer(('localhost', port), SundayHTTPHandler)
    for attempt_port in range(port, port + 10):
        try:
            server = HTTPServer(('localhost', attempt_port), SundayHTTPHandler)
            run_server(attempt_port)
            break
        except OSError:
            continue
