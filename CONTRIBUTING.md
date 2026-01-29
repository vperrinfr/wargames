# Contributing to Global Thermonuclear War

Thank you for your interest in contributing to this project! This document provides guidelines and instructions for contributing.

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [Getting Started](#getting-started)
3. [Development Setup](#development-setup)
4. [How to Contribute](#how-to-contribute)
5. [Coding Standards](#coding-standards)
6. [Testing](#testing)
7. [Documentation](#documentation)
8. [Pull Request Process](#pull-request-process)

## Code of Conduct

This project is educational and meant to promote understanding of Cold War history and the futility of nuclear warfare. Please be respectful and constructive in all interactions.

### Our Standards

- Be respectful and inclusive
- Focus on constructive feedback
- Maintain educational value
- Keep discussions on-topic
- Remember the project's message: "The only winning move is not to play"

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- Basic understanding of Python and terminal applications
- Familiarity with the WarGames (1983) film is helpful but not required

### Fork and Clone

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/wargames.git
   cd wargames
   ```
3. Add upstream remote:
   ```bash
   git remote add upstream https://github.com/vperrinfr/wargames.git
   ```

## Development Setup

### 1. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Development Dependencies

```bash
pip install pytest black flake8 mypy
```

### 4. Verify Installation

```bash
python3 test_game.py
```

## How to Contribute

### Types of Contributions

We welcome various types of contributions:

1. **Bug Fixes** - Fix issues in existing code
2. **Features** - Add new game features or modes
3. **Documentation** - Improve or add documentation
4. **Testing** - Add or improve tests
5. **UI/UX** - Enhance the terminal interface
6. **AI** - Improve WOPR's decision-making
7. **Performance** - Optimize game performance
8. **Localization** - Add language support

### Finding Issues

- Check the [Issues](https://github.com/vperrinfr/wargames/issues) page
- Look for issues labeled `good first issue` or `help wanted`
- Comment on an issue to indicate you're working on it

### Creating Issues

Before creating a new issue:

1. Search existing issues to avoid duplicates
2. Use a clear, descriptive title
3. Provide detailed description
4. Include steps to reproduce (for bugs)
5. Add relevant labels

**Bug Report Template:**
```markdown
**Description:**
Brief description of the bug

**Steps to Reproduce:**
1. Step one
2. Step two
3. ...

**Expected Behavior:**
What should happen

**Actual Behavior:**
What actually happens

**Environment:**
- OS: [e.g., macOS 13.0]
- Python Version: [e.g., 3.10.0]
- Terminal: [e.g., iTerm2]
```

**Feature Request Template:**
```markdown
**Feature Description:**
Clear description of the feature

**Use Case:**
Why this feature would be useful

**Proposed Implementation:**
How you think it could be implemented

**Alternatives Considered:**
Other approaches you've thought about
```

## Coding Standards

### Python Style Guide

We follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) with some modifications:

- Line length: 100 characters (not 79)
- Use double quotes for strings
- Use type hints where appropriate

### Code Formatting

Format your code with Black:

```bash
black src/
```

### Linting

Check code quality with flake8:

```bash
flake8 src/ --max-line-length=100
```

### Type Checking

Use mypy for type checking:

```bash
mypy src/
```

### Naming Conventions

- **Classes**: `PascalCase` (e.g., `GameEngine`, `MissileManager`)
- **Functions/Methods**: `snake_case` (e.g., `launch_missile`, `get_targets`)
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `MAX_MISSILES`, `WOPR_QUOTES`)
- **Private methods**: `_leading_underscore` (e.g., `_check_impacts`)

### Code Structure

```python
"""
Module docstring explaining purpose
"""

# Standard library imports
import sys
import time

# Third-party imports
from colorama import Fore, Style

# Local imports
from src.game_engine import GameEngine


class MyClass:
    """Class docstring"""
    
    def __init__(self, param: str):
        """Constructor docstring"""
        self.param = param
    
    def public_method(self) -> str:
        """Public method docstring"""
        return self._private_method()
    
    def _private_method(self) -> str:
        """Private method docstring"""
        return self.param
```

### Documentation Strings

Use Google-style docstrings:

```python
def launch_missile(missile_type: str, target: Target) -> bool:
    """Launch a missile at a target.
    
    Args:
        missile_type: Type of missile ('ICBM', 'SLBM', 'CRUISE')
        target: Target object to attack
    
    Returns:
        True if launch successful, False otherwise
    
    Raises:
        ValueError: If missile_type is invalid
        RuntimeError: If no missiles remaining
    """
    pass
```

## Testing

### Running Tests

```bash
# Run all tests
python3 test_game.py

# Run with pytest (if available)
pytest tests/
```

### Writing Tests

Create test files in the `tests/` directory:

```python
import unittest
from src.game_logic.target import Target


class TestTarget(unittest.TestCase):
    """Test Target class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.target = Target(
            name="Test City",
            target_type="CITY",
            x=100, y=100,
            population=1000000,
            strategic_value=50,
            defense_level=0.3
        )
    
    def test_take_damage(self):
        """Test damage calculation"""
        result = self.target.take_damage(warheads=5, accuracy=0.9)
        self.assertGreater(result['hits'], 0)
        self.assertGreater(self.target.damage_level, 0)
    
    def tearDown(self):
        """Clean up after tests"""
        pass
```

### Test Coverage

Aim for:
- Core logic: 80%+ coverage
- UI components: 50%+ coverage
- Integration tests for main workflows

## Documentation

### Types of Documentation

1. **Code Comments** - Explain complex logic
2. **Docstrings** - Document all public APIs
3. **README** - Project overview and quick start
4. **Guides** - Detailed usage instructions
5. **API Docs** - Complete API reference

### Documentation Files

- `README.md` - Project overview
- `QUICKSTART.md` - Quick start guide
- `INSTALL.md` - Installation instructions
- `docs/GAMEPLAY.md` - Gameplay guide
- `docs/DESIGN.md` - Technical design
- `docs/API.md` - API reference
- `CONTRIBUTING.md` - This file

### Updating Documentation

When making changes:

1. Update relevant docstrings
2. Update API documentation if needed
3. Update guides if behavior changes
4. Add examples for new features
5. Update README if necessary

## Pull Request Process

### Before Submitting

1. **Update your fork:**
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes:**
   - Write clean, documented code
   - Follow coding standards
   - Add tests for new features
   - Update documentation

4. **Test your changes:**
   ```bash
   python3 test_game.py
   black src/
   flake8 src/
   ```

5. **Commit your changes:**
   ```bash
   git add .
   git commit -m "Add feature: brief description"
   ```
   
   Use clear commit messages:
   - `Add:` for new features
   - `Fix:` for bug fixes
   - `Update:` for improvements
   - `Docs:` for documentation
   - `Test:` for tests
   - `Refactor:` for code refactoring

6. **Push to your fork:**
   ```bash
   git push origin feature/your-feature-name
   ```

### Submitting Pull Request

1. Go to your fork on GitHub
2. Click "New Pull Request"
3. Select your feature branch
4. Fill out the PR template:

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Code refactoring

## Testing
- [ ] Tests pass locally
- [ ] Added new tests
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] No breaking changes
- [ ] Commit messages are clear

## Related Issues
Closes #123
```

### Review Process

1. Maintainers will review your PR
2. Address any requested changes
3. Once approved, PR will be merged
4. Your contribution will be credited

### After Merge

1. Delete your feature branch:
   ```bash
   git branch -d feature/your-feature-name
   git push origin --delete feature/your-feature-name
   ```

2. Update your fork:
   ```bash
   git checkout main
   git pull upstream main
   git push origin main
   ```

## Development Guidelines

### Game Balance

When modifying game mechanics:

- Maintain educational value
- Keep difficulty progression logical
- Test across all difficulty levels
- Ensure AI remains challenging but fair

### UI/UX Principles

- Keep terminal output clean and readable
- Use colors meaningfully (green=normal, yellow=warning, red=alert)
- Maintain 1980s terminal aesthetic
- Ensure compatibility with various terminal sizes

### AI Development

When improving WOPR:

- Maintain personality and quotes from the film
- Keep decision-making transparent
- Balance challenge with playability
- Preserve the "learning" aspect

### Performance

- Keep frame rate at 60 FPS minimum
- Optimize hot paths (game loop, rendering)
- Profile before optimizing
- Don't sacrifice readability for minor gains

## Community

### Communication Channels

- **GitHub Issues** - Bug reports and feature requests
- **Pull Requests** - Code contributions and discussions
- **Discussions** - General questions and ideas

### Getting Help

If you need help:

1. Check existing documentation
2. Search closed issues
3. Ask in GitHub Discussions
4. Create a new issue with `question` label

## Recognition

Contributors will be:

- Listed in the project README
- Credited in release notes
- Acknowledged in commit history

## License

By contributing, you agree that your contributions will be licensed under the same license as the project (see LICENSE file).

---

## Thank You!

Your contributions help preserve the educational message of WarGames and make this project better for everyone.

*"The only winning move is not to play. How about a nice game of chess?"* - WOPR

---

**Questions?** Open an issue with the `question` label or start a discussion.

**Ready to contribute?** Check out the [good first issue](https://github.com/vperrinfr/wargames/labels/good%20first%20issue) label!