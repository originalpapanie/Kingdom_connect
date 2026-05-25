export default function Home() {
  return (
    <main className="min-h-screen bg-gradient-to-br from-slate-900 to-slate-800">
      <div className="container mx-auto px-4 py-20">
        <div className="text-center space-y-6">
          <h1 className="text-5xl font-bold text-white">
            Welcome to KingdomConnect
          </h1>
          <p className="text-xl text-slate-300">
            Comprehensive church management platform for modern ministries
          </p>
          <div className="flex gap-4 justify-center mt-8">
            <button className="px-8 py-3 bg-blue-600 hover:bg-blue-700 text-white rounded-lg font-semibold transition">
              Get Started
            </button>
            <button className="px-8 py-3 border-2 border-slate-400 text-slate-300 hover:bg-slate-700 rounded-lg font-semibold transition">
              Learn More
            </button>
          </div>
        </div>
      </div>
    </main>
  );
}
