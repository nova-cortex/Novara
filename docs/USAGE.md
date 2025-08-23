# Usage Guide

A comprehensive guide on how to use Novara, your ultimate entertainment hub, for discovering and managing anime and movies.

## Table of Contents

- [Overview](#overview)
- [Quick Start](#quick-start)
- [Step-by-Step Setup](#step-by-step-setup)
- [Customization Guide](#customization-guide)
- [Making It Your Default Template](#making-it-your-default-template)
- [Repository Structure](#repository-structure)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)

## Overview

Novara is a comprehensive entertainment hub designed to help you discover, track, and get personalized recommendations for anime and movies. It leverages:

- **Jikan API**: For extensive anime data.
- **OMDb API**: For detailed movie information.
- **Google Gemini API**: For intelligent, personalized recommendations.
- **User-Friendly Interface**: A clean and intuitive command-line interface.
- **Watchlist Management**: Easily add and remove titles from your personal watchlist.

## Quick Start

### Quick Start

To get Novara up and running quickly, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/nova-cortex/novara.git
   cd novara
   ```

2. **Create a virtual environment (recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up API Keys**:
   - Create a `.env` file in the `src` directory.
   - Add your API keys for OMDb, and Google Gemini.
     ```
     OMDB_API_KEY=your_omdb_api_key
     GEMINI_API_KEY=your_gemini_api_key
     ```

5. **Run the application**:
   ```bash
   python src/main.py
   ```

## Step-by-Step Setup

### 1. Initial Setup

After cloning the repository, ensure you have followed the [Quick Start](#quick-start) steps to install dependencies and set up API keys.

### 2. Running the Application

To start Novara, simply run the `main.py` file:

```bash
python src/main.py
```

### 3. Interacting with the Application

Novara provides a command-line interface (CLI) for interaction. Here are some common actions:

- **Search for Anime**: Use the search function to find anime titles.
- **Search for Movies**: Use the search function to find movie titles.
- **View Details**: Select a title to view detailed information.
- **Add to Watchlist**: Add anime or movies to your personal watchlist.
- **View Watchlist**: Display all titles currently in your watchlist.
- **Get Recommendations**: Utilize the Gemini AI integration for personalized suggestions.

### 4. API Key Management

Your API keys are loaded from the `.env` file. If you encounter issues with API calls, ensure:
- The `.env` file is in the `src` directory.
- Your API keys are correctly formatted.
- You have valid API keys for Jikan, OMDb, and Google Gemini.

## Customization Guide

### API Key Configuration

To customize the API keys, edit the `.env` file in the `src` directory. This allows you to use your own API keys for Jikan, OMDb, and Google Gemini.

### Watchlist Management

The watchlist data is stored locally. You can manage your watchlist directly through the application's interface.

### UI Components

Novara's user interface is built using Python's `rich` library. You can modify the files in `src/app/ui_components/` to change the appearance and layout of the application.

## Troubleshooting

### Common Issues

#### API Key Errors
**Problem**: Application fails to fetch data or provide recommendations.
**Solution**:
- Ensure your `.env` file is correctly set up with valid API keys.
- Check for typos in the API key names.
- Verify your internet connection.

#### Missing Dependencies
**Problem**: Application fails to start due to missing modules.
**Solution**:
- Ensure all dependencies are installed: `pip install -r requirements.txt`.
- If using a virtual environment, ensure it is activated.

#### Application Not Starting
**Problem**: Running `python main.py` does nothing or throws an error.
**Solution**:
- Check your Python version (must be 3.8+).
- Review the console for any error messages and address them.
- Ensure `main.py` is in the root directory and you are running the command from there.

## Project Structure

```
Novara/
├── LICENSE
├── pyproject.toml
├── requirements.txt
├── assets/
│   ├── novara-banner.jpg
│   ├── novara-logo.png
│   └── screenshots/
│       └── screenshot.png
├── docs/
│   ├── Blueprint.docx
│   ├── CHANGELOG.md
│   ├── CODE_OF_CONDUCT.md
│   ├── CONTRIBUTING.md
│   ├── README.md
│   ├── SECURITY.md
│   ├── STATUS.md
│   └── USAGE.md
└── src/
    ├── .env
    ├── main.py
    └── app/
        ├── __init__.py
        ├── clients/
        │   ├── __init__.py
        │   ├── googlegemini.py
        │   ├── jikan.py
        │   └── omdb.py
        ├── ui_components/
        │   ├── anime_details.py
        │   ├── cards.py
        │   ├── movie_details.py
        │   ├── styles.py
        │   └── watchlist_display.py
        └── utils/
            ├── api_keys.py
            └── watchlist.py
```

## Best Practices

### API Key Security
- Never commit your `.env` file to version control. It is already listed in `.gitignore`.
- Keep your API keys confidential.

### Code Organization
- Maintain a clear separation of concerns (e.g., clients for API interaction, ui_components for display).
- Use meaningful names for files, functions, and variables.

### Error Handling
- Implement robust error handling for API calls and user input to ensure a smooth experience.

### Documentation
- Keep `README.md` and `USAGE.md` updated with current project status and instructions.
- Use clear, concise language in all documentation.
- Maintain `CHANGELOG.md` for version tracking.

## Troubleshooting

### Common Issues

#### Template Files Not Showing
**Problem**: GitHub templates not appearing in issue/PR creation
**Solution**: Ensure files are in correct paths with proper `.md` extension

#### Images Not Loading
**Problem**: Images in README not displaying
**Solution**: Check image paths and ensure images are committed to repository

#### License Conflicts
**Problem**: License doesn't match project requirements
**Solution**: Replace LICENSE file with appropriate license for your project

#### Documentation Out of Sync
**Problem**: Multiple README files causing confusion
**Solution**: Choose either root README.md or docs/README.md as primary, link to the other

### 📞 Support

- **🐛 Issues**: [Novara Issues](https://github.com/nova-cortex/novara/issues)
- **🔓 Security**: [Novara Security](https://github.com/nova-cortex/novara/security)
- **⛏ Pull Requests**: [Novara Pull Requests](https://github.com/nova-cortex/novara/pulls)
- **📖 Documentation**: [Novara Documentation](https://github.com/nova-cortex/novara/tree/main/docs)

### Contributing

If you'd like to contribute to Novara, please refer to our [Contributing Guide](CONTRIBUTING.md).

---

**Made with ❤️ by Nova Cortex**

*Novara is designed to be your ultimate entertainment hub, powered by intelligent recommendations and a user-friendly interface.*
