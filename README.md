# KingdomConnect

A production-ready, enterprise-grade Multi-Branch Church Management SaaS Web Application.

## Overview

KingdomConnect is a comprehensive church management platform designed for multi-branch organizations with centralized headquarters oversight. The platform provides tools for:

- Headquarters oversight and branch management
- Finance management (tithes, offerings, donations, payroll)
- Asset/property management
- Member management and pastoral care
- Attendance tracking and event management
- Communication systems (SMS, Email, WhatsApp)
- AI-powered insights and automation
- Real-time notifications and updates

## Tech Stack

### Frontend
- Next.js 15+
- React 19+
- TypeScript
- Tailwind CSS
- shadcn/ui
- Redux Toolkit
- React Query / TanStack Query
- React Hook Form + Zod validation
- Recharts for analytics
- PWA support

### Backend
- Laravel 12 API
- REST API + GraphQL support
- JWT authentication
- RBAC (Role-Based Access Control)
- Queue system
- Event-driven architecture
- Laravel Reverb for real-time

### Infrastructure
- PostgreSQL
- Redis caching
- AWS S3 compatible storage
- Docker & Docker Compose
- CI/CD ready

## Getting Started

### With Docker (Recommended)
```bash
git clone https://github.com/originalpapanie/Kingdom_connect.git
cd Kingdom_connect
cp .env.example .env
docker-compose up -d
```

### Manual Setup
See [INSTALLATION.md](./docs/INSTALLATION.md)

## Project Structure

```
Kingdom_connect/
├── frontend/              # Next.js frontend
├── backend/               # Laravel API
├── docker/                # Docker configuration
├── docs/                  # Documentation
└── README.md
```

See [PROJECT_STRUCTURE.md](./docs/PROJECT_STRUCTURE.md) for detailed breakdown.

## Features

### Super Admin Dashboard
- Global church statistics
- Branch management
- System settings
- Subscription management
- AI insights

### Branch Management
- Department management
- Member management
- Event management
- Attendance tracking
- Communication center

### Finance Module
- Daily offerings & tithes
- Expense tracking
- Payroll management
- Financial reports
- Payment integrations

### Member Portal
- Profile management
- Online giving
- Event registration
- Prayer requests
- Livestream access

## Documentation

- [Installation Guide](./docs/INSTALLATION.md)
- [API Documentation](./docs/API.md)
- [Architecture Guide](./docs/ARCHITECTURE.md)
- [Deployment Guide](./docs/DEPLOYMENT.md)
- [Contributing Guidelines](./CONTRIBUTING.md)

## Security

- JWT authentication
- Role-Based Access Control (RBAC)
- API rate limiting
- Data encryption
- Audit logging
- Activity monitoring

## Support

For support, contact: support@kingdomconnect.com

## License

MIT License - See [LICENSE](./LICENSE) file for details.

## Version

v1.0.0 - Initial Release
