import React from 'react';

const Auth = () => {
  return (
    <div className="h-screen w-screen flex">
      {/* Left half: Blue background with heading and info text */}
      <div className="w-1/2 bg-blue-900 flex items-start justify-start p-10">
        <div className="text-yellow-400 max-w-md">
          <h1 className="text-6xl font-extrabold text-red-800 mb-6">
            LOGISTICS PULSE COPILOT
          </h1>
          <p className="text-lg font-medium leading-relaxed">
            We monitor live shipment data to detect route deviations, abnormal pricing, and potential fraud in real-time.
            <br /><br />
            Our RAG-based copilot instantly flags anomalies and retrieves relevant policies or historical data to support fast decisions.
          </p>
        </div>
      </div>

      {/* Right half: Background image with login form */}
      <div
        className="w-1/2 relative flex items-center justify-center"
        style={{
          backgroundImage: `url("/image.png")`,
          backgroundSize: 'cover',
          backgroundPosition: 'center',
          backgroundRepeat: 'no-repeat',
        }}
      >
        <div className="absolute inset-0 bg-black/40" />

        <div className="relative z-10 bg-black/60 shadow-2xl rounded-md w-[28rem] p-8 flex flex-col items-center">
          <h1 className="text-3xl font-bold mb-6 text-yellow-400">Login</h1>

          <form className="w-full space-y-4">
            <input
              type="text"
              placeholder="Username"
              className="w-full px-4 py-2 rounded bg-gray-900/80 text-white placeholder-gray-400"
            />
            <input
              type="password"
              placeholder="Password"
              className="w-full px-4 py-2 rounded bg-gray-900/80 text-white placeholder-gray-400"
            />
            <button
              type="submit"
              className="w-full bg-yellow-500 hover:bg-yellow-600 text-black font-bold py-2 rounded"
            >
              Sign In
            </button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default Auth;
