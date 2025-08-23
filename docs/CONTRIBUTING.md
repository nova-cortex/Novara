# Contributing to Novara

Thank you for your interest in contributing to Novara! We welcome contributions from everyone and appreciate your help in making this entertainment hub better.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)
- [Issue Guidelines](#issue-guidelines)
- [Community](#community)

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior by opening an issue on our GitHub repository.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following:
- A GitHub account
- Git installed on your local machine
- Basic knowledge of Markdown for documentation
- Understanding of GitHub templates and repository structure

### First Time Setup

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/your-username/novara.git
   cd novara
   ```
3. Add the upstream repository:
   ```bash
   git remote add upstream https://github.com/nova-cortex/novara.git
   ```
4. Review the project structure (refer to `README.md` for the latest structure).

## How to Contribute

### Types of Contributions

We welcome several types of contributions:

- **Bug Fixes**: Identify and fix issues in the application.
- **New Features**: Implement new functionalities for anime, movies, or recommendations.
- **Improvements**: Enhance existing features, UI components, or API integrations.
- **Documentation**: Improve or add to our documentation and guides.
- **Refactoring**: Improve code quality, readability, and maintainability.
- **Testing**: Add unit or integration tests.

### Before You Start

1. Check existing [issues](https://github.com/nova-cortex/novara/issues) and [pull requests](https://github.com/nova-cortex/novara/pulls) to avoid duplicates.
2. For major changes or new features, please open an issue first to discuss your proposed changes.
3. Make sure your contribution aligns with Novara's goal of providing a comprehensive entertainment hub.

## Development Setup

### Local Development

1. **Prerequisites**: Ensure you have Python 3.8+ and `pip` installed.
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up API Keys**:
   - Create a `.env` file in the `src` directory.
   - Add your API keys for Jikan, OMDb, and Google Gemini.
     ```
     JIKAN_API_KEY=your_jikan_api_key
     OMDB_API_KEY=your_omdb_api_key
     GEMINI_API_KEY=your_gemini_api_key
     ```
4. Create a new branch for your feature or improvement:
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/issue-description
   ```
5. Make your changes following our [coding standards](#coding-standards).
6. Test your changes:
   - Run the application locally: `python src/main.py`
   - Verify new features or bug fixes work as expected.
   - Ensure no regressions are introduced.
7. Preview your changes:
   - Interact with the application to ensure UI and functionality are correct.

## Coding Standards

### General Guidelines

- Write clean, readable, and well-commented Python code.
- Follow PEP 8 style guide for Python code.
- Use consistent naming conventions.
- Add docstrings to functions and classes.

### Python Standards

- **Code Style**: Adhere to PEP 8. Use a linter like `flake8` or `pylint`.
- **Type Hinting**: Use type hints for function arguments and return values.
- **Error Handling**: Implement robust error handling using `try-except` blocks.
- **Modularity**: Keep functions and modules focused on a single responsibility.

### Documentation Standards

- **Markdown Guidelines**:
  - Use consistent heading hierarchy.
  - Include code blocks with appropriate language highlighting.
  - Include proper links and references.
- **Docstrings**: Use Google-style docstrings for functions and classes.

### File Organization

- Keep related files in appropriate directories
- Use clear, descriptive file names
- Maintain consistent directory structure
- Include README files in subdirectories when helpful

## Commit Guidelines

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification for commit messages.

### Commit Message Format

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Types

- `feat`: A new feature or enhancement
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc.)
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `perf`: A code change that improves performance
- `test`: Adding missing tests or correcting existing tests
- `chore`: Other changes that don't modify src or test files

### Examples

```
feat(anime): add new anime search functionality

fix(omdb): correct movie data parsing issue

docs: update installation instructions

style: reformat Python files with Black

refactor(clients): consolidate API client initialization
```

## Pull Request Process

### Before Submitting

1. Ensure your branch is up to date with the `main` branch:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. Review your changes thoroughly.
3. Update documentation if necessary.
4. Ensure all tests pass and the application runs without errors.

### Submitting Your Pull Request

1. Push your branch to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

2. Create a pull request from your fork to the `main` branch of the Novara repository.

3. Fill out the pull request template completely.

4. Link any related issues using keywords (e.g., "Closes #123").

### Pull Request Template

When creating a pull request, please include:

- **Description**: Clear description of what changes you made
- **Motivation**: Why are these changes needed?
- **Type of Change**: Bug fix, new feature, documentation, etc.
- **Testing**: How did you test your changes?
- **Screenshots**: If applicable, add screenshots of visual changes
- **Breaking Changes**: List any breaking changes
- **Checklist**: Complete the provided checklist

### Review Process

1. All pull requests require at least one review from a maintainer
2. Address any feedback or requested changes promptly
3. Once approved, a maintainer will merge your pull request
4. Your contribution will be included in the next release

## Issue Guidelines

### Before Creating an Issue

1. Search existing [issues](https://github.com/nova-cortex/novara/issues) to avoid duplicates.
2. Check if the issue might be related to your specific use case.
3. Gather relevant information (screenshots, error logs, steps to reproduce).

### Bug Reports

When reporting a bug, please include:

- **Bug Description**: Clear and concise description of the bug.
- **Steps to Reproduce**: Detailed steps to reproduce the issue.
- **Expected Behavior**: What you expected to happen.
- **Actual Behavior**: What actually happened.
- **Affected Component(s)**: Which part of the application is affected (e.g., `src/app/clients/jikan.py`, `src/app/ui_components/anime_details.py`).
- **Environment**: Your operating system, Python version, and any other relevant environment details.
- **Additional Context**: Screenshots, error messages, or logs.

### Feature Requests

When requesting a feature, please include:

- **Feature Description**: Clear description of the proposed feature.
- **Use Case**: Why is this feature needed and how will it benefit users?
- **Proposed Solution**: Your ideas for implementation or how it might work.
- **Examples**: Examples from other applications if applicable.
- **Additional Context**: Any other relevant information.

## Community

### Getting Help

If you need help or have questions, don't hesitate to:
- Open an [issue](https://github.com/nova-cortex/novara/issues) with the "question" label.
- Reach out to the maintainers via GitHub.

### Recognition

We appreciate all contributions and maintain a contributors list to recognize everyone who has helped improve this project. All contributors will be acknowledged in our documentation.

### License

By contributing to this project, you agree that your contributions will be licensed under the MIT License, the same license as the project. See [LICENSE](../LICENSE) for details.

---

## Quick Reference

### Common Commands

```bash
# Setup
git clone https://github.com/your-username/novara.git
cd novara
git remote add upstream https://github.com/nova-cortex/novara.git

# Development
git checkout -b feature/new-feature
# Make your changes
pip install -r requirements.txt # if new dependencies
python src/main.py # to run and test
git add .
git commit -m "feat: add new feature X"
git push origin feature/new-feature
```

### 📞 Support

- **🐛 Issues**: [Novara Issues](https://github.com/nova-cortex/novara/issues)
- **🔓 Security**: [Novara Security](https://github.com/nova-cortex/novara/security)
- **⛏ Pull Requests**: [Novara Pull Requests](https://github.com/nova-cortex/novara/pulls)
- **📖 Documentation**: [Novara Documentation](https://github.com/nova-cortex/novara/tree/main/docs)

### Need Help?

If you're new to contributing or need assistance:
- Review our existing code for examples.
- Check the project structure and follow existing patterns.
- Don't hesitate to ask questions in issues.
- Start with small improvements to get familiar with the project.

Thank you for contributing to Novara! Together, we're building a better entertainment hub. 🎉
