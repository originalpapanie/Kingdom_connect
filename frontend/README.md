# KingdomConnect Frontend

Modern React/Next.js frontend for the KingdomConnect church management platform.

## Getting Started

### Prerequisites
- Node.js 18+
- npm or yarn

### Installation

1. Install dependencies:
```bash
npm install
```

2. Create a `.env.local` file based on `.env.example`:
```bash
cp .env.example .env.local
```

3. Update the API URL if needed:
```env
NEXT_PUBLIC_API_URL=http://localhost:8000/api
```

### Development

Run the development server:
```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

### Building

Create an optimized production build:
```bash
npm run build
npm start
```

### Code Quality

- **Linting**: `npm run lint`
- **Formatting**: `npm run format`

## Project Structure

```
src/
├── app/              # Next.js app directory
│   ├── layout.tsx    # Root layout
│   ├── page.tsx      # Home page
│   └── globals.css   # Global styles
├── lib/              # Utilities and helpers
│   └── api-client.ts # API client instance
└── components/       # Reusable React components
```

## Technologies

- **Framework**: Next.js 14
- **UI Framework**: React 18
- **Styling**: Tailwind CSS
- **HTTP Client**: Axios
- **Language**: TypeScript
- **Linting**: ESLint
- **Formatting**: Prettier

## Environment Variables

See `.env.example` for all available environment variables.

## Contributing

Please follow the existing code style and run `npm run format` before committing.
