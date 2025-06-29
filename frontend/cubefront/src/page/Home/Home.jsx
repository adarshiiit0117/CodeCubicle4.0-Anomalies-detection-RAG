import React from 'react';

const Home = () => {
  return (
    <div className="relative min-h-screen overflow-hidden">
      <div
        className="absolute inset-0 bg-cover bg-center bg-no-repeat opacity-100"
        style={{ backgroundImage: "url('/image.png')" }}
      />

      <div className="relative z-10 flex flex-col items-center justify-center min-h-screen text-center px-4">
        <div className="bg-blue-700 bg-opacity-70 rounded-2xl p-8 text-white max-w-4xl shadow-lg">
          <h1 className="text-5xl md:text-7xl font-extrabold drop-shadow-lg mb-6 text-yellow-400">
            Welcome to Logistics Pulse Copilot
          </h1>

          <p className="text-lg md:text-2xl">
            We monitor live shipment data to detect route deviations, abnormal pricing, and potential fraud in real-time.
            <br />
            Our RAG-based copilot instantly flags anomalies and retrieves relevant policies or historical data to support fast decisions.
          </p>
        </div>
      </div>
    </div>
  );
};

export default Home;
