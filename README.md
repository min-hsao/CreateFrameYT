# Create Frame YT

A Python CLI tool to generate PHP webpages with embedded YouTube videos and contact information. Useful for creating simple video landing pages.

## Features

- 📺 Embed YouTube videos with responsive iframe
- 📝 Add custom contact text
- 🎲 Random filename generation option
- 🎨 Clean, responsive design
- 🔒 PHP security (htmlspecialchars)

## Requirements

- Python 3.6+
- Web server with PHP support (for hosting output)

## Installation

No dependencies required - uses Python standard library.

## Usage

```bash
# Interactive mode
python create_framed_yt.py

# With arguments
python create_framed_yt.py --url "https://youtube.com/watch?v=..." --text "Contact: email@example.com"

# Random filename
python create_framed_yt.py --url "https://youtube.com/watch?v=..." --text "My contact" --random

# Custom filename
python create_framed_yt.py --url "https://youtube.com/watch?v=..." --text "Contact info" --filename mypage
```

## Arguments

| Argument | Description |
|----------|-------------|
| `--url` | YouTube video URL |
| `--text` | Contact text to display |
| `--filename` | Output PHP filename |
| `--random` | Generate random 12-char filename |

## Output

Creates a PHP file with:
- Responsive YouTube embed
- Contact information section
- Mobile-friendly CSS
- Clean, minimal design

## Supported URL Formats

- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- `https://youtube.com/embed/VIDEO_ID`

## License

MIT License - see [LICENSE](LICENSE) for details.
