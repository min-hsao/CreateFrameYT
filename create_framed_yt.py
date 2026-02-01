#!/usr/bin/env python3
# File: create_frame_yt.py
# Description: Creates a PHP webpage with embedded YouTube video and contact information
import argparse
import re
import string
import random

def generate_random_filename():
    """Generate a random 12-character alphanumeric filename"""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(12)) + '.php'

def extract_youtube_id(url):
    """Extract YouTube video ID from various URL formats"""
    patterns = [
        r'(?:youtube\.com\/watch\?v=|youtu.be\/)([A-Za-z0-9_-]+)',
        r'youtube.com\/embed\/([A-Za-z0-9_-]+)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

def create_php_file(youtube_url, contact_text, filename=None):
    """Create the PHP file with the specified content"""
    if filename is None:
        filename = generate_random_filename()
    elif not filename.endswith('.php'):
        filename += '.php'
    
    video_id = extract_youtube_id(youtube_url)
    if not video_id:
        raise ValueError("Invalid YouTube URL")

    # PHP template
    php_content = '''<!DOCTYPE html>
<?php
// PHP variables for easy updating
$videoId = "{video_id}";
$contactText = <<<EOT
{contact_text}
EOT;
?>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Information</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .container {{
            max-width: 800px;
            margin: 0 auto;
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .video-container {{
            position: relative;
            padding-bottom: 56.25%;
            height: 0;
            margin-bottom: 20px;
        }}
        .video-container iframe {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border: none;
        }}
        .contact-info {{
            text-align: center;
            font-size: 18px;
            line-height: 1.6;
            white-space: pre-line;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="video-container">
            <iframe 
                src="https://www.youtube.com/embed/<?php echo htmlspecialchars($videoId); ?>"
                title="YouTube video"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen>
            </iframe>
        </div>
        <div class="contact-info">
            <?php echo nl2br(htmlspecialchars($contactText)); ?>
        </div>
    </div>
</body>
</html>'''.format(video_id=video_id, contact_text=contact_text)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(php_content)
    
    return filename

def main():
    parser = argparse.ArgumentParser(description='Generate a PHP file with YouTube video and contact information')
    parser.add_argument('--url', help='YouTube video URL')
    parser.add_argument('--text', help='Contact text for the outer frame')
    parser.add_argument('--filename', help='Output PHP filename (optional)')
    parser.add_argument('--random', action='store_true', help='Generate random filename')
    
    args = parser.parse_args()
    
    # Get YouTube URL
    youtube_url = args.url
    while not youtube_url:
        youtube_url = input('Enter YouTube URL: ').strip()
    
    # Get contact text
    contact_text = args.text
    while not contact_text:
        print('Enter contact text (press Enter twice when done):')
        lines = []
        while True:
            line = input()
            if not line and lines and not lines[-1]:
                break
            lines.append(line)
        contact_text = '\n'.join(lines[:-1])
    
    # Determine filename
    filename = None
    if args.random:
        filename = generate_random_filename()
    elif args.filename:
        filename = args.filename
    else:
        use_random = input('Generate random filename? (y/n): ').lower().startswith('y')
        if use_random:
            filename = generate_random_filename()
        else:
            while not filename:
                filename = input('Enter filename (will add .php if needed): ').strip()
    
    try:
        created_file = create_php_file(youtube_url, contact_text, filename)
        print(f'Successfully created: {created_file}')
    except ValueError as e:
        print(f'Error: {e}')
        return 1
    except Exception as e:
        print(f'An error occurred: {e}')
        return 1
    
    return 0

if __name__ == '__main__':
    exit(main())