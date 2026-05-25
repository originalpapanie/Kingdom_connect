import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'KingdomConnect - Church Management SaaS',
  description: 'Comprehensive church management platform for modern ministries',
  viewport: 'width=device-width, initial-scale=1',
  keywords: ['church', 'management', 'SaaS', 'ministry'],
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className="bg-background text-foreground antialiased">
        {children}
      </body>
    </html>
  );
}
