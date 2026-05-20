# Contributing to KingdomConnect

## Code of Conduct

Be respectful, inclusive, and professional in all interactions.

## Getting Started

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes
4. Commit with meaningful messages
5. Push to your fork
6. Open a Pull Request

## Development Guidelines

### Code Style

**Frontend (TypeScript/React):**
- Follow ESLint configuration
- Use Prettier for formatting
- Components in PascalCase
- Functions/hooks in camelCase
- 2-space indentation

**Backend (Laravel/PHP):**
- Follow PSR-12 standard
- Use Laravel conventions
- Add PHPDoc comments
- 4-space indentation

### Commit Messages

```
type(scope): subject

body

footer
```

Types: feat, fix, docs, style, refactor, perf, test, chore

### Commit Message Examples

- `feat(auth): add two-factor authentication`
- `fix(member): resolve member search issue`
- `docs(api): update endpoint documentation`
- `refactor(finance): improve transaction processing`

## Testing

```bash
# Frontend
cd frontend
npm run test
npm run test:watch

# Backend
cd backend
php artisan test
```

## Pull Request Process

1. Update documentation
2. Add tests for new features
3. Ensure all tests pass
4. Request review from maintainers
5. Address feedback
6. Merge when approved

## Branch Naming Convention

- `feature/description` - New features
- `fix/description` - Bug fixes
- `docs/description` - Documentation updates
- `refactor/description` - Code refactoring
- `test/description` - Test additions

## Questions?

Open an issue or contact the team at support@kingdomconnect.com

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
